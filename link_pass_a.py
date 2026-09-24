"""
link_pass_a.py -- Phase A of the linking pass: mechanical, deterministic, no LLM.

Finds places where a page's body mentions ANOTHER page's title as plain text but does
not link it, wraps the mention in [[wikilinks]], and adds a Related line for it.

Additive and conservative by design:
  - Only wraps the FIRST unlinked mention of a title in a page body.
  - Never rewrites or reflows existing prose; only inserts [[ ]] around an exact match.
  - Only appends to Related; never edits or removes an existing Related line.
  - Skips matches inside frontmatter, headings, existing [[links]], and code spans.

Usage:
    uv run link_pass_a.py --dry-run     # report what WOULD change
    uv run link_pass_a.py               # apply
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WIKI = ROOT / "wiki"
PAGE_DIRS = ["concepts", "entities", "syntheses"]
MIN_TITLE_LEN = 5          # don't match very short titles (too many false hits)

# Single-word page titles that are also ordinary English and produce false matches.
# A page with one of these titles is still a real page and still gets linked FROM
# elsewhere -- it is just never auto-linked by bare text match.
BLOCKED_TITLES = {
    "memory", "token", "tokens", "evaluation", "agent", "agents", "planning",
    "sampling", "vocabulary", "infrastructure", "monitoring", "router", "kernel",
    "embedding", "embeddings", "retriever", "safety", "supervision", "pruning",
    "batching", "perturbation", "inconsistency", "hallucination", "temperature",
    "quantization", "perplexity", "entropy", "finetuning", "seq2seq", "softmax",
    "logprobs", "rag", "rlhf", "peft", "lora", "qlora", "gpu",
}
REASON = "see-also: mentioned in this page's text"


def page_title(text: str, slug: str) -> str:
    m = re.search(r"(?m)^#\s+(.+)$", text)
    return m.group(1).strip() if m else slug.replace("-", " ")


def load_pages():
    pages = {}
    for d in PAGE_DIRS:
        for f in (WIKI / d).glob("*.md"):
            t = f.read_text(encoding="utf-8")
            pages[f.stem] = {"path": f, "text": t, "title": page_title(t, f.stem), "dir": d}
    return pages


def split_page(text: str):
    """Return (frontmatter, body_before_related, related_block, tail)."""
    fm = ""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            end = text.find("\n", end + 1)
            fm, text = text[:end + 1], text[end + 1:]
    m = re.search(r"(?m)^## Related\s*$", text)
    if not m:
        return fm, text, None, ""
    rel_start = m.start()
    nxt = re.search(r"(?m)^## ", text[m.end():])
    rel_end = m.end() + nxt.start() if nxt else len(text)
    return fm, text[:rel_start], text[rel_start:rel_end], text[rel_end:]


def already_links(page_text: str, slug: str) -> bool:
    return f"[[{slug}]]" in page_text


def find_unlinked(body: str, title: str):
    """First occurrence of `title` in body that isn't already inside [[ ]] or a heading."""
    pat = re.compile(r"(?<!\[\[)\b" + re.escape(title) + r"\b(?!\]\])", re.IGNORECASE)
    for m in pat.finditer(body):
        line_start = body.rfind("\n", 0, m.start()) + 1
        line = body[line_start:body.find("\n", m.start()) if body.find("\n", m.start()) != -1 else len(body)]
        if line.lstrip().startswith("#"):      # skip headings
            continue
        if "[[" in line[:m.start() - line_start] and "]]" in line[m.start() - line_start:]:
            continue
        return m
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    pages = load_pages()
    print(f"{len(pages)} pages loaded\n")

    # title -> slug, longest titles first so "model distillation" beats "distillation"
    targets = sorted(
        ((info["title"], slug) for slug, info in pages.items()
         if len(info["title"]) >= MIN_TITLE_LEN
         and info["title"].strip().lower() not in BLOCKED_TITLES),
        key=lambda x: -len(x[0]),
    )

    changed, new_links = 0, 0
    for slug, info in sorted(pages.items()):
        text = info["text"]
        fm, body, related, tail = split_page(text)
        additions = []
        for title, tslug in targets:
            if tslug == slug or already_links(text, tslug):
                continue
            m = find_unlinked(body, title)
            if not m:
                continue
            shown = m.group(0)
            link = f"[[{tslug}]]" if shown.lower() == tslug.replace("-", " ").lower() else f"[[{tslug}|{shown}]]"
            body = body[:m.start()] + link + body[m.end():]
            additions.append(f"- [[{tslug}]]  ({REASON})")
            text = fm + body + (related or "") + tail  # keep in sync for already_links checks
        if not additions:
            continue
        if related is None:
            related = "## Related\n" + "\n".join(additions) + "\n"
            new_text = fm + body.rstrip() + "\n\n" + related + tail
        else:
            new_text = fm + body + related.rstrip() + "\n" + "\n".join(additions) + "\n\n" + tail.lstrip("\n")
        changed += 1
        new_links += len(additions)
        print(f"{info['dir']}/{slug}.md  +{len(additions)} link(s): " +
              ", ".join(a.split("]]")[0].replace("- [[", "") for a in additions))
        if not args.dry_run:
            info["path"].write_text(new_text, encoding="utf-8")

    print(f"\n{changed} page(s) would change, {new_links} new link(s)." if args.dry_run
          else f"\n{changed} page(s) updated, {new_links} new link(s) added.")


if __name__ == "__main__":
    main()
