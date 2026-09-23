---
type: concept
sources: [ch02-sampling-strategies]
---
# Softmax

Softmax is the function that converts a model's [[logits]] into a probability distribution over the vocabulary: the probability of the ith token is the exponential of its logit divided by the sum of exponentials of all logits (AIE p.90). Computing softmax over a large vocabulary requires two full passes over all values — one to sum the exponentials, one to divide each exponential by that sum — making it computationally expensive for language models with large vocabularies (AIE p.93). This cost motivates strategies like [[top-k-sampling]], which restrict softmax to a smaller candidate set (AIE p.93).

## Key figures
None.

## Related
- [[logits]]  (prerequisite: softmax operates on logits to produce probabilities)
- [[temperature]]  (part-of: temperature adjusts logits before softmax is applied to them)
- [[top-k-sampling]]  (boundary: top-k limits softmax's computation to the top-k logits rather than the full vocabulary)

## Provenance
- [[sources/ch02-sampling-strategies]]
