---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Model Parameters

A parameter is a variable within an ML model that is updated through training; today the term 'model weights' is generally used to refer to all parameters (AIE p.7). A model's size is typically measured by its number of parameters, and in general -- though not always -- more parameters mean greater capacity to learn desired behaviors (AIE p.7).

What counts as 'large' has shifted over time: OpenAI's first GPT model (June 2018) had 117 million parameters and was considered large; GPT-2 (February 2019), with 1.5 billion parameters, downgraded 117 million to 'small'; as of the book's writing, 100 billion parameters is considered large (AIE p.8). Larger models need more training data because they have more capacity to learn and maximizing their performance requires proportionally more examples -- training a large model on a small dataset wastes compute, since similar or better results could be had from a smaller model on that same dataset (AIE p.8).

## Key figures
- GPT-1 (June 2018): 117 million parameters, considered large at the time (AIE p.8)
- GPT-2 (February 2019): 1.5 billion parameters (AIE p.8)
- As of writing, 100 billion parameters is considered large (AIE p.8)

## Examples
None.

## Related
- [[language-model]]  (part-of: parameter count is how a language model's scale is measured)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
