---
type: concept
sources: [ch02-sampling-fundamentals]
---
# Greedy Sampling

Greedy sampling is the strategy of always picking the outcome with the highest probability (AIE p.88). It often works well for classification tasks -- e.g., if a model thinks an email is more likely spam than not, marking it as spam is sensible. For a language model, however, greedy sampling produces boring, repetitive outputs, since the model would always respond with the most common words for any given question (AIE p.88).

## Key figures
None.

## Related
- [[sampling]]  (part-of: one strategy for selecting an outcome from a computed probability distribution)
- [[best-of-n-sampling]]  (contrast: picks the single most likely token each step vs. generating and selecting among multiple full outputs)

## Provenance
- [[sources/ch02-sampling-fundamentals]]
