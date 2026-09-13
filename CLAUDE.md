# Wiki Schema (CLAUDE.md)

This file is the operating manual for the agent that maintains this wiki. The agent
reads it before every ingest, query, and lint. It is the constitution; obey it over
instinct.

---

## 1. Purpose and scope

This wiki compiles one immutable source (Chip Huyen, *AI Engineering*) into a
structured, interlinked markdown knowledge base. It exists to be **measured against a
RAG baseline** on a fixed 20-question evaluation set. It is a portfolio artifact, not a
daily-use tool.

Three consequences bind everything below:

- **Frozen for evaluation.** Once built, the wiki is not modified during a query. There
  is no write-back. The `query` operation never creates or edits pages.
- **Built blind to the eval.** The agent is never shown the 20 evaluation questions.
  Pages are built from the source and this schema only. Organising the wiki around the
  questions would be training on the test.
- **Provenance is mandatory.** Every claim points to a page in the immutable book.

---

## 2. Layers and directory structure

```
raw/                      Immutable source. The book, split into section files.
  ai-engineering/
    ch07-s03.txt          One file per ingest unit (a book section).
    ...
wiki/                     LLM-owned. The agent writes here; a human only reads.
  index.md                Catalog of all pages, grouped by topic. Query entry point.
  log.md                  Append-only record of every operation.
  concepts/               Concept pages (ideas, techniques, methods).
  entities/               Entity pages (people, tools, organisations, datasets).
  sources/                One summary page per ingested section (provenance).
CLAUDE.md                 This schema.
```

There is deliberately **no `comparisons/` folder**. Comparison and synthesis answers
are produced at query time by traversing links between atomic pages, not by pre-building
the comparison a question happens to ask. See section 5.

---

## 3. Page types

**Concept page** (`concepts/`): one idea per page. Quantization, distillation,
embeddings, backpropagation, cross-entropy, inference optimisation, and so on. This is
the primary retrieval substrate; most questions are answered here.

**Entity page** (`entities/`): one named thing per page. A person, tool, org, or
dataset. "Chip Huyen" is an entity page, not a concept page.

**Source-summary page** (`sources/`): one per ingested section. Records what that
section covered and which book pages it spans. Provenance bookkeeping. Queries do not
target these; they are reachable by link for citation verification only.

**Index** (`index.md`): the catalog. Groups every concept and entity page under **book
topic areas** (for example: Training fundamentals, Model compression, Retrieval,
Evaluation, Prompt engineering, People and tools). Topic areas come from the book's own
structure, never from the eval categories.

**Log** (`log.md`): append-only, one line per operation, date-prefixed and parseable.

---

## 4. Page template

Every concept and entity page follows this exact structure.

```markdown
# <Page title>

<One-paragraph definition or description. Plain prose. Every factual claim carries a
book-page citation in the form (AIE p.NNN).>

## Key figures
<Load-bearing numbers preserved verbatim, each with a page cite. A load-bearing figure
is one where the exact value IS the answer: covering it would make a correct answer
impossible. If the source states no such figures, write "None." Do not paraphrase
numbers into prose only; they must survive here exactly.>

- <e.g. DistilBERT is 40% smaller than BERT, 60% faster, retains 97% of language
  understanding (AIE p.NNN)>

## Related
<Links to other pages, each with a short reason for the link. This section is what
carries comparison and synthesis questions, so it must be substantive, not decorative.>

- [[distillation]] — alternative compression method; contrast: modifies precision vs.
  trains a smaller student model
- [[inference-optimization]] — quantization is one technique under this topic

## Provenance
<Which source-summary page(s) this content was drawn from.>

- [[sources/ch07-s03]]
```

The `Key figures` and `Related` sections are the two load-bearing parts of this schema.
The measurement lives or dies on them.

---

## 5. Linking rules

