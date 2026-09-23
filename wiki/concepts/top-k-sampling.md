---
type: concept
sources: [ch02-sampling-strategies]
---
# Top-k Sampling

Top-k is a sampling strategy that reduces computation by performing softmax over only the top-k highest logits rather than the full vocabulary, then sampling from those top values (AIE p.93). A smaller k makes text more predictable but less interesting, since the model is limited to a smaller set of likely words; k is typically chosen anywhere from 50 to 500, much smaller than a model's vocabulary size (AIE p.93).

## Key figures
- k typically ranges from 50 to 500 (AIE p.93)

## Related
- [[softmax]]  (boundary: top-k restricts softmax's computation to a fixed-size subset instead of the full vocabulary)
- [[top-p-sampling]]  (contrast: top-k fixes the number of candidates considered, while top-p varies it based on cumulative probability)
- [[sampling]]  (part-of: one strategy among several for shaping model output)

## Provenance
- [[sources/ch02-sampling-strategies]]
