# LLM Wiki vs RAG: a measured comparison on one book

## Summary

I built an LLM wiki of Chip Huyen's *AI Engineering* (418 interlinked pages) and measured it against a RAG system I had previously built over the same book ([rag-book](https://github.com/phtviet/rag-book)): same corpus, same 20 questions, same judge.

- **The wiki won every run.** 17 to 20 correct out of 20 across 7 runs, against RAG's 16, on roughly the same amount of context when not following links.
- **Its main retrieval failure was the lossy index:** a fact the wiki held but couldn't find. I diagnosed it to three layers and fixed it with BM25 over page bodies. The final system scored 19 and 20, with no wrong answers.
- **Link traversal added nothing measurable.** The mechanism behind "knowledge compounds" gained one question once, and it didn't replicate.
- **Caveat: different answer models** (Sonnet 5 for the wiki, Sonnet 4.5 for RAG). Several wins trace to retrieval rather than to how answers were written, but the comparison doesn't fully separate the two.

## Why measure this

The claim that a wiki beats RAG because knowledge compounds is everywhere in the discussion around this pattern. It is almost never measured, because measuring it needs a RAG baseline and an evaluation set built on the same corpus. I already had both from the earlier RAG project, so the comparison could be run with only one thing changing: what gets retrieved.

Having a working baseline also made several sharper questions answerable:

1. **Does the wiki beat RAG at all?** A high score on its own could simply mean an easy evaluation set. (Results, Finding 1)
2. **Where does each approach win?** A per-question comparison shows which kinds of question favour pre-synthesised pages, and which still favour raw text. (Finding 1, Limitations)
3. **Is any advantage just more context?** This is only answerable by measuring how much text RAG actually reads per question. (How it was measured, Results)
4. **Does link traversal, the pattern's core mechanism, matter?** (Finding 3)
5. **Is a given difference a retrieval effect or an answer-model effect?** RAG's retrieval is deterministic and logged, so the passages it saw can be checked directly. (Finding 1)
6. **Can the scoring be trusted?** Earlier RAG runs made it possible to validate the scorer against historical results. (How it was measured)

## The two systems

**RAG (the baseline).** The book's text is chunked, embedded with bge-small, retrieved by vector similarity (top 20), reranked by a cross-encoder down to 3 chunks, and answered with a faithfulness prompt. Everything is synthesised at query time, from raw text.

**Wiki (this project).** This follows Andrej Karpathy's LLM-wiki pattern: an LLM compiles source material once into persistent, interlinked pages, and questions are answered from those pages rather than from the raw text. Here, an ingest agent reads the book one section at a time and writes concept, entity and synthesis pages, each with a definition, preserved key figures, typed links to related pages and page-level citations. At query time an LLM router reads the wiki's index, picks up to N pages, and an answer model responds from those pages with `(AIE p.NNN)` citations. Optional extras: following each page's Related links one hop, and adding BM25 keyword retrieval over page bodies.

The essential difference is *when* the synthesis happens. RAG retrieves raw passages and reasons over them on every query. The wiki retrieves the output of reasoning that was done once, at ingest.

## Building the wiki

**Corpus parity.** The wiki was built from exactly the text RAG indexed: I reused the RAG system's extraction script, so the page span, exclusions (front matter, back cover, the book's alphabetical index) and cleaning are identical. I then cut that text at the book's own subsection headings, read from the PDF's outline, giving 166 source sections. The unit of ingest is the smallest span in which a concept arrives whole, which in a well-structured book is the author's own subsection.

**The schema.** A single `SCHEMA.md` governs the agent. The rules that mattered most:

- **Entity bar and concept bar.** A thing earns its own page only when the section defines it in its own right. A concept that is merely named, in a list or a forward reference, stays a link. Without these, chapter 1 alone produced about 60 thin pages.
- **Fact placement and key figures.** Load-bearing numbers are preserved verbatim in a `Key figures` section on the page they belong to, so summarisation cannot soften "40% smaller" into "much smaller."
- **A closed set of link types** (contrast, part-of, example-of, prerequisite, boundary, see-also), so relationships are consistent and checkable.
- **Build-blind.** The ingest agent never saw the 20 evaluation questions. The evaluation set was added to this repository only after the wiki was frozen.
- **Frozen for measurement.** No write-back: answering a question never edits the wiki.

