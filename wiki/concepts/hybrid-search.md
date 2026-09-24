---
type: concept
sources: [ch06-retrieval-algorithms]
---
# Hybrid Search

Hybrid search combines term-based retrieval and embedding-based retrieval to leverage the distinct advantages of each, since a production retrieval system typically needs more than one approach (AIE p.265-266).

Algorithms can be combined in sequence: a cheap, less precise retriever (e.g. term-based) fetches candidates first, then a more precise, more expensive mechanism (e.g. k-nearest neighbors) selects the best among them -- a step also called [[reranking]]. For example, a keyword search for 'transformer' fetches all documents containing the word, then vector search narrows these to the ones actually about the intended sense of 'transformer' (AIE p.266).

Algorithms can also be combined in parallel, as an ensemble: multiple retrievers fetch candidates simultaneously, and their rankings are merged into a final ranking via an algorithm such as [[reciprocal-rank-fusion]] (AIE p.266).

## Key figures
None.

## Related
- [[term-based-retrieval]]  (part-of: one of the two retrieval approaches combined in hybrid search)
- [[embedding-based-retrieval]]  (part-of: one of the two retrieval approaches combined in hybrid search)
- [[reciprocal-rank-fusion]]  (example-of: an algorithm for combining parallel retriever rankings into one)
- [[reranking]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch06-retrieval-algorithms]]
