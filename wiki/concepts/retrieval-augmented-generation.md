---
type: concept
sources: [ch01-from-large-language-models-to-foundation-models]
---
# Retrieval-Augmented Generation (RAG)

Retrieval-augmented generation (RAG) is the technique of connecting a model to an external database -- for example, a database of customer reviews -- that the model can leverage to supplement its instructions and generate better outputs (AIE p.11). It is presented alongside [[prompt-engineering]] and [[finetuning]] as one of three common AI engineering techniques for adapting a foundation model to specific needs (AIE p.11).

## Key figures
None.

## Examples
- Connecting a product-description generator to a database of customer reviews (AIE p.11)

## Related
- [[foundation-model]]  (prerequisite: RAG is one way of adapting a general-purpose foundation model)
- [[prompt-engineering]]  (contrast: supplementing instructions with a retrieved database vs. crafting instructions/examples directly)
- [[finetuning]]  (contrast: retrieving external data at inference time vs. further training the model's weights)

## Provenance
- [[sources/ch01-from-large-language-models-to-foundation-models]]
