"""
query.py -- answer ONE question from the frozen wiki.

Mirrors the RAG baseline's query shape (locate -> retrieve -> answer), differing only in
WHAT is indexed: synthesised wiki pages instead of raw chunks.

Two LLM calls per question:
  1. ROUTE  -- given index.md and the question, pick the pages to read.
  2. ANSWER -- given those pages (plus one hop of their Related links), answer with
               (AIE p.NNN) citations, or decline if the wiki does not cover it.

The wiki is FROZEN: this script never creates or modifies a page. No write-back.

NOTE: anthropic SDK 1.8.0 removed the `temperature` parameter, so runs are not
temperature-pinned. Reproducibility is instead handled by saving every run's full
output (routed pages, hopped pages, answer) so results are auditable after the fact.
Build-blind is preserved -- the questions were never shown to ingest.

Usage:
    uv run query.py "What is model distillation?"
    uv run query.py "..." --no-hop      # ablation: skip link-following
    uv run query.py "..." --json        # machine-readable, for run_eval.py
    uv run query.py "..." --bm25        # hybrid: LLM routing UNION BM25 over page bodies
"""
from __future__ import annotations
import argparse, json, os, re, sys
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
WIKI = ROOT / "wiki"
PAGE_DIRS = ["concepts", "entities", "syntheses"]
MODEL = os.getenv("WIKI_MODEL", "claude-sonnet-5")
MAX_TOKENS = 4000
MAX_PAGES = 6          # default cap on routed pages (RAG used top_n=3; use --max-pages 3 to match)
MAX_HOP_PAGES = 6      # cap on additional pages pulled in via Related links
VERSION = "query.py v3.1 (route + 1-hop, max-pages, bm25-union, refusal-safe)"
BM25_K = 3             # pages BM25 adds to the router's picks when --bm25 is on

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]")


def load_pages() -> dict[str, Path]:
    out = {}
    for d in PAGE_DIRS:
        for f in (WIKI / d).glob("*.md"):
            out[f.stem] = f
    return out


STOPWORDS = set("""a an and are as at be by can do does for from has have how i in is it its
of on or that the their this to was what when where which who why will with you your about
into than then these those there been being more most other such only also so if not no""".split())
# Words every page contains for STRUCTURAL reasons (section headers, Related keywords,
# citation labels). Left in, they give every page a small positive score for any
# question that happens to use them ("AI-related"), so BM25 would add junk pages.
STOPWORDS |= set("""related provenance key figures examples none aie sources see also
contrast part example prerequisite boundary""".split())
_BM25 = None  # (bm25, slugs) cache


def _tokens(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOPWORDS and len(w) > 1]


