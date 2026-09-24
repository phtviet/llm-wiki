---
type: entity
sources: [ch06-retrieval-algorithms]
---
# HNSW (Hierarchical Navigable Small World)

HNSW (Malkov and Yashunin, 2016) constructs a multi-layer graph where nodes represent vectors and edges connect similar vectors, enabling nearest-neighbor search by traversing graph edges. Its authors' implementation is open source; it is also implemented in [[faiss]] and Milvus (AIE p.263). As an index type, HNSW provides high accuracy and fast query times but requires significant time and memory to build, in contrast to a simpler index like LSH (AIE p.266).

## Key figures
None.

## Related
- [[vector-database]]  (example-of: a detailed, high-accuracy vector index type)
- [[faiss]]  (see-also: implements HNSW alongside its own native algorithms)

## Provenance
- [[sources/ch06-retrieval-algorithms]]
