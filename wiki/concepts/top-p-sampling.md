---
type: concept
sources: [ch02-sampling-strategies]
---
# Top-p Sampling

Top-p sampling, also known as nucleus sampling, allows for a more dynamic selection of values to sample from than [[top-k-sampling]]. The model sums the probabilities of the most likely next values in descending order and stops when the cumulative sum reaches p; only the values within this cumulative probability are considered for sampling (AIE p.94). Unlike top-k, top-p doesn't necessarily reduce the softmax computation load, but because it focuses only on the most relevant values for each context, it allows outputs to be more contextually appropriate; despite limited theoretical justification, it has proven to work well in practice and has grown popular (AIE p.95).

A related strategy is min-p, where a minimum probability threshold is set that a token must reach to be considered during sampling (AIE p.95).

## Key figures
- Common top-p values in language models typically range from 0.9 to 0.95; a top-p of 0.9 means the model considers the smallest set of values whose cumulative probability exceeds 90% (AIE p.94)

## Related
- [[sampling]]  (part-of: one strategy for selecting the next token from a computed distribution)
- [[top-k-sampling]]  (contrast: fixed candidate count vs. dynamic cumulative-probability cutoff)
- [[temperature]]  (contrast: reshapes the whole probability distribution rather than bounding a candidate set)
- [[softmax]]  (prerequisite: cumulative probabilities are computed from a softmax distribution over logits)

## Provenance
- [[sources/ch02-sampling-strategies]]
