---
type: concept
sources: [ch02-sampling-strategies]
---
# Top-k Sampling

Top-k is a sampling strategy that reduces computation without sacrificing too much of a model's response diversity. Softmax normally requires two passes over all possible values in the [[vocabulary]]: one for the exponential sum and one to divide each value by that sum, which is expensive for a large vocabulary. Top-k sampling instead picks the k highest logits after they are computed, and performs softmax only over those top-k logits, then samples from the resulting values (AIE p.93-94).

A smaller k value makes text more predictable but less interesting, since the model is limited to a smaller set of likely words (AIE p.94).

## Key figures
- Depending on desired diversity, k can range from 50 to 500, much smaller than a model's vocabulary size (AIE p.94)

## Related
- [[sampling]]  (part-of: one strategy for selecting the next token from a computed distribution)
- [[softmax]]  (prerequisite: top-k restricts softmax's computation to the k highest logits)
- [[top-p-sampling]]  (contrast: fixed candidate count vs. dynamic cumulative-probability cutoff)
- [[temperature]]  (contrast: reshapes the whole probability distribution rather than restricting the candidate set)

## Provenance
- [[sources/ch02-sampling-strategies]]
