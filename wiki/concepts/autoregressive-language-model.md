---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Autoregressive Language Model

An autoregressive language model (sometimes called a causal language model) is trained to predict the next token in a sequence using only the preceding tokens (AIE p.4). It can continually generate one token after another, which makes it the model of choice for text generation today, and consequently far more popular than masked language models (AIE p.4-5). Unless stated otherwise, the book uses 'language model' to mean an autoregressive model (AIE p.5).

## Key figures
None.

## Examples
- [[gpt-4]]  (autoregressive model behind ChatGPT)

## Related
- [[masked-language-model]]  (contrast: predicts only the next token from preceding context vs. filling in blanks from both directions)
- [[language-model]]  (part-of: the default sense of 'language model' in the book)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
