---
type: concept
sources: [ch06-retrieval-optimization]
---
# Reranking

Reranking is the process of reordering documents that a retriever has already fetched to make the ranking more accurate. It is especially useful when the number of retrieved documents needs to be reduced, either to fit a model's context or to reduce input token count (AIE p.269). A common pattern combines a cheap but less precise retriever to fetch candidates with a more precise, more expensive mechanism that reranks them.

Documents can also be reranked by time, weighting more recent data higher — useful for time-sensitive applications like news aggregation, an email chatbot, or stock market analysis. Context reranking (reranking documents that will be placed in a model's context) differs from traditional search reranking: in search, exact rank position (first vs. fifth) is crucial, but in context reranking the order still matters — since models tend to better understand documents at the beginning and end of the context — but the impact of order is less significant than in search ranking, as long as a relevant document is included at all (AIE p.269).

## Key figures
None.

## Examples
None.

## Related
- [[chunking-strategy]]  (see-also: reranking operates on the chunks that chunking strategy produces and a retriever fetches)
- [[context-length]]  (boundary: models understand documents at the start/end of context better, making position within context still matter for reranking)
- [[retriever]]  (prerequisite: reranking reorders documents an initial retriever has already fetched)

## Provenance
- [[sources/ch06-retrieval-optimization]]