**Calibration before automation.** I hand-wrote three pages as gold exemplars, then diffed the agent's output against them. Schema-only output over-produced pages and misplaced examples; adding exemplars fixed placement but made the agent drop pages the rules required, because it imitated the exemplars' sparseness. The fix was to state in the prompt that exemplars govern style, while the bars alone decide which pages exist.

**Result.** 166 sections ingested with no failures, 418 page files plus 164 source pages, and a mechanical linking pass that added 279 links where a page's text named another page without linking it. After that pass, every page had at least two Related links.

## How it was measured

- **Same questions.** The 20-question evaluation set written for the RAG system, with a reference answer for each (see the caveat on how those were written, below): 8 factual, 2 specific detail, 2 comparison, 5 synthesis, and 3 out-of-corpus questions that should be declined. All 20 are listed in the appendix, with per-question results; reference answers are in `eval_set.py`.
- **Same judge, same environment.** Answers were scored by the RAG project's LLM judge (claude-sonnet-4-5, temperature 0), unmodified and run in that project's own environment, because the newer SDK used to generate wiki answers no longer accepts a temperature setting. How the judge works and how it was validated are described below.
- **Scorer validated.** Before scoring anything new, I re-scored an old RAG run and reproduced its historical result exactly (15 correct, 5 partial), twice.
- **RAG re-scored in the same session.** The RAG project originally reported 17/20. Re-scored alongside the wiki runs, the same RAG output scores **16 correct, 4 partial**, with one borderline answer (embeddings) now marked partial. All comparisons below use 16.
- **Context measured, not assumed.** Every answer records how many characters of wiki text the answer model read. RAG's equivalent is 3 retrieved chunks of about 2,051 characters each, roughly 6,150 characters per question.
- **Replication.** Routing is not deterministic, so the main conditions were each run twice.
- **Answer models differ (not controlled).** Wiki routing and answers used Claude Sonnet 5; the RAG answers used Claude Sonnet 4.5. The wiki was also built with Sonnet 5 at ingest, which is a legitimate part of the approach (synthesis done once, with the best model available) but is disclosed here.
- **One manual correction.** In two runs the judge rewarded the wiki for *declining* Q19, apparently treating it as an out-of-corpus question. Q19 has a factual answer in the book, so I scored those as wrong.

### How answers are scored

Each answer is scored by an LLM judge (claude-sonnet-4-5, temperature 0) that receives four things: the question, its category, the reference answer, and the system's answer. It is not told which system produced the answer. It returns one verdict and a one-sentence rationale:

- **Correct:** accurate, and conveys the core concept the question asks about. It may omit secondary detail, and it may include accurate information beyond the reference.
- **Partial:** accurate as far as it goes, but a core concept, defining property or required specific value is missing.
- **Wrong:** contains inaccuracies or fabrications, or misses the core concept entirely.

The bar depends on the question type. Specific-detail questions must contain the exact value asked for. Comparisons must state the key differences. Synthesis questions must state the *relationship* the reference describes, not merely discuss both topics; this is why the wiki's Q5 answers were often marked partial. Out-of-corpus questions are correct only if the system declines.

Two properties of the judge matter for reading the results. First, accurate content beyond the reference is never penalised, so a fuller answer can only help, up to the point of covering the core concepts. Second, it checks facts against the reference, not whether citations point to the right page, which is why a misattributed citation (see Limitations) can still score correct.

**Validation.** The judge was validated against my own hand scores when the RAG system was built. On that independent check it agreed on **15 of 20** questions, and all five disagreements were the judge being stricter than me. On two of them (Q5 and Q8) the judge was right: I had accepted answers that missed a core point, so I revised my scores. After a prompt refinement it matched the revised scores on all 20, but that figure isn't independent, so 15/20 is the honest number. At temperature 0, repeated runs of the judge on the same file gave identical verdicts.

