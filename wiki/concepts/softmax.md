---
type: concept
sources: [ch02-sampling-fundamentals]
---
# Softmax

Softmax is the function commonly used to convert a [[logit-vector]] into a probability distribution. For a vocabulary of size N with logits x1, x2, ..., xN, the probability of the ith token is pi = e^xi / sum_j(e^xj) (AIE p.90). This normalizes the logits, which may be negative and do not sum to one, into non-negative values that sum to one.

## Key figures
None.

## Related
- [[logit-vector]]  (prerequisite: softmax takes the logit vector as input)
- [[sampling]]  (prerequisite: the probability distribution softmax produces is what sampling draws from)

## Provenance
- [[sources/ch02-sampling-fundamentals]]
