---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Autoregressive Language Model

An autoregressive language model is trained to predict the next token in a sequence
using only the preceding tokens, and can continually generate one token after another
(AIE p.4). Autoregressive models are sometimes called causal language models. They are
today's models of choice for text generation and are much more popular than masked
language models for that purpose (AIE p.4-5). Unless stated otherwise, the book uses
"language model" to mean an autoregressive model (AIE p.5).

## Key figures
None.

## Related
- [[masked-language-model]]  (contrast: predicts only the next token from preceding context vs. filling in blanks from both directions)
- [[language-model]]  (part-of: one of the two main types of language model; the book's default sense)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
