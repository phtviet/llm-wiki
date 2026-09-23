---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Dataset Engineering

Dataset engineering refers to curating, generating, and annotating the data needed for training and adapting AI models; it is one of the three main responsibilities of [[model-development]] (AIE p.42). Traditional ML engineering deals mostly with close-ended tasks (e.g., spam vs. not spam) and tabular data, whereas foundation models are open-ended, making annotation much harder — it's easier to judge whether an email is spam than to judge a written essay (AIE p.42).

In AI engineering, data work shifts from feature engineering toward deduplication, tokenization, context retrieval, and quality control, including removing sensitive or toxic data (AIE p.42-43). Some argue that since models are now commodities, data becomes the main differentiator, making dataset engineering more important than ever. Data requirements scale with the adaptation technique: training from scratch needs more data than finetuning, which needs more than prompt engineering (AIE p.42). Expertise in a model's training data also helps diagnose its strengths and weaknesses (AIE p.42).

## Key figures
None.

## Related
- [[model-development]]  (part-of: one of model development's three main responsibilities)
- [[model-adaptation]]  (see-also: data requirements scale with which adaptation technique is used)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
