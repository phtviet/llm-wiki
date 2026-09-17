# Wiki Schema

This file is the operating manual for the agent that maintains this wiki. The agent
reads it before every ingest, query, and lint. It is the constitution; obey it over
instinct.

It is tool-agnostic. It says "the agent," never names a model, and works whether the
agent runs on Claude, GPT, or anything else. The filename is a convention, not a
dependency: your ingest and query scripts load this file by explicit path, so the name
is yours to choose. (See "Portability" at the end.)

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
  Every build decision is made as if the eval did not exist. Test for any decision:
  would I do this if I had never seen the questions? If it only makes sense because a
  question asks for it, stop. Shaping the wiki around the questions is training on the
  test.
- **Provenance is mandatory.** Every claim points to a page in the immutable book.

**Maintenance is deferred.** Continuous-maintenance operations (deduplication,
re-ingest, staleness checks, contradiction resolution) belong to the separate personal
fork built after v1.0, not to this frozen measured build. Their absence here is a
decision, not an oversight.

---

## 2. Layers and directory structure

```
raw/                      Immutable source. The book, split into section files.
  ai-engineering/
    ch08-model-distillation.txt   One file per ingest unit (a book section).
    ...
wiki/                     LLM-owned. The agent writes here; a human only reads.
  index.md                Catalog of all pages, grouped by topic. Query entry point.
  log.md                  Append-only record of every operation.
  _review.md              Human-review queue (e.g. no-fit keyword flags). Minimal; see section 9.
  concepts/               Concept pages (ideas, techniques, methods).
  entities/               Entity pages (people, tools, orgs, datasets, models).
  sources/                One page per ingested section. Provenance + citation label.
  syntheses/              Cross-cutting pages the source itself makes (see section 3).
SCHEMA.md                 This schema.
```

---

## 3. Page types

**Concept page** (`concepts/`): one idea per page. Quantization, distillation,
embeddings, backpropagation, cross-entropy, and so on. Primary retrieval substrate.

**Entity page** (`entities/`): one named thing per page. A person, tool, org, dataset,
or model. "Chip Huyen" and "DistilBERT" are entity pages. Governed by the entity bar
(section 4).

**Synthesis page** (`syntheses/`): a cross-cutting analysis or comparison that **the
source itself draws**, captured as one page. The book contrasting data-centric and
model-centric AI is a synthesis; a comparison written because an eval question asks for
it is not (that is a build-blind violation). Synthesis pages are built blind, from the
source only.

**Source-summary page** (`sources/`): one per ingested section. Records what the section
covered, which book pages it spans, and **defines the citation label** for its source
via frontmatter (section 6). Queries do not target these; they are reached by link for
citation resolution.

**Index** (`index.md`): the catalog. Groups every concept, entity, and synthesis page
under **book topic areas** (Training fundamentals, Model compression, Retrieval,
Evaluation, Prompt engineering, People and tools). Topic areas come from the book's
structure, never from the eval categories.

**Log** (`log.md`): append-only, one line per operation, date-prefixed and parseable.

**Measurement note.** The wiki is built once, in full, with synthesis pages. The three
comparison conditions are a query-time split over that single build: RAG; wiki-atomic
(retrieval restricted to concepts and entities plus their links); wiki-plus-syntheses
(syntheses included). Building once keeps the build blind and the syntheses honest;
the split isolates what the synthesis layer is worth.

---

## 4. Page-creation rules (granularity and placement)

Apply these two rules in order. Sequencing them resolves the conflict between them.

**Entity bar (apply first).** A thing earns its own entity page when the ingested
section gives it a definition and at least one distinct attribute or figure of its own.
Judge on the section's material only, never on whether an eval question needs it. Things
below the bar appear as inline mentions on the relevant concept page.

Chosen calibration: the **mechanical** bar above, which is what an agent can apply from
the section in front of it. It does proliferate pages (e.g. both Alpaca and Nemotron-4
earn pages, not just DistilBERT). That is accepted: storage is a non-issue, and the cost
that does scale (index length) is a routing concern for the daily-use fork, not this
build.

**Fact-placement (apply second).** An **entity-specific** figure lives on that entity's
page. A **concept-general** figure lives on the concept page. Because the entity bar ran
first: if the entity earned a page, its figures go there; if it did not, the figure
rides inline in its mention. ("Entity-specific," not "model-specific" — a model is just
one kind of entity; the rule holds for people, tools, and datasets too.)

Example: "DistilBERT is 40% smaller" is entity-specific → the DistilBERT page. "Distilled
models are typically 40-60% smaller" would be concept-general → the distillation page.

---

## 5. Page template

Every concept, entity, and synthesis page follows this structure.

