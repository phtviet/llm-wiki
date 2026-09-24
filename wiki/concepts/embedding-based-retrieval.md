---
type: concept
sources: [ch06-retrieval-algorithms]
---
# Embedding-Based Retrieval

Embedding-based retrieval (also called semantic retrieval) ranks documents by how closely their meanings align with a query, rather than by lexical overlap. It is generally considered a dense-retrieval approach, since [[embedding]]s are typically dense vectors, though sparse embeddings exist (e.g. SPLADE, which uses regularized BERT embeddings pushed toward zero for efficiency) (AIE p.257, p.260).

With embedding-based retrieval, indexing gains an extra step: converting data chunks into embeddings, stored in a [[vector-database]]. Querying then has two steps: (1) an embedding model converts the query into an embedding using the same model used at indexing time, and (2) a retriever fetches the k data chunks whose embeddings are closest to the query embedding. The value of k depends on the use case, generative model, and query. Real-world systems may add a reranker and caches (AIE p.260-261).

Embedding-based retrieval can be improved over time -- the embedding model and retriever can be finetuned, separately or together -- and supports more natural, semantics-focused queries than term-based retrieval. However, converting data into embeddings can obscure exact keywords (e.g. specific error codes or product names), making them harder to search; this limitation motivates combining embedding-based with term-based retrieval as [[hybrid-search]] (AIE p.265).

## Key figures
- Vector database spend can be one-fifth to half of a company's model-API spend (AIE p.265)

## Examples
- [[faiss]]

## Related
- [[term-based-retrieval]]  (contrast: semantic similarity vs. lexical matching; combined as [[hybrid-search]])
- [[vector-database]]  (prerequisite: embedding-based retrieval requires a vector database to store and search embeddings)
- [[embedding]]  (prerequisite: retrieval quality depends on embedding quality)
- [[mteb]]  (see-also: benchmark for evaluating the embeddings that power semantic retrieval)

## Provenance
- [[sources/ch06-retrieval-algorithms]]
