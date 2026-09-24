---
type: concept
sources: [ch05-in-context-learning-zero-shot-and-few-shot]
---
# Few-Shot Learning

Few-shot learning is [[in-context-learning]] where the model is given examples, called shots, in the prompt. Five examples in the prompt makes it 5-shot learning; providing none is [[zero-shot-learning]] instead. In general, the more examples shown, the better a model can learn the desired behavior, though the number is bounded by the model's maximum [[context-length]] and more examples increase prompt length and inference cost (AIE p.213-214).

For GPT-3, few-shot learning showed significant improvement over zero-shot learning. However, Microsoft's 2023 analysis found few-shot learning led to only limited improvement over zero-shot learning on GPT-4 and other models, suggesting more powerful models are better at following instructions with fewer examples. That study may have underestimated the value of few-shot examples for domain-specific use cases: if a model has seen few training examples of a specific API (e.g. the Ibis dataframe API), including examples of it in the prompt can still make a large difference (AIE p.214).

## Key figures
None.

## Examples
- [[zero-shot-learning]]  (the no-example counterpart)

## Related
- [[in-context-learning]]  (part-of: few-shot learning is in-context learning performed with example shots in the prompt)
- [[zero-shot-learning]]  (contrast: examples provided in the prompt vs. none)
- [[context-length]]  (boundary: number of usable shots is capped by the model's maximum context length)

## Provenance
- [[sources/ch05-in-context-learning-zero-shot-and-few-shot]]