```markdown
---
type: concept | entity | synthesis
sources: [<source-page-slug>, ...]
---
# <Page title>

<Definition or description, kept as tight as the concept allows. One main idea per page:
if it grows past two or three short paragraphs, that is a signal to split the page or
push detail onto a linked page, not to write more here. Include only what would change
an answer; cut padding. The book's own academic references (e.g. "(Sanh et al., 2019)")
stay inline where they occur — they are the source's scholarship. The provenance citation
(LABEL p.NNN) closes the claim-cluster: cite once at the end of a run of claims drawn
from one page, not after every sentence.>

## Key figures
<Load-bearing numbers preserved verbatim, each with a page cite. A figure is
load-bearing if the number itself carries the claim — softening it to a vague word
("much smaller", "far faster") would destroy real information. Preserve those exactly.
Illustrative numbers that gloss without loss need not appear here. Place figures per the
fact-placement rule (section 4). If the page has no load-bearing figures of its own,
write "None" — an empty slot is that rule working, not a gap.>

- <e.g. 40% smaller than BERT, retains 97% of language comprehension, 60% faster (AIE p.395)>

## Examples
<Instances of the concept, as brief links or one-liners — NOT prose paragraphs. Full
detail lives on the linked entity page. Omit this section on entity and synthesis pages.>

- [[distilbert]]  (student trained from scratch; canonical case)

## Related
<Links to other pages. Each reason begins with one or more relationship keywords from the
closed set (below), followed by ": " and a brief gloss; put direction in the gloss. A
link may carry more than one keyword when the relationship is genuinely compound. This
section carries comparison and synthesis questions, so it must be substantive. Missing
connective tissue is the main way this wiki fails a synthesis question.>

- [[quantization]]  (contrast: other main model-compression method; lowers numerical precision vs. trains a small student)
- [[data-synthesis]]  (part-of: distillation is one use of synthetic data; boundary: not all synthetic-data training is distillation)

## Provenance
<Which source-summary page(s) this content was drawn from.>

- [[sources/ch08-model-distillation]]
```

`Key figures` and `Related` are the two load-bearing sections. The measurement lives or
dies on them.

### Related keyword set (closed)

The one place the relationship vocabulary is defined. Ingest picks from it; lint checks
against it.

- **contrast** — A and B are alternatives or differ in approach.
- **part-of** — A is a component or subset of B (composition or subsumption).
- **example-of** — A is a concrete instance of concept B (instantiation).
- **prerequisite** — A requires or builds on B; understanding or using A needs B.
- **boundary** — marks where A and B diverge, or where the relationship stops (a caveat).
- **see-also** — generic relatedness; last resort when none of the above fits.

Design rule for the set: keywords must be **disjoint** — each names a distinct KIND of
relationship, so there is never a choice between two that both fit. The set's value is
consistency, and consistency comes from disjointness, not from size. Do NOT add
near-synonyms (e.g. "differs-from" for contrast) or inverses (e.g. "enables," the inverse
of prerequisite — put direction in the gloss instead): they reintroduce the drift the
closed set exists to prevent. Add a keyword only for a genuinely new KIND the corpus
actually exhibits (warrant), and only by a human editing this list. First warrant
candidate if it recurs: **evaluates** (A measures or evaluates B).

---

## 6. Citation format

- Provenance citations take the form `(LABEL p.NNN)`, where **NNN is the printed book
  page** (not the PDF page).
- **LABEL is defined on a `sources/` page, not invented ad hoc.** Each source page
  declares its label in frontmatter. A citation is a two-hop pointer: `(AIE p.395)` names
  the source, the source page resolves `AIE` to the book and edition, the page number
  indexes into it. The schema fixes the *format*; the sources layer holds the *list* of
  labels. Adding a source later means a new `sources/` page, not a schema edit.
- The book's **own academic references** (e.g. "(Sanh et al., 2019)") are kept inline and
  are distinct from provenance: they are the source citing its sources, not the wiki's
  audit trail. Only `(LABEL p.NNN)` is lint-validated.
- A wiki page is **never** evidence for itself or another wiki page.

Source-page frontmatter (identity block):

```markdown
---
type: source
label: AIE
title: AI Engineering
author: Chip Huyen
publisher: O'Reilly
year: 2024
pages: printed book pages
---
# AIE — AI Engineering (Chip Huyen, O'Reilly, 2024)

Immutable source. Citation label **AIE**. Cite as (AIE p.NNN) using printed book pages.
Covered by this ingest: <chapter / section, book pp.NNN–NNN>.
```

---

## 7. Index format

`index.md` groups pages by book topic area. Each entry is a link plus a one-line summary.

```markdown
## Model compression
- [[quantization]] — reduces numerical precision to cut memory and speed up compute
- [[distillation]] — trains a small student to mimic a larger teacher

## People and tools
- [[chip-huyen]] — author; ML systems writer and engineer
```

The index is the query entry point and, at ingest, the agent's map of what pages already
exist so it can link to them. It must stay in sync with the pages on disk; lint checks
this.

