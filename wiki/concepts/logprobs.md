---
type: concept
sources: [ch02-sampling-strategies]
---
# Logprobs

Logprobs, short for log probabilities, are the probabilities a model computes for tokens expressed on a log scale (AIE p.92). Log scale is preferred when working with a neural network's probabilities because it helps reduce the underflow problem: with a large vocabulary, many token probabilities are too small to be represented by a machine and get rounded down to zero, and log scale mitigates this (AIE p.92). Logprobs are useful for building applications (especially classification), evaluating applications, and understanding how models work under the hood, but many model providers don't expose them, or expose only a limited API, likely for security reasons since exposed logprobs make a model easier to replicate (AIE p.93).

## Key figures
- A language model may have a vocabulary size of 100,000, making many token probabilities too small to represent without underflowing to zero (AIE p.92)
- OpenAI's API exposes logprobs for only the top 20 most likely tokens (AIE p.93)

## Related
- [[logits]]  (contrast: logprobs are log-scaled probabilities, derived after softmax, not raw model outputs)
- [[sampling]]  (part-of: logprobs support building, evaluating, and debugging sampling-based applications)

## Provenance
- [[sources/ch02-sampling-strategies]]
