---
type: concept
sources: [ch06-retrieval-algorithms]
---
# Retrieval Quality Metrics (Context Precision and Recall)

A retriever's quality can be evaluated based on the quality of documents it retrieves, using two metrics common in RAG evaluation frameworks: context precision (also called context relevance) and context recall. Context precision asks, of all retrieved documents, what percentage is relevant to the query; context recall asks, of all documents relevant to the query, what percentage was retrieved (AIE p.264).

To compute these, an evaluation set of test queries and documents is curated, and each test document is annotated relevant or not relevant to each query, either by humans or AI judges. Context precision is simpler to compute since it only requires comparing retrieved documents to the query; context recall requires annotating the relevance of all documents in the database to that query, which many production RAG frameworks skip supporting (AIE p.264).

When ranking order matters (more relevant documents should rank first), metrics such as NDCG (normalized discounted cumulative gain), MAP (Mean Average Precision), and MRR (Mean Reciprocal Rank) can be used instead (AIE p.264-265).

A full RAG system evaluation should cover retrieval quality, the quality of embeddings (for embedding-based retrieval), and the final generated outputs, since a retriever is ultimately good only if it helps the system produce high-quality answers (AIE p.265).

## Key figures
None.

## Related
- [[embedding-based-retrieval]]  (evaluates: context precision/recall assess the documents an embedding-based retriever returns)
- [[mteb]]  (see-also: separate benchmark for evaluating embedding quality itself, alongside retrieval-output evaluation)
- [[bird-sql]]  (see-also: both are component-level evaluation approaches within larger AI systems)

## Provenance
- [[sources/ch06-retrieval-algorithms]]
