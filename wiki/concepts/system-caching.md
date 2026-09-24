---
type: concept
sources: [ch10-step-4-reduce-latency-with-caches]
---
# System Caching

System caching applies established software-caching ideas to AI applications to reduce latency and cost, distinct from inference-level caching mechanisms like [[kv-cache]] and [[prompt-caching]] (discussed for inference optimization). There are two major system caching mechanisms: [[exact-caching]] and [[semantic-caching]] (AIE p.460).

## Key figures
None.

## Examples
- [[exact-caching]]  (reuses results only for identical requests)
- [[semantic-caching]]  (reuses results for semantically similar requests)

## Related
- [[kv-cache]]  (contrast: inference-level caching mechanism vs. system-level caching covered here)
- [[prompt-caching]]  (contrast: inference-level caching mechanism vs. system-level caching covered here)
- [[exact-caching]]  (part-of: one of the two major system caching mechanisms)
- [[semantic-caching]]  (part-of: one of the two major system caching mechanisms)

## Provenance
- [[sources/ch10-step-4-reduce-latency-with-caches]]
