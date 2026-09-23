---
type: concept
sources: [ch02-sampling-strategies]
---
# Top-p Sampling

Top-p sampling, also known as nucleus sampling, dynamically selects the set of values to sample from: the model sums token probabilities in descending order and stops once the cumulative sum reaches p, considering only the values within that cumulative probability (AIE p.94). This adapts the number of candidates to the situation — few for a yes/no question, many for an open-ended one — unlike the fixed count used by [[top-k-sampling]] (AIE p.94). Unlike top-k, top-p doesn't necessarily reduce softmax's computation load, since its benefit is contextual appropriateness rather than speed, but it has proven popular in practice (AIE p.94-95). A related strategy, min-p, sets a minimum probability a token must reach to be considered during sampling (AIE p.95).

## Key figures
- Common top-p values range from 0.9 to 0.95 (AIE p.94)
- A top-p of 0.9 means the model considers the smallest set of values whose cumulative probability exceeds 90% (AIE p.94)

## Related
- [[top-k-sampling]]  (contrast: top-p varies the candidate set size via cumulative probability instead of a fixed k)
- [[softmax]]  (boundary: top-p narrows the candidate set for contextual relevance but does not necessarily reduce softmax's computation cost)
- [[sampling]]  (part-of: one strategy among several for shaping model output)

## Provenance
- [[sources/ch02-sampling-strategies]]
