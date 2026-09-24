---
type: synthesis
sources: [ch07-finetuning-and-rag]
---
# Finetuning versus RAG

The book frames the choice between [[rag]] and [[finetuning]] as depending on whether a model's failures are information-based or behavior-based. Information-based failures happen when outputs are factually wrong or outdated, either because the model lacks the information (e.g. private data) or because its knowledge is stale (AIE p.316). Behavior-based failures happen when outputs are factually fine but irrelevant, malformatted, or otherwise stylistically wrong -- for example generating HTML that doesn't compile, or technical specs that miss needed detail (AIE p.317).

The book's summary rule: **finetuning is for form, and RAG is for facts.** RAG supplies external knowledge to make answers more accurate and mitigates hallucination; finetuning teaches a model to follow syntaxes and styles, and can reduce or worsen hallucination depending on training-data quality (AIE p.317). [[semantic-parsing]] tasks, which hinge on producing output in an expected structured format, often require finetuning because strong off-the-shelf models are weaker on less common syntaxes (AIE p.317).

Ovadia et al. (2024) found RAG outperforms finetuning even on tasks that seem like knowledge tasks: for almost all MMLU question categories, RAG beat finetuning across three models (Mistral 7B, Llama 2-7B, Orca 2-7B), and RAG with the unfinetuned base model outperformed RAG with finetuned models -- meaning finetuning for a specific task can degrade performance elsewhere (AIE p.316-317). RAG and finetuning are not mutually exclusive: combining RAG with a finetuned model boosted MMLU performance 43% of the time, though 57% of the time it did not improve over RAG alone (AIE p.318).

When a model has both information and behavior issues, the book recommends starting with RAG, since RAG avoids the cost of curating training data or hosting finetuned models, and starting simple with term-based retrieval like [[bm25]] rather than jumping to embedding-based methods (AIE p.317-318). See [[model-adaptation-workflow]] for the book's step-by-step process combining prompting, retrieval, and finetuning over time.

## Related

- [[rag]]  (contrast: facts-oriented adaptation vs. finetuning's form-oriented adaptation)
- [[finetuning]]  (contrast: form-oriented adaptation vs. RAG's facts-oriented adaptation)
- [[ovadia-et-al-finetuning-vs-retrieval-study]]  (see-also: empirical study underlying this comparison)
- [[model-adaptation-workflow]]  (part-of: this comparison feeds directly into the book's staged adaptation workflow)
- [[mmlu]]  (example-of: benchmark used by Ovadia et al. to compare RAG and finetuning)
- [[bm25]]  (example-of: recommended starting point when beginning with RAG)
- [[hallucination]]  (see-also: RAG mitigates it via grounding; finetuning can worsen or reduce it depending on data quality)

## Provenance

- [[sources/ch07-finetuning-and-rag]]
