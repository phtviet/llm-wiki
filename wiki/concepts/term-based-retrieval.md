---
type: concept
sources: [ch06-retrieval-algorithms]
---
# Term-Based Retrieval

Term-based retrieval (also called lexical retrieval) finds relevant documents using keyword matching: given a query, it retrieves documents containing the query's terms (AIE p.258). It is considered a sparse-retrieval approach, since each term can be represented as a sparse one-hot vector whose length equals the vocabulary size (AIE p.257).

Two problems drive its refinement. First, many documents may contain a term, so a heuristic ranks documents by how many times the term appears -- term frequency (TF). Second, not all query terms are equally informative; a term's importance is measured as inversely proportional to the number of documents it appears in -- inverse document frequency (IDF), computed as the total document count divided by the count of documents containing the term (AIE p.258-259). [[tf-idf]] combines TF and IDF into a single relevance score, and [[bm25]] refines TF-IDF by normalizing term frequency by document length (AIE p.259).

[[tokenization]] -- breaking a query into individual terms -- underlies term-based retrieval. Simple whitespace splitting can break multi-word terms (e.g. 'hot dog' into 'hot' and 'dog'), losing meaning; treating common n-grams as terms mitigates this. Preprocessing commonly includes lowercasing, punctuation removal, and stop-word elimination (AIE p.259-260).

Compared to embedding-based retrieval, term-based retrieval is much faster during indexing and querying, and performs well out of the box, but is simple and has fewer components to tune for improvement. It computes relevance at a lexical rather than semantic level, so a query like '[[transformer-architecture]]' can return irrelevant documents about unrelated senses of 'transformer' (AIE p.260, p.265).

## Key figures
None. Figures illustrating TF-IDF and BM25 mechanics are worked examples, not load-bearing; entity-specific figures live on [[bm25]] and [[elasticsearch]].

## Examples
- [[elasticsearch]]  (inverted-index-based term retrieval solution)
- [[bm25]]  (TF-IDF variant normalized by document length)

## Related
- [[embedding-based-retrieval]]  (contrast: lexical matching vs. semantic similarity; also combined as [[hybrid-search]])
- [[tf-idf]]  (part-of: TF-IDF is the scoring formula underlying term-based retrieval)
- [[bm25]]  (example-of: widely used term-based retrieval algorithm)
- [[lexical-similarity]]  (see-also: both measure surface-level text overlap, one for retrieval and one for evaluation)
- [[transformer-architecture]]  (see-also: mentioned in this page's text)
- [[tokenization]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch06-retrieval-algorithms]]
