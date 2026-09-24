---
type: concept
sources: [ch10-step-4-reduce-latency-with-caches]
---
# Semantic Caching

Unlike exact caching, semantic caching reuses cached results even when the incoming query is only semantically similar, not identical, to a previously cached one. For example, 'What's the capital of Vietnam?' and 'What's the capital city of Vietnam?' are worded differently but semantically equivalent, so the cached answer to the first can be reused for the second. Reusing similar queries increases the cache's hit rate and can reduce cost, but semantic caching can also reduce a model's performance if a match is wrongly judged similar (AIE p.460-461).

Semantic caching depends on a reliable way to determine query similarity, typically [[semantic-similarity]] via embeddings. The process: (1) generate an embedding for each incoming query; (2) use vector search to find the cached embedding with the highest similarity score to the current query; (3) if that score exceeds a similarity threshold, treat the cached query as a match and return its cached result, otherwise process the query and cache it together with its embedding and result. This requires a [[vector-database]] to store cached query embeddings (AIE p.461-462).

Semantic caching's value is more dubious than other caching techniques because many of its components are prone to failure: it depends on high-quality embeddings, functional vector search, and a reliable similarity metric, and setting the right similarity threshold takes significant trial and error. A mismatched query returns an incorrect cached response. Semantic caching is also time-consuming and compute-intensive, since it requires a vector search whose speed and cost scale with the size of the cached embeddings. It may still be worthwhile if the cache hit rate is high, but the efficiency, cost, and performance risks should be evaluated first (AIE p.462).

## Key figures
None.

## Examples
None.

## Related
- [[exact-caching]]  (contrast: reuses results for semantically similar queries vs. only identical ones)
- [[semantic-similarity]]  (prerequisite: semantic caching relies on semantic similarity to judge whether two queries match)
- [[vector-database]]  (prerequisite: semantic caching requires a vector database to store and search cached query embeddings)

## Provenance
- [[sources/ch10-step-4-reduce-latency-with-caches]]