That validation used RAG answers and was not repeated on wiki answers, which are longer and structured differently. The judge's one observed error in this project came on a wiki answer: it twice treated Q19 as out-of-corpus and rewarded a decline (see above). During validation it also once credited an answer with a formula that appeared only in the reference; that did not recur at temperature 0, but it is a known failure mode. Because that earlier case was Q20, I checked the wiki's Q20 answers directly: both final runs state the equation H(P, Q) = H(P) + D_KL(P || Q), so those verdicts are genuine.

**Reference answers.** These were written while building the RAG system, largely drafted from its own outputs and only partly checked against the book, so the judge partly enforces those drafting choices. If that introduces a bias, it most likely favours RAG, whose answers the references were drafted from.

## Results

| System | Context vs RAG | Run 1 | Run 2 |
|---|---|---|---|
| RAG baseline (re-scored) | 1.0x | 16 / 4 / 0 | |
| Wiki, 3 pages, no hop | 0.7x | 17 / 1 / 2 | |
| Wiki, 6 pages, no hop | 1.1x | 18 / 1 / 1 | 19 / 1 / 0 |
| Wiki, 6 pages, 1-hop links | 2.6x | 19 / 0 / 1 | 19 / 1 / 0 |
| **Wiki, 6 pages, BM25 union (final)** | **1.7x** | **19 / 1 / 0** | **20 / 0 / 0** |

*Correct / partial / wrong, out of 20. Context is average characters read per question across all 20 questions, relative to RAG's ~6,150. Wiki averages include out-of-corpus questions where it read nothing, so they understate the wiki's context on answerable questions by about 15%.*

## Finding 1: The wiki answered more questions correctly than RAG, at comparable context

On every run, the wiki produced more fully correct answers than RAG. The fairest head-to-head on context is 6 pages without link-following: about the same amount of text as RAG, and 18 to 19 correct against 16.

The two systems also used different answer models, so how much of that margin is architecture is not settled. What can be said is that several of the wiki's wins are traceable to *retrieval*, which the answer model can't affect:

- **Q20 (entropy and cross-entropy):** RAG lost it for omitting the equation. The equation is on book p.121. RAG's three retrieved chunks were pp.119, 120 and 122, so it never saw the page. The wiki's cross-entropy page contains the equation.
- **Q9 (inference-optimization techniques):** the techniques are spread across the chapter. Three chunks can't cover them; a page that gathers them can.
- **Q19 (a specific figure):** the wiki's failures here were routing failures, independent of the answer model (Finding 2).

Where the model could plausibly matter is in completeness: the judge rewards answers that cover all the reference's points, and a newer model may simply write fuller answers from the same material. Separating the two needs a re-run with matched models.

Before scoring the wiki, I wrote down predictions for RAG's four partial answers. Most held:

| Question | RAG's gap | Prediction | Outcome |
|---|---|---|---|
| Q1 quantization | missed the speed-up and the PTQ/QAT approaches | correct | correct in every wiki run |
| Q9 inference-optimization techniques | techniques scattered across pages it didn't retrieve | correct with more pages | correct at 6 pages, partial at 3 |
| Q20 entropy and cross-entropy | missing the equation | correct | correct in every wiki run |
| Q8 embeddings | missing "similar items have nearby vectors" | uncertain | correct in every wiki run |

These are the questions where a curated page that gathers one concept's material in one place beats three passages that each hold part of it. I also predicted the wiki's main risk would be a specific-detail question whose figure got summarised away. That risk materialised, though not for the reason I expected.

## Finding 2: The wiki's main failure was a lossy index, and BM25 over page bodies fixed it

Q19 asks how many of the top 1,000 AI-related GitHub repositories were dedicated to evaluation. The answer, "over 50," was in the wiki the whole time: preserved verbatim in the `Key figures` section of `challenges-of-evaluating-foundation-models`, with the correct page citation. Ingest did its job. Yet without BM25 the wiki answered correctly in only 2 of 5 runs.

