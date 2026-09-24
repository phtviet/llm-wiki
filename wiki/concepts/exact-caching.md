---
type: concept
sources: [ch10-step-4-reduce-latency-with-caches]
---
# Exact Caching

With exact caching, a cached item is reused only when the exact same item is requested again. For example, if a user asks a model to summarize a product, the system checks whether a summary of that exact product already exists in the cache; if so it is fetched, otherwise the product is summarized and the result cached. Exact caching is also used for embedding-based retrieval, to avoid redundant vector search when an incoming query is already cached (AIE p.460).

Caching is especially valuable for queries involving multiple steps (e.g., chain-of-thought) or time-consuming actions (e.g., retrieval, SQL execution, or web search), since it can skip repeating that work. An exact cache can be implemented with in-memory storage for fast retrieval, or with databases such as PostgreSQL or Redis, or tiered storage, to balance speed and capacity. An eviction policy is crucial to manage cache size and maintain performance; common policies include Least Recently Used (LRU), Least Frequently Used (LFU), and first in, first out (FIFO). Whether a query is worth caching depends on how likely it is to recur: user-specific queries (e.g., 'What's the status of my recent order?') and time-sensitive queries (e.g., 'How's the weather?') are poor caching candidates. Many teams train a classifier to predict whether a query should be cached (AIE p.460-461).

Caching can cause data leaks if not handled properly. If a response depends on user-specific information (e.g., a return policy that varies by membership) but the system mistakes the query for a generic one and caches the personalized answer, a later user asking the same generic-seeming question can be served the first user's private information (AIE p.461).

## Key figures
None.

## Examples
- [[rag-architecture]]  (embedding-based retrieval can cache vector search results to avoid redundant lookups)

## Related
- [[semantic-caching]]  (contrast: reuses results only for identical requests vs. for semantically similar ones)
- [[vector-database]]  (see-also: exact caching for embedding-based retrieval checks the vector search cache before querying the vector database)

## Provenance
- [[sources/ch10-step-4-reduce-latency-with-caches]]