- Links use `[[wikilink]]` syntax (Obsidian-compatible).
- Every link in a `Related` section carries a short reason. A bare link is a lint error.
- Links are **bidirectional in intent**: if A's `Related` cites B, B's `Related` should
  cite A. Lint checks for missing back-links.
- Because there are no pre-built comparison pages, a comparison or synthesis answer is
  built by pulling the atomic pages the question touches and reading their `Related`
  reasons. If two concepts are genuinely related in the book, the link and its reason
  must exist, or the query cannot traverse to them. Missing connective tissue is the
  main way this wiki can fail a synthesis question; treat it as such during ingest.

---

## 6. Citation format

- All claims cite the **immutable book by page**: `(AIE p.143)`.
- Citations never point at wiki pages as if they were sources. A wiki page is never
  evidence for itself or for another wiki page.
- `AIE` is the fixed short label for the book. When other sources are added later, each
  gets its own short label; the format stays `(<label> p.NNN)`.

---

## 7. Index format

`index.md` groups pages by book topic area. Each entry is a link plus a one-line
summary.

```markdown
## Model compression
- [[quantization]] — reduces numerical precision to cut memory and speed up compute
- [[distillation]] — trains a small student to mimic a larger teacher

## People and tools
- [[chip-huyen]] — author; ML systems writer and engineer
```

The index is the query entry point. It must stay in sync with the pages on disk; lint
checks this.

---

## 8. Log format

Append-only. One line per operation. Never edited or reordered.

```
2026-09-06 ingest   ch07-s03  -> +concepts/quantization +concepts/distillation +sources/ch07-s03
2026-09-06 query    "What is quantization?"  -> concepts/quantization  [answered]
2026-09-06 lint     -> 0 broken links, 1 orphan (entities/snorkel), 0 missing back-links
```

---

## 9. Ingest workflow

Input is one section file from `raw/`. Never the whole book at once; sectioned ingest is
what makes extraction clean and facts survive.

1. Read the section.
2. Identify the concepts and entities it introduces or extends.
3. For each, create or update its page per the template. Preserve load-bearing figures
   verbatim into `Key figures`. Cite the book page on every claim.
4. Add `Related` links (with reasons) to existing pages, and back-links on those pages.
5. Write or update the section's `sources/` summary page.
6. Update `index.md`. Append one line to `log.md`.

The agent is never shown the evaluation questions during ingest.

---

## 10. Query protocol

1. Read `index.md`. Route to the relevant concept or entity page(s).
2. For a comparison or synthesis question, pull each page the question touches and follow
   `Related` reasons to any connecting pages.
3. Answer from the retrieved pages only, with book-page citations carried through.
4. If no page covers the question, **decline**: state the topic is not in the wiki. Do
   not fabricate. (This is the correct behaviour for out-of-corpus questions.)
5. Append the query to `log.md`.
6. **Do not create or modify any page.** No write-back. The wiki is frozen.

The query path is deliberately shaped like the RAG baseline's: locate pages, pull them,
synthesise an answer. The only intended difference between the two systems is what is
indexed (synthesised wiki pages vs. raw chunks), not how cleverly retrieval works.

---

## 11. Lint (minimal)

The corpus is frozen, so lint is a build-correctness check, not a contradiction engine.
It checks only:

- Broken `[[wikilinks]]` (target page missing).
- Orphan pages (in `wiki/` but absent from `index.md`, or with no inbound links).
- Index-vs-disk drift (index lists a page that does not exist, or omits one that does).
- Bare `Related` links (a link with no reason).
- Pages with numeric claims in prose but an empty `Key figures` section (possible
  load-bearing figure lost to paraphrase).

Lint fixes what it safely can and reports the rest. It does not rewrite page content.

---

## 12. Integrity guards (do not relax)

1. Build blind to the 20 evaluation questions.
2. Do not edit the evaluation set to suit the wiki. Verify its balance; leave it as is.
3. Provenance on every claim, pointing into the immutable book by page.
4. Freeze the wiki before scoring. Write-back stays off for the core comparison.