Three safety nets failed in sequence:

1. **The index summary didn't advertise the fact.** The router decides from one line per page, and this page's line describes intelligence, open-endedness and benchmark saturation, with nothing a question about repositories would match.
2. **The router confidently opened one page.** It usually uses most of its budget, but on Q19 it often opened only the general `evaluation` page, sure that was enough.
3. **The link graph had no path.** `evaluation` does not link to the page on why evaluation is hard, so link-following could not recover it either.

This is the first failure mode practitioners report for this pattern: past roughly 100 to 200 pages, one-line summaries can no longer advertise everything in the page bodies.

**The fix:** BM25 keyword search over page bodies, combined with the router's picks by simple union. BM25 doesn't depend on the summary, the router's confidence or the link graph. It ranked the right page second (behind a chapter 1 page that also discusses GitHub repositories), inside the top 3 that I had fixed before looking.

With BM25, Q19 was correct in both runs. The attribution here rests on mechanism, not just score: **in both runs the router repeated its original mistake**, opening only `evaluation`, and BM25 supplied the missing page each time.

## Finding 3: Link traversal added no measurable benefit, and the lossy index appeared even at single-book scale

**Link traversal did not improve accuracy.** Following each page's Related links, the pattern's headline mechanism, cost about 2.4 times the context of the no-hop condition. In the first round it gained exactly one question, Q5. In the replication, Q5 went back to partial and the hop and no-hop conditions scored identically. The gain was noise.

The likely reasons are specific to a single-book wiki: the router already sees every page summary and opens the relevant neighbours directly, and the hop follows links in order rather than by relevance, so it adds noise as often as signal. Traversal may matter more in a multi-source wiki, where the index gets lossier and questions span sources, but that is untested here.

**The lossy index appeared at single-book scale.** Early in planning I assumed a single book would produce 30 to 60 pages, well under the threshold where index-based routing degrades. The wiki reached 418, and the failure appeared as described.

## Limitations

- **Different answer models.** Sonnet 5 for the wiki, Sonnet 4.5 for RAG. This is the largest open question about the headline result, discussed under Finding 1.
- **Q5 is the one question RAG answers more reliably.** It asks how the evaluation and inference-optimization chapters relate. The reference expects the link "optimization can degrade quality, so you must evaluate." The wiki had the supporting fact in context ("many optimization techniques can cause model degradation," AIE p.426) and still made the connection in only 2 of 7 runs. This is not a retrieval failure: neither corpus states the relationship outright, and the wiki's answer model made the inference inconsistently.
- **The wiki can misattribute citations.** In Q3, the answer attributed a relationship between distillation and quantization to AIE p.395. I checked the book: that page doesn't mention quantization. The claim came from a link description written during ingest, which the answer model couldn't distinguish from sourced text. The judge scores correctness, not citation accuracy, so this didn't affect scores. RAG can't make this error, because its citations come directly from the passage it retrieved. Measuring how often it happens is future work.
- **Reference answers partly drafted from RAG output** and only partly checked against the book (see How answers are scored). Any resulting bias most likely favours RAG.
- **Small sample.** 20 questions, two runs per main condition. Differences of one question are within run-to-run variation; the margin over RAG is the robust result, not any single score.
- **No temperature control** on the wiki side, so routing and answers vary between runs. The judge itself was stable at temperature 0.
- **One judge error corrected by hand** (Q19 in two runs), described above.

## Engineering notes

Several bugs were more instructive than the features:

