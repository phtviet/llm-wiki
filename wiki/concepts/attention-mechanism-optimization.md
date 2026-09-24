---
type: concept
sources: [ch09-model-optimization]
---
# Attention Mechanism Optimization

Attention mechanism optimization covers techniques to reduce the computation and memory cost of the attention mechanism during inference, falling into three buckets: redesigning the attention mechanism, optimizing the KV cache, and writing kernels for attention computation (AIE p.434).

Redesigning the attention mechanism changes the model's architecture directly, so it can only be applied during training or finetuning (AIE p.434). Local windowed attention attends only to a fixed-size window of nearby tokens rather than all previous tokens, reducing the effective sequence length and hence the KV cache and computation cost (Beltagy et al., 2020); it can be interleaved with global attention, where local attention captures nearby context and global attention captures task-specific information across the document (AIE p.434). Cross-layer attention (Brandon et al., 2024) shares key-value vectors across adjacent layers, and multi-query attention (Shazeer, 2019) shares them across query heads, both reducing KV cache memory footprint (AIE p.434-435). Grouped-query attention (Ainslie et al., 2023) generalizes multi-query attention by grouping query heads and sharing key-value pairs only within a group, balancing flexibility between query-head count and key-value-pair count (AIE p.435).

## Key figures
- Attending to a 1,000-token window instead of an average 10,000-token sequence reduces KV cache size by 10 times (AIE p.434)
- Three layers sharing key-value vectors via cross-layer attention reduces the KV cache three times (AIE p.434)

## Examples
None.

## Related
- [[kv-cache]]  (part-of: KV cache optimization is one bucket of attention mechanism optimization)
- [[attention-mechanism]]  (prerequisite: optimizes the underlying attention computation)
- [[flashattention]]  (example-of: kernel-writing bucket of attention optimization)

## Provenance
- [[sources/ch09-model-optimization]]
