---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Dataset Engineering

Dataset engineering is the curation, generation, and annotation of the data needed for training and adapting AI models (AIE p.42). It is one of the three main responsibilities of [[model-development]], alongside modeling/training and inference optimization.

Traditional ML engineering deals mostly with close-ended tasks (a model's output is one of a predefined set of values, e.g. spam classification) and tabular data. Foundation models are open-ended, so annotation is much harder — judging whether an email is spam is far easier than judging the quality of a written essay (AIE p.42). Foundation models also work with unstructured data, shifting the work from feature engineering toward deduplication, [[tokenization]], context retrieval, and quality control (including removing sensitive or toxic data) (AIE p.42-43).

How much data is needed depends on the adaptation technique: training from scratch generally needs more data than finetuning, which needs more data than [[prompt-engineering]] (AIE p.43). Because models are increasingly commodities, some argue data is now the main differentiator, making dataset engineering more important than ever; a model's training data also gives clues to its strengths and weaknesses (AIE p.43).

## Key figures
None.

## Related
- [[model-development]]  (part-of: one of the three main responsibilities of model development)
- [[model-adaptation]]  (see-also: the amount of data needed for dataset engineering scales with the adaptation technique chosen)
- [[inference-optimization]]  (see-also: sibling responsibility within model development)
- [[prompt-engineering]]  (see-also: mentioned in this page's text)
- [[tokenization]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
