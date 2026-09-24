"""
ingest.py -- one-section ingest for the LLM wiki.

Reads ONE raw section file, plus SCHEMA.md and the current wiki/index.md, and asks the
model to produce/update the wiki pages for that section, obeying the schema. Writes the
pages, merges index.md, appends to log.md, and records any review flags.

Build-blind by construction: this script never reads the evaluation questions.

Usage:
    # calibration run: schema only, no few-shot exemplars, don't write yet
    uv run ingest.py raw/ai-engineering/ch08-model-distillation.txt --dry-run

    # with few-shot exemplars (for sections OTHER than the one you hand-authored)
    uv run ingest.py raw/ai-engineering/ch09-quantization.txt \
        --exemplars concepts/model-distillation.md entities/distilbert.md
"""
from __future__ import annotations
import argparse, json, sys, os, datetime
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
WIKI = ROOT / "wiki"
SCHEMA_PATH = ROOT / "SCHEMA.md"
EXEMPLARS_DIR = ROOT / "exemplars"
# Set to your current preferred model. Escalate to a stronger model only if calibration
# shows this one falls short of your hand pages. Check docs.claude.com for current names.
MODEL = os.getenv("WIKI_MODEL", "claude-sonnet-5")
MAX_TOKENS = 16000  # output budget; thinking is disabled below so this is all for output
VERSION = "ingest.py v3 (retry + exemplar guard)"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def build_system(schema: str) -> str:
    return (
        "You are the ingest agent for a structured markdown wiki. The schema below is your "
        "constitution; obey it exactly, over any instinct.\n\n"
        "You are given ONE source section, the current wiki index, and optionally exemplar "
        "pages. Produce the concept / entity / synthesis pages the section calls for, plus "
        "its one source-summary page, following the schema's page template, entity bar, "
        "fact-placement rule, citation format, and closed Related-keyword set. Invent "
        "nothing: every factual claim carries a (LABEL p.NNN) citation whose page number "
        "comes from the section text. If a Related link needs a relationship the keyword "
        "set does not cover, use the closest keyword and add a review_flag; never coin a "
        "new keyword. You never see the evaluation questions.\n\n"
        "Exemplar pages, when provided, show page STYLE and section PLACEMENT only. They do "
        "NOT limit which pages you create. Apply the entity bar and concept bar to THIS "
        "section in full and create every page they require, even when the exemplars are "
        "sparser than the section warrants. Concretely: work through every named thing in "
        "the section, and if it has a definition plus at least one distinct attribute or "
        "figure of its own here, it gets its own entity page, regardless of whether it plays "
        "a supporting role or whether the exemplars happen to include a similar page. Do not "
        "let an exemplar's restraint suppress a page the bar requires.\n\n"
        "The CONCEPT bar is strict, and violating it is the most common failure. In "
        "overview, summary, or list-heavy sections, most named concepts are only NAMED, "
        "not developed. A concept earns a page ONLY if THIS section actually explains it: "
        "gives its mechanism, definition, or substantive detail of its own. A concept that "
        "appears only as an item in a list, a one-line mention, a use-case blurb, or a "
        "forward reference to a later chapter stays a dangling [[link]], NOT a page. "
        "Example: a section that lists 'training, finetuning, inference optimization' as "
        "steps in a workflow without explaining each creates LINKS to them, not pages. "
        "When unsure, prefer a link over a page. A page for a merely-named concept is a "
        "failure, not a happy accident.\n\n"
        "INDEX: index_entries lists ONLY concept, entity, and synthesis pages. NEVER add a "
        "sources/ page to index_entries -- source pages are provenance records, not query "
        "targets, and must stay out of the index.\n\n"
        "SLUGS: if a concept or entity already appears in the current index, reuse its "
        "EXACT existing slug and target that same page. Never invent a variant slug "
        "(e.g. 'evaluation-ch1', 'finetuning-2') for something that already exists.\n\n"
        "UPDATING: only use action 'update' when THIS section adds substantive new content "
        "to an existing page. If your section merely mentions or references a concept that "
        "already has a page, LINK to it and do not rewrite it -- never overwrite a fuller "
        "existing page with a thinner, passing-mention version.\n\n"
        "Review flags belong ONLY in the top-level review_flags array. NEVER write a "
        "[review_flag: ...] note, or any other flag, aside, or bracketed comment, inside a "
        "page's content. Page content is the finished wiki page a reader sees and must "
        "contain nothing but the page itself. A dangling link to a not-yet-created page is "
        "normal: leave the page text clean and, if worth surfacing, note it in review_flags.\n\n"
        "Your output MUST be valid, parseable JSON. Inside string values, escape every "
        "double quote as \\\" and every backslash as \\\\. Avoid double quotes inside "
        "page text where possible -- use single quotes instead.\n\n"
        "Return ONLY a JSON object, no prose, no code fences, with this exact shape:\n"
        "{\n"
        '  "pages": [{"path": "concepts/<slug>.md", "action": "create" or "update",\n'
        '             "content": "<full markdown including frontmatter>"}],\n'
        '  "index_entries": [{"topic": "<book topic area>",\n'
        '                     "line": "- [[<slug>]] -- <one-line summary>"}],\n'
        '  "review_flags": ["<no-fit keyword or judgment call needing a human>"],\n'
        '  "log_summary": "<+concepts/x +entities/y +sources/z>"\n'
        "}\n\n"
        "=== SCHEMA (your constitution) ===\n" + schema
    )


