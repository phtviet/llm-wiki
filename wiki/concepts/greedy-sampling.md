---
type: concept
sources: [ch02-sampling-fundamentals]
---
# Greedy Sampling

Greedy sampling is always picking the outcome with the highest probability (AIE p.88). It often works for classification tasks—if an email is more likely to be spam than not, marking it spam is reasonable—but for a language model it produces boring output, since the model would always respond with the most common words for any given context (AIE p.88-89). This motivates sampling the next token according to its probability instead of always taking the most likely one.

## Key figures
None.

## Related
- [[sampling]]  (part-of: greedy sampling is one strategy within the broader sampling process; contrast: picks the single most likely outcome instead of drawing from the full distribution)

## Provenance
- [[sources/ch02-sampling-fundamentals]]