- **A silent version mismatch.** For several sessions I was running an old segmentation script that cut on page breaks instead of headings, which pushed the cross-entropy equation into the wrong file. The giveaway was a difference in the generated header format. The whole wiki was rebuilt from the corrected corpus, and scripts now print a version banner on every run.
- **A slug collision.** The book has a chapter and a section both called "Inference Optimization," so one file overwrote the other and the chapter introduction disappeared. Colliding names now get a suffix.
- **Shadowed pages.** The wiki has 418 page files, but the query and lint scripts index pages by name and loaded 415: three names exist in two folders at once (`common-crawl`, `human-in-the-loop` and `model-gateway`), so one of each pair is unreachable. Small enough not to move the results, but the loaders should key on folder and name.
- **A silent empty input.** A path bug meant one full ingest ran with no exemplars at all, without any error. Missing exemplars now stop the run.
- **Measuring beat assuming.** RAG's chunk size was configured as a 1,024-token maximum, so I assumed RAG read about 12,000 characters per question. Measured, each chunk is a single book page of about 2,051 characters, half what I'd assumed. That roughly doubled every context ratio I had been quoting.
- **A new retriever exposed an old bug.** Before BM25, out-of-corpus questions never reached the answer model. With BM25 adding pages, "how do I make bombs?" did, the model refused, and the refusal came back with no text, which the harness recorded as a blank answer. Refusals are now recorded as declines.
- **Judge parity across SDK versions.** The newer SDK dropped the temperature parameter. Rather than modify the judge, I scored every run in the RAG project's environment, so both systems were judged by identical code.

## What's next

- **Re-run with matched answer models,** the one change that would make the headline comparison fully controlled.
- **Relationship linking.** An LLM pass over the whole wiki to add links that aren't stated in any page's text, run blind to the questions. Q5 gives it a measured motivation.
- **A systematic citation audit,** turning the Q3 observation into a rate: what share of the wiki's citations actually support their claims.
- **An agentic query loop** that can look at what it retrieved and decide to search further, compared against the fixed pipeline here.
- **A multi-source wiki,** the setting where link traversal and cross-source synthesis should matter most, and where this comparison can be repeated with the hop fixed to rank links by relevance.

## Appendix: the 20 evaluation questions

Questions are reproduced verbatim from the evaluation set. Results compare the RAG baseline (re-scored) with the final wiki configuration (6 pages, BM25 union, no link-following) across its two runs. The three out-of-corpus questions are scored correct when the system declines.

| # | Question | Category | RAG | Wiki run 1 | Wiki run 2 |
|---|---|---|---|---|---|
| 1 | What is quantization? | factual | partial | correct | correct |
| 2 | What percentage smaller is DistilBERT than BERT? | specific detail | correct | correct | correct |
| 3 | What is model distillation? | factual | correct | correct | correct |
| 4 | What's the difference between quantization and distillation? | comparison | correct | correct | correct |
| 5 | How do the chapters on evaluation and inference optimization relate? | synthesis | correct | partial | correct |
| 6 | What does the book say about quantum computing? | out of corpus | correct | correct | correct |
| 7 | What is RAG? | factual | correct | correct | correct |
| 8 | What are embeddings? | factual | partial | correct | correct |
| 9 | What are the main techniques for inference optimization? | synthesis | partial | correct | correct |
| 10 | Who is Chip Huyen? | factual | correct | correct | correct |
| 11 | What is backward propagation? | factual | correct | correct | correct |
| 12 | What is Viet's favourite colour? | out of corpus | correct | correct | correct |
| 13 | What are the best practices of prompt engineering? | factual | correct | correct | correct |
| 14 | What are the malicious attacks that can be done with prompt engineering? | factual | correct | correct | correct |
| 15 | What is the future of comparative evaluation? | synthesis | correct | correct | correct |
| 16 | When should we finetune a model? | synthesis | correct | correct | correct |
| 17 | How do I make bombs? | out of corpus | correct | correct | correct |
| 18 | What is the difference between data-centric AI and model-centric AI? | comparison | correct | correct | correct |
| 19 | As of May 2024, how many repositories are dedicated to evaluation, from the author's own analysis of the top 1000 AI-related repositories on Github? | specific detail | correct | correct | correct |
| 20 | How does entropy and cross-entropy relate? | synthesis | partial | correct | correct |

*Totals: RAG 16 correct, 4 partial; wiki 19 correct, 1 partial (run 1) and 20 correct (run 2).*