def build_user(section_name, section_stem, section_text, index_text, exemplars):
    parts = [f"=== CURRENT wiki/index.md ===\n{index_text or '(empty -- this is an early ingest)'}\n"]
    for name, content in exemplars:
        parts.append(f"=== EXEMPLAR PAGE: {name} ===\n{content}\n")
    parts.append(f"Source-summary page path: sources/{section_stem}.md (define its citation label per the schema).")
    parts.append(f"=== SOURCE SECTION: {section_name} ===\n{section_text}\n")
    parts.append("Produce the JSON now.")
    return "\n".join(parts)


def parse_json(raw: str) -> dict:
    """Extract the JSON object by braces, so preambles and code fences don't break it."""
    raw = raw.strip()
    start, end = raw.find("{"), raw.rfind("}")
    if start == -1 or end == -1 or end < start:
        raise ValueError(f"No JSON object found in model output:\n{raw[:800]}")
    return json.loads(raw[start:end + 1], strict=False)


def merge_index(index_path: Path, entries: list[dict]) -> None:
    lines = index_path.read_text(encoding="utf-8").splitlines() if index_path.exists() else []
    for e in entries:
        header = f"## {e['topic']}"
        line = e["line"]
        if header in lines:
            i = lines.index(header)
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "):
                j += 1
            if line not in lines[i:j]:
                lines.insert(j, line)
        else:
            if lines and lines[-1].strip():
                lines.append("")
            lines += [header, line]
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("section", help="path to a raw section file")
    ap.add_argument("--exemplars", nargs="*", default=[], help="wiki-relative exemplar page paths")
    ap.add_argument("--dry-run", action="store_true", help="print the model's JSON, write nothing")
    args = ap.parse_args()

    print(f"[{VERSION} | model={MODEL}]")
    section_path = Path(args.section)
    section_text = read(section_path)
    if not section_text:
        sys.exit(f"Empty or missing section: {section_path}")

    schema = read(SCHEMA_PATH)
    if not schema:
        sys.exit(f"SCHEMA.md not found at {SCHEMA_PATH}")
    index_text = read(WIKI / "index.md")
    exemplars = []
    for e in args.exemplars:
        content = read(EXEMPLARS_DIR / e)
        if not content.strip():
            sys.exit(f"Exemplar missing or empty: {EXEMPLARS_DIR / e}\n"
                     f"(exemplars are read from {EXEMPLARS_DIR}, not wiki/)")
        exemplars.append((e, content))

    from anthropic import Anthropic  # imported here so --help / tests need no key
    load_dotenv(ROOT / ".env")
    client = Anthropic()  # reads ANTHROPIC_API_KEY

    user_msg = build_user(section_path.name, section_path.stem, section_text, index_text, exemplars)
    system_msg = build_system(schema)

    data = None
    last_err = None
    for attempt in range(1, 4):  # up to 3 tries: malformed JSON on big sections is common
        messages = [{"role": "user", "content": user_msg}]
        if attempt > 1:
            messages[0]["content"] += (
                f"\n\nNOTE: your previous reply was not valid JSON ({last_err}). "
                "Return ONLY a valid JSON object this time. Escape all inner double quotes."
            )
        resp = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            thinking={"type": "disabled"},
            system=system_msg,
            messages=messages,
        )
        if resp.stop_reason == "max_tokens":
            sys.exit(f"Output hit max_tokens ({MAX_TOKENS}) and was truncated. Raise MAX_TOKENS.")
        raw = "".join(b.text for b in resp.content if b.type == "text")
        if not raw.strip():
            sys.exit(f"No text in reply (stop_reason={resp.stop_reason}); blocks={[b.type for b in resp.content]}")
        try:
            data = parse_json(raw)
            break
        except (json.JSONDecodeError, ValueError) as e:
            last_err = str(e)[:120]
            print(f"  attempt {attempt}: bad JSON ({last_err}); retrying" if attempt < 3 else
                  f"  attempt {attempt}: bad JSON ({last_err})")
    if data is None:
        sys.exit(f"Failed to get valid JSON after 3 attempts: {last_err}")


    if args.dry_run:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    written = []
    for pg in data["pages"]:
        dest = WIKI / pg["path"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(pg["content"].rstrip() + "\n", encoding="utf-8")
        written.append(f"{pg['action']} {pg['path']}")

    merge_index(WIKI / "index.md", data.get("index_entries", []))

    flags = data.get("review_flags", [])
    if flags:
        with (WIKI / "_review.md").open("a", encoding="utf-8") as f:
            for fl in flags:
                f.write(f"- [{section_path.name}] {fl}\n")

    today = datetime.date.today().isoformat()
    with (WIKI / "log.md").open("a", encoding="utf-8") as f:
        f.write(f"{today} ingest   {section_path.stem}  -> {data.get('log_summary', '')}\n")

    print("Wrote:")
    for w in written:
        print(f"  {w}")
    if flags:
        print(f"\n{len(flags)} review flag(s) -> wiki/_review.md")


if __name__ == "__main__":
    main()