def _page_body(text: str) -> str:
    """Searchable content only: drop YAML frontmatter, the Provenance section, heading
    lines, and [[wikilink]] slugs (link targets are other pages' names, not this page's
    content). Related-link REASONS are kept, since they describe real relationships."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    text = re.split(r"(?m)^## Provenance\s*$", text)[0]
    text = re.sub(r"(?m)^#+ .*$", "", text)
    text = LINK_RE.sub(" ", text)
    return text


def bm25_search(question: str, pages: dict[str, Path], k: int = BM25_K) -> list[str]:
    """Deterministic keyword retrieval over page BODIES (not index summaries)."""
    global _BM25
    if _BM25 is None:
        from rank_bm25 import BM25Okapi
        slugs = sorted(pages)
        corpus = [_tokens(_page_body(pages[s].read_text(encoding="utf-8"))) for s in slugs]
        _BM25 = (BM25Okapi(corpus), slugs)
    bm25, slugs = _BM25
    scores = bm25.get_scores(_tokens(question))
    ranked = sorted(range(len(slugs)), key=lambda i: -scores[i])
    return [slugs[i] for i in ranked[:k] if scores[i] > 0]


def related_targets(text: str) -> list[str]:
    m = re.search(r"(?m)^## Related\s*$", text)
    if not m:
        return []
    nxt = re.search(r"(?m)^## ", text[m.end():])
    block = text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():]
    return [t.strip().split("/")[-1] for t in LINK_RE.findall(block)]


def route(client, question: str, index_text: str, max_pages: int = MAX_PAGES) -> list[str]:
    system = (
        "You route questions to pages in a markdown wiki. You are given the wiki's index "
        "and a question. Return ONLY a JSON array of page slugs (no prose, no fences) for "
        "the pages most likely to contain the answer, most relevant first, at most "
        f"{max_pages}. Use slugs exactly as they appear in the index. If the wiki clearly "
        "does not cover the question's topic at all, return an empty array []."
    )
    user = f"=== WIKI INDEX ===\n{index_text}\n\n=== QUESTION ===\n{question}\n\nReturn the JSON array now."
    resp = client.messages.create(model=MODEL, max_tokens=1000,
                                  thinking={"type": "disabled"},
                                  system=system, messages=[{"role": "user", "content": user}])
    raw = "".join(b.text for b in resp.content if b.type == "text").strip()
    s, e = raw.find("["), raw.rfind("]")
    if s == -1 or e == -1:
        return []
    try:
        return [str(x).strip().split("/")[-1] for x in json.loads(raw[s:e + 1])][:max_pages]
    except json.JSONDecodeError:
        return []


def answer(client, question: str, docs: list[tuple[str, str]]) -> str:
    system = (
        "You answer questions using ONLY the wiki pages provided. Rules:\n"
        "- Answer from the supplied pages only. Do not use outside knowledge.\n"
        "- Carry through the (AIE p.NNN) citations that support your claims.\n"
        "- If the supplied pages do not cover the question, say plainly that the wiki "
        "does not cover it. Do not fabricate or guess.\n"
        "- Be direct and complete; no preamble."
    )
    body = "\n\n".join(f"=== PAGE: {slug} ===\n{text}" for slug, text in docs)
    user = f"{body}\n\n=== QUESTION ===\n{question}"
    resp = client.messages.create(model=MODEL, max_tokens=MAX_TOKENS,
                                  thinking={"type": "disabled"},
                                  system=system, messages=[{"role": "user", "content": user}])
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    if not text:
        # e.g. a safety refusal (stop_reason="refusal") returns no text block. Treat it as a
        # decline rather than silently writing an empty answer, and log why.
        print(f"  [answer model returned no text: stop_reason={resp.stop_reason}; recorded as decline]",
              file=sys.stderr)
        return "The wiki does not cover this topic."
    return text


def run(client, question: str, hop: bool = True, max_pages: int = MAX_PAGES,
        bm25: bool = False, bm25_k: int = BM25_K):
    pages = load_pages()
    index_text = (WIKI / "index.md").read_text(encoding="utf-8")

    routed = [s for s in route(client, question, index_text, max_pages) if s in pages]
    bm25_added = []
    if bm25:  # union: BM25 can add pages even when the router returned none
        bm25_added = [s for s in bm25_search(question, pages, bm25_k) if s not in routed]
    if not routed and not bm25_added:
        return {"question": question, "routed": [], "hopped": [], "bm25": [],
                "context_chars": 0, "answer": "The wiki does not cover this topic."}

    docs, seen = [], set()
    for slug in routed + bm25_added:
        docs.append((slug, pages[slug].read_text(encoding="utf-8")))
        seen.add(slug)

    hopped = []
    if hop:
        for slug, text in list(docs):
            for tgt in related_targets(text):
                if tgt in pages and tgt not in seen and len(hopped) < MAX_HOP_PAGES:
                    docs.append((tgt, pages[tgt].read_text(encoding="utf-8")))
                    seen.add(tgt)
                    hopped.append(tgt)

    context_chars = sum(len(t) for _, t in docs)
    return {"question": question, "routed": routed, "hopped": hopped, "bm25": bm25_added,
            "context_chars": context_chars,
            "answer": answer(client, question, docs)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("--no-hop", action="store_true", help="ablation: don't follow Related links")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--max-pages", type=int, default=MAX_PAGES,
                    help="cap on routed pages (3 = RAG-comparable budget)")
    ap.add_argument("--bm25", action="store_true", help="union router picks with BM25 top-k")
    ap.add_argument("--bm25-k", type=int, default=BM25_K)
    args = ap.parse_args()

    from anthropic import Anthropic
    load_dotenv(ROOT / ".env")
    client = Anthropic()

    result = run(client, args.question, hop=not args.no_hop, max_pages=args.max_pages,
                 bm25=args.bm25, bm25_k=args.bm25_k)

    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        print(f"[{VERSION} | model={MODEL} | hop={not args.no_hop}]")
        print(f"routed: {result['routed']}")
        print(f"bm25:   {result.get('bm25', [])}")
        print(f"hopped: {result['hopped']}\n")
        print(result["answer"])


if __name__ == "__main__":
    main()
