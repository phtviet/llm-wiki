---
type: concept
sources: [ch06-retrieval-algorithms]
---
# Reciprocal Rank Fusion (RRF)

Reciprocal rank fusion (RRF) (Cormack et al., 2009) is an algorithm for combining rankings from multiple retrievers used in parallel. It assigns each document a score based on its rank from each retriever: rank 1 scores 1/1 = 1, rank 2 scores 1/2 = 0.5, and so on -- the higher the rank, the higher the score. A document's final score is the sum of its scores across all retrievers; a document ranked first by one retriever and second by another scores 1 + 0.5 = 1.5 (AIE p.267).

The full formula for a document D is Score(D) = sum over retrievers i of 1 / (k + ri(D)), where n is the number of ranked lists, ri(D) is D's rank from retriever i, and k is a constant avoiding division by zero and controlling the influence of lower-ranked documents (AIE p.267).

## Key figures
- Typical value of the constant k is 60 (AIE p.267)

## Related
- [[hybrid-search]]  (part-of: RRF is the algorithm used to merge rankings from parallel retrievers in hybrid search)

## Provenance
- [[sources/ch06-retrieval-algorithms]]
