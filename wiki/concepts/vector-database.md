---
type: concept
sources: [ch06-retrieval-algorithms]
---
# Vector Database

A vector database stores vectors (typically embeddings) and is responsible for vector search: given a query embedding, finding and returning nearby vectors in the database. Vectors must be indexed and stored so that vector search is fast and efficient. Vector search is common in any application using embeddings -- search, recommendation, data organization, clustering, fraud detection -- not only RAG (AIE p.261).

Vector search is framed as a nearest-neighbor search problem. The naive solution, k-nearest neighbors (k-NN), computes similarity scores (e.g. cosine similarity) between the query and all vectors, ranks them, and returns the top k; this is precise but computationally heavy and suited only to small datasets. For large datasets, approximate nearest neighbor (ANN) algorithms are used instead, organizing vectors into buckets, trees, or graphs, and optionally quantizing or sparsifying vectors to reduce compute (AIE p.261-262).

A detailed index such as [[hnsw]] gives high accuracy and fast query times but takes longer and more memory to build; a simpler index such as LSH is quicker and less memory-intensive to build but yields slower, less accurate queries (AIE p.266). Any database that can store and search vectors can be called a vector database; many traditional databases have extended or plan to extend to support this (AIE p.263).

## Key figures
None.

## Examples
- [[faiss]]
- [[hnsw]]

## Related
- [[embedding-based-retrieval]]  (prerequisite: embedding-based retrieval depends on a vector database for storage and search)
- [[ann-benchmarks]]  (evaluates: compares ANN algorithms on recall, QPS, build time, and index size)

## Provenance
- [[sources/ch06-retrieval-algorithms]]
