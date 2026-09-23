---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Masked Language Model

A masked language model is trained to predict missing tokens anywhere in a sequence,
using context from both before and after the missing tokens -- in essence, trained to
fill in the blank (AIE p.4). A well-known example is BERT, bidirectional encoder
representations from transformers (Devlin et al., 2018) (AIE p.4). Masked language
models are commonly used for non-generative tasks such as sentiment analysis and text
classification, and for tasks needing understanding of context on both sides, such as
code debugging (AIE p.4).

## Key figures
None.

## Related
- [[autoregressive-language-model]]  (contrast: uses context from both directions vs. only preceding tokens; used for classification-style tasks vs. generation)
- [[language-model]]  (part-of: one of the two main types of language model)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
