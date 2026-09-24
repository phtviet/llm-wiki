"""
segment.py -- cut the book into per-subsection raw/ files, matching the RAG corpus.

Text comes through extract.py (the SAME extraction RAG used), so the raw layer is the
same span/exclusions/cleaning RAG saw. Boundaries are the book's own subsection HEADINGS
(from the PDF outline), located in the text and cut there -- so a section is one whole
concept regardless of where page breaks fall.

Run once from the llm-wiki repo root (extract.py copied in, PDF placed in the repo):
    uv run segment.py
Then REVIEW raw/ai-engineering/*.txt before ingesting.
"""
from __future__ import annotations
import re
from pathlib import Path
from pypdf import PdfReader
from extract import extract_book

PDF = "AI_Engineering.pdf"
SKIP_FRONT = 20
SKIP_BACK = 1
INDEX_PAGES = set(range(521, 534))
PAGE_OFFSET = 24                      # printed book page = PDF page - PAGE_OFFSET
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
                    pg = reader.get_destination_page_number(it) + 1
                except Exception:
                    continue
                rows.append([pg, it.title.strip(), depth])
    walk(reader.outline)
    return rows


def find_heading(page_text: str, title: str):
    """Locate a heading in a page's text, tolerant of whitespace. Returns offset or None."""
    clean = re.sub(r"^Chapter\s+\d+\.\s*", "", title)
    words = [re.escape(w) for w in clean.split()]
    if not words:
        return None
    pattern = r"\s+".join(words)
    m = re.search(pattern, page_text, re.IGNORECASE)
    return m.start() if m else None


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

    pages = extract_book(PDF, skip_front_pages=SKIP_FRONT,
                         skip_back_pages=SKIP_BACK, exclude_pages=INDEX_PAGES)
    page_text = {p: t for p, t in pages}

    # Concatenate in page order; remember where each page starts, to map offsets->pages.
    full, page_start, off = [], [], 0
    for p, t in pages:
        page_start.append((off, p))
        full.append(t)
        off += len(t) + 1
    full_text = "\n".join(t for _, t in pages)

    def page_of(offset):
        pg = page_start[0][1]
        for o, p in page_start:
            if o <= offset:
                pg = p
            else:
                break
        return pg

    # Compute a cut offset for every heading at/after Chapter 1.
    cuts, misses = [], 0
    for pg, title, depth, ch in entries:
        if pg < ch1:
            continue
        pt = page_text.get(pg, "")
        pos = find_heading(pt, title)
        if pos is None:  # heading text not found on its page -> fall back to page start, flag it
            pstart = next((o for o, p in page_start if p == pg), None)
            if pstart is None:
                continue
            cuts.append((pstart, title, ch, False))
            misses += 1
        else:
            pstart = next(o for o, p in page_start if p == pg)
            cuts.append((pstart + pos, title, ch, True))
    cuts.sort(key=lambda c: c[0])

    OUT.mkdir(parents=True, exist_ok=True)
    written = 0
    seen = {}
    for i, (offset, title, ch, matched) in enumerate(cuts):
        end = cuts[i + 1][0] if i + 1 < len(cuts) else len(full_text)
        body = full_text[offset:end].strip()
        if len(body) < 50:
            continue
        clean = re.sub(r"^Chapter\s+\d+\.\s*", "", title)
        slug = f"ch{ch:02d}-{slugify(clean)}"
        if slug in seen:
            seen[slug] += 1
            slug = f"{slug}-{seen[slug]}"
        else:
            seen[slug] = 1
        bs = page_of(offset) - PAGE_OFFSET
        be = page_of(end - 1) - PAGE_OFFSET
        flag = "" if matched else "   [HEADING NOT MATCHED -> page-cut fallback, review]"
        header = (f"# Source: Chip Huyen, AI Engineering (O'Reilly, 2024)\n"
                  f"# Chapter {ch} -> {title}\n"
                  f"# Book pages: {bs}-{be}\n"
                  f"# Immutable raw source. Do not edit.\n\n")
        (OUT / f"{slug}.txt").write_text(header + body + "\n", encoding="utf-8")
        written += 1
        print(f"{slug}.txt  book pp.{bs}-{be}  ({len(body)} chars){flag}")
    print(f"\n{written} files. {misses} heading(s) not matched (page-cut fallback).")


if __name__ == "__main__":
    main()
