---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Masked Language Model

A masked language model is trained to predict missing tokens anywhere in a sequence, using context from both before and after the missing tokens -- in essence, trained to fill in the blank (AIE p.4). For example, given 'My favorite __ is blue', a masked language model should predict 'color' (AIE p.4). [[bert]] (bidirectional encoder representations from transformers) is a well-known example (Devlin et al., 2018) (AIE p.4).

As of writing, masked language models are commonly used for non-generative tasks such as sentiment analysis and text classification, and for tasks needing understanding of context on both sides, such as code debugging (AIE p.4).

## Key figures
None.

## Examples
- [[bert]]  (canonical masked language model)

## Related
- [[autoregressive-language-model]]  (contrast: uses bidirectional context to fill in blanks vs. only preceding context to predict the next token)
- [[language-model]]  (part-of: one of the two main language-model types)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
