---
type: concept
sources: [ch02-sampling-strategies]
---
# Logits

Logits are the raw, unnormalized scores a language model produces over its vocabulary for a given input, one per possible token (AIE p.90). Larger logits correspond to higher probabilities, but logits are not themselves probabilities: they don't sum to one and can be negative (AIE p.90). A softmax layer converts a logit vector into a probability distribution, computing the probability of the ith token as the exponential of its logit divided by the sum of exponentials of all logits (AIE p.90). [[temperature]] adjusts logits (by division) before this softmax step, and [[top-k-sampling]] restricts softmax to a subset of the highest logits to cut computation (AIE p.93).

## Key figures
None.

## Related
- [[softmax]]  (prerequisite: logits must pass through softmax to become probabilities)
- [[temperature]]  (prerequisite: temperature is applied by adjusting logits before softmax)
- [[top-k-sampling]]  (prerequisite: top-k selects among logits before applying softmax)
- [[logprobs]]  (contrast: logprobs are probabilities in log scale, derived after softmax, not raw logits)

## Provenance
- [[sources/ch02-sampling-strategies]]
