"""
segment.py -- cut the book into per-section raw/ files, matching the RAG corpus.

Text comes through extract.py (the SAME extraction the RAG baseline used), so the
wiki's raw layer is the same span, exclusions, and cleaning RAG saw. Boundaries come
from the PDF's own outline (the author's segmentation).

Run once from the llm-wiki repo root (after copying extract.py in and placing the PDF):
    uv run segment.py
Then REVIEW raw/ai-engineering/*.txt before ingesting.
"""
from __future__ import annotations
import re
from pathlib import Path
from pypdf import PdfReader
from extract import extract_book

PDF = "AI_Engineering.pdf"            # the book PDF, placed in the repo (gitignored)
SKIP_FRONT = 20                      # must match rag-book/index_book.py
SKIP_BACK = 1
INDEX_PAGES = set(range(521, 534))   # back-of-book index, excluded exactly as RAG did
PAGE_OFFSET = 24                     # printed book page = PDF page - PAGE_OFFSET
OUT = Path("raw/ai-engineering")


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def outline_entries(reader):
    rows = []
    def walk(items, depth=0):
        for it in items:
            if isinstance(it, list):
                walk(it, depth + 1)
            else:
                try:
                    pg = reader.get_destination_page_number(it) + 1  # 1-indexed PDF page
                except Exception:
                    continue
                rows.append([pg, it.title.strip(), depth])
    walk(reader.outline)
    return rows


def main():
    reader = PdfReader(PDF)
    entries = outline_entries(reader)
    entries.sort(key=lambda r: r[0])

    ch1 = next((pg for pg, t, d in entries if re.match(r"Chapter\s+1\.", t)), 0)

    cur_ch = 0
    for row in entries:
        m = re.match(r"Chapter\s+(\d+)\.", row[1])
        if m:
            cur_ch = int(m.group(1))
        row.append(cur_ch)  # [pg, title, depth, ch]

    cut = [r for r in entries if r[0] >= ch1]  # drop front matter
    starts = [r[0] for r in cut]

    pages = dict(extract_book(PDF, skip_front_pages=SKIP_FRONT,
                              skip_back_pages=SKIP_BACK, exclude_pages=INDEX_PAGES))
    OUT.mkdir(parents=True, exist_ok=True)

    written = 0
    for i, (start, title, depth, ch) in enumerate(cut):
        end = starts[i + 1] if i + 1 < len(cut) else max(pages) + 1  # exclusive
        body = "\n".join(pages[p] for p in range(start, end) if p in pages).strip()
        if len(body) < 50:
            continue
        clean = re.sub(r"^Chapter\s+\d+\.\s*", "", title)
        slug = f"ch{ch:02d}-{slugify(clean)}"
        bs, be = start - PAGE_OFFSET, end - 1 - PAGE_OFFSET
        header = (f"# Source: Chip Huyen, AI Engineering (O'Reilly, 2024)\n"
                  f"# Chapter {ch} -> {title}\n"
                  f"# Book pages: {bs}-{be}  (PDF pages {start}-{end - 1})\n"
                  f"# Immutable raw source. Do not edit.\n\n")
        (OUT / f"{slug}.txt").write_text(header + body + "\n", encoding="utf-8")
        written += 1
        print(f"{slug}.txt  book pp.{bs}-{be}  ({len(body)} chars)")
    print(f"\n{written} section files written.")


if __name__ == "__main__":
    main()
