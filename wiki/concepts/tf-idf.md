---
type: concept
sources: [ch06-retrieval-algorithms]
---
# TF-IDF

TF-IDF (term frequency-inverse document frequency) is an algorithm that scores a document's relevance to a query by combining two metrics: term frequency (TF), how often a term appears in a document, and inverse document frequency (IDF), how rare a term is across all documents (AIE p.258-259).

For a term with document count C(t) out of N total documents, IDF(t) = log(N / C(t)); the higher a term's IDF, the more important it is. The naive TF-IDF score of document D for query Q sums, over all query terms, the term's IDF multiplied by its frequency in D: Score(D, Q) = sum of IDF(ti) x f(ti, D) (AIE p.258-259).

## Key figures
- Example: if 5 of 10 documents contain a term, its IDF is 10 / 5 = 2 (AIE p.259)

## Related
- [[term-based-retrieval]]  (part-of: TF-IDF is the core scoring formula for term-based retrieval)
- [[bm25]]  (prerequisite: BM25 is a modification of TF-IDF that normalizes term frequency by document length)

## Provenance
- [[sources/ch06-retrieval-algorithms]]