---

## 8. Log format

Append-only. One line per operation. Never edited or reordered.

```
2026-09-06 ingest   ch08-model-distillation  -> +concepts/model-distillation +entities/distilbert +entities/alpaca +sources/ch08-model-distillation
2026-09-06 query    "What is model distillation?"  -> concepts/model-distillation  [answered]
2026-09-06 lint     -> 0 broken links, 1 orphan (entities/nemotron-4), 0 missing back-links
```

---

## 9. Ingest workflow

Input is one section file from `raw/`. Never the whole book at once; sectioned ingest is
what makes extraction clean and facts survive.

1. Read the section. Read the current `index.md` so you can see every page that already
   exists and link to it.
2. Identify the concepts and entities it introduces or extends. Apply the entity bar
   (section 4) to decide what gets a page vs. a mention.
3. Before creating any page, check the index for a near-match to avoid duplicates.
4. Create or update each page per the template. Preserve load-bearing figures verbatim,
   placed per the fact-placement rule. Close each claim-cluster with `(LABEL p.NNN)`.
5. If the section itself draws a cross-cutting comparison, create a `syntheses/` page for
   it — blind, from the source, never targeting an eval question.
6. Add `Related` links to existing pages, and back-links on those pages. Begin each reason
   with a keyword from the closed set (section 5). If none fits, use the closest existing
   keyword and append a line to `wiki/_review.md` noting the no-fit; do NOT coin a new
   keyword (the set is extended only by a human editing section 5). To let the agent also
   propose a candidate keyword in that flag, add "and suggest a candidate" here — it still
   may not use the candidate until a human adds it to the set.
7. Write or update the section's `sources/` page (with its label frontmatter).
8. Update `index.md`. Append one line to `log.md`.

**Linking pass (after all sections are ingested).** Walk the finished wiki once and, for
each page, add the `Related` links it should carry now that every target exists. Cross-
linking is a global operation that is only tractable once the graph is complete; do not
rely on incremental ingest to have found every link against a half-built graph.

The agent is never shown the evaluation questions during ingest.

---

## 10. Query protocol

1. Read `index.md`. Route to the relevant page(s).
2. For a comparison or synthesis question, pull each page the question touches and follow
   `Related` reasons to connecting pages (and to a `syntheses/` page if one exists and
   the active condition includes it).
3. Answer from the retrieved pages only, carrying `(LABEL p.NNN)` citations through.
4. If no page covers the question, **decline**: state the topic is not in the wiki. Do
   not fabricate. (Correct behaviour for out-of-corpus questions.)
5. Append the query to `log.md`.
6. **Do not create or modify any page.** No write-back. The wiki is frozen.

The query path is deliberately shaped like the RAG baseline's: locate pages, pull them,
synthesise an answer. The only intended difference between the systems is what is indexed
(synthesised wiki pages vs. raw chunks), not how cleverly retrieval works.

---

## 11. Lint (minimal)

The corpus is frozen, so lint is a build-correctness check, not a contradiction engine.
It checks only:

- Broken `[[wikilinks]]` (target page missing).
- Orphan pages (in `wiki/` but absent from `index.md`, or with no inbound links).
- Index-vs-disk drift (index lists a missing page, or omits an existing one).
- Bare `Related` links (a link with no reason).
- Related reasons whose leading keyword is not in the closed set (section 5).
- Unresolved citation labels (a `(LABEL p.N)` whose LABEL is not declared on any
  `sources/` page).
- Probable duplicate pages (near-identical titles or content — the cost of the mechanical
  entity bar).
- Pages with numeric claims in prose but an empty `Key figures` section (possible
  load-bearing figure lost to paraphrase).

Lint fixes what it safely can and reports the rest. It does not rewrite page content.

---

## 12. Integrity guards (do not relax)

1. Build blind to the 20 evaluation questions (section 1).
2. Do not edit the evaluation set to suit the wiki. Verify its balance; leave it as is.
3. Provenance on every claim, pointing into the immutable book by printed page.
4. Freeze the wiki before scoring. Write-back stays off for the core comparison.

---

## Portability

Nothing above is tied to a particular model or tool. Switching the agent from Claude to
GPT (or anything else) changes which API your ingest/query scripts call, not a word of
this schema — your scripts load this file by path and pass it in the prompt regardless.

The filename is the only tool-coupled thing, and only for interactive coding agents that
auto-discover instructions. Claude Code auto-loads `CLAUDE.md`; the cross-tool standard
`AGENTS.md` is read by most other agents. Since your pipeline reads this file explicitly
rather than relying on auto-discovery, the name is free. It is called `SCHEMA.md` because
that is what it is. If you later want a coding agent to auto-load it during development,
add a thin `CLAUDE.md` or `AGENTS.md` whose first line imports `@SCHEMA.md`, and keep
this file as the single source of truth.
