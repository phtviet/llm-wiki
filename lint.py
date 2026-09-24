"""
lint.py -- Phase C: build-correctness check over the finished wiki. No LLM, read-only
by default.

Checks (per SCHEMA.md section 11):
  1. Broken [[wikilinks]]      -- target page does not exist
  2. Orphan pages              -- no inbound links from any other page
  3. Index drift               -- index lists a missing page, or omits an existing one
  4. Bare Related links        -- a Related link with no reason in parentheses
  5. Bad Related keywords      -- reason does not lead with a keyword from the closed set
  6. Unresolved citation labels-- (LABEL p.N) whose LABEL is not declared on a sources/ page
  7. Asymmetric links          -- A links B in Related but B does not link back
  8. Numeric-claim / empty Key figures -- prose has figures but Key figures says None

Usage:
    uv run lint.py              # report everything
    uv run lint.py --summary    # counts only
"""
from __future__ import annotations
import argparse, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WIKI = ROOT / "wiki"
PAGE_DIRS = ["concepts", "entities", "syntheses"]
KEYWORDS = {"contrast", "part-of", "example-of", "prerequisite", "boundary", "see-also"}

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]")
REL_LINE_RE = re.compile(r"(?m)^\s*-\s*\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]\s*(.*)$")
CITE_RE = re.compile(r"\(([A-Z][A-Za-z0-9_-]{1,15})\s+p\.\s?\d+")


def related_block(text: str) -> str:
    m = re.search(r"(?m)^## Related\s*$", text)
    if not m:
        return ""
    nxt = re.search(r"(?m)^## ", text[m.end():])
    return text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():]


def key_figures_block(text: str) -> str:
    m = re.search(r"(?m)^## Key figures\s*$", text)
    if not m:
        return ""
    nxt = re.search(r"(?m)^## ", text[m.end():])
    return text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", action="store_true")
    args = ap.parse_args()

    pages, sources = {}, {}
    for d in PAGE_DIRS:
        for f in (WIKI / d).glob("*.md"):
            pages[f.stem] = {"text": f.read_text(encoding="utf-8"), "dir": d, "path": f}
    for f in (WIKI / "sources").glob("*.md"):
        sources[f.stem] = f.read_text(encoding="utf-8")

    valid = set(pages) | {f"sources/{s}" for s in sources} | set(sources)
    labels = set()
    for t in sources.values():
        m = re.search(r"(?m)^label:\s*(\S+)", t)
        if m:
            labels.add(m.group(1))

    issues = defaultdict(list)
    inbound = defaultdict(set)
    rel_map = defaultdict(set)

    for slug, info in pages.items():
        text = info["text"]

        # 1. broken links
        for tgt in LINK_RE.findall(text):
            tgt = tgt.strip()
            base = tgt.split("/")[-1]
            if tgt not in valid and base not in valid:
                issues["broken_links"].append(f"{info['dir']}/{slug} -> [[{tgt}]]")
            else:
                if base != slug and base in pages:
                    inbound[base].add(slug)

        # 4/5. Related line quality
        for tgt, reason in REL_LINE_RE.findall(related_block(text)):
            tgt = tgt.strip().split("/")[-1]
            if tgt in pages:
                rel_map[slug].add(tgt)
            reason = reason.strip()
            if not reason:
                issues["bare_links"].append(f"{info['dir']}/{slug} -> [[{tgt}]]")
                continue
            inner = reason.lstrip("(").strip()
            first = inner.split(":")[0].strip().lower()
            if first not in KEYWORDS:
                issues["bad_keyword"].append(f"{info['dir']}/{slug} -> [[{tgt}]]  ({first[:30]})")

        # 6. citation labels
        for lab in set(CITE_RE.findall(text)):
            if lab not in labels:
                issues["unknown_label"].append(f"{info['dir']}/{slug}: ({lab} p.N)")

        # 8. numeric claim but empty Key figures
        kf = key_figures_block(text)
        if kf.strip().lower().startswith("none"):
            body = text.split("## Key figures")[0]
            if re.search(r"\b\d+(\.\d+)?\s?%|\b\d{2,}B\b|\b\d+ billion\b", body):
                issues["figure_maybe_lost"].append(f"{info['dir']}/{slug}")

    # 2. orphans
    for slug, info in pages.items():
        if not inbound[slug]:
            issues["orphans"].append(f"{info['dir']}/{slug}")

    # 7. asymmetry
    for a, targets in rel_map.items():
        for b in targets:
            if b in rel_map and a not in rel_map[b]:
                issues["asymmetric"].append(f"{a} -> {b} (no back-link)")

    # 3. index drift
    idx = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""
    indexed = {m.split("/")[-1] for m in LINK_RE.findall(idx)}
    for slug in pages:
        if slug not in indexed:
            issues["not_in_index"].append(slug)
    for slug in indexed:
        if slug not in pages:
            issues["index_ghost"].append(slug)

    order = ["broken_links", "orphans", "not_in_index", "index_ghost", "bare_links",
             "bad_keyword", "unknown_label", "asymmetric", "figure_maybe_lost"]
    print(f"{len(pages)} pages, {len(sources)} source pages, labels: {sorted(labels)}\n")
    for k in order:
        v = issues[k]
        print(f"{k:20s} {len(v)}")
        if not args.summary:
            for line in v[:25]:
                print(f"    {line}")
            if len(v) > 25:
                print(f"    ... and {len(v) - 25} more")
    print(f"\nTotal issues: {sum(len(v) for v in issues.values())}")


if __name__ == "__main__":
    main()
