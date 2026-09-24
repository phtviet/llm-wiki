---
type: concept
sources: [ch09-model-optimization]
---
# KV Cache

Generating token xt+1 requires the key and value vectors for all preceding tokens. Rather than recompute them at every decoding step, the KV cache stores these vectors for reuse, so only the most recently generated token's key and value vectors need to be computed and appended to the cache (AIE p.432-433). A KV cache is used only during inference; during training all tokens in a sequence are known in advance, so next-token computations can be done all at once rather than sequentially, removing the need for a cache (AIE p.433).

The number of attention computations grows exponentially (O(n^2)) with sequence length, while KV cache size grows linearly with sequence length and also grows with [[batch-size]]. Cache size is ultimately bounded by available hardware memory, creating a bottleneck for long-context applications, and a large cache also takes time to load into memory, an issue for latency-sensitive applications (AIE p.433).

The cache size, without optimization, is calculated as 2 x B x S x L x H x M, where B is batch size, S is sequence length, L is number of transformer layers, H is model dimension, and M is the memory needed per cached value (e.g. FP16 or FP32) (AIE p.434).

Techniques to make the attention mechanism more efficient fall into three buckets: redesigning the attention mechanism, optimizing KV cache management, and writing kernels for attention computation (AIE p.434).

## Key figures
- A 500B+ model with multi-head attention, batch size 512, and [[context-length]] 2048 has a 3TB KV cache -- three times the size of the model's weights (Pope et al., 2022) (AIE p.433)
- [[llama-2]] 13B (40 layers, model dimension 5,120), batch size 32, sequence length 2,048, FP16 (2 bytes/value): KV cache = 2 x 32 x 2,048 x 40 x 5,120 x 2 = 54 GB (AIE p.434)
- Character.AI reduced KV cache size by over 20x using multi-query attention, interleaved local/global attention, and cross-layer attention, given an average 180-message dialogue history (AIE p.435)

## Examples
None.

## Related
- [[attention-mechanism-optimization]]  (part-of: KV cache management is one of the three buckets of attention optimization)
- [[attention-mechanism]]  (prerequisite: the KV cache exists to avoid recomputing attention's key/value vectors)
- [[flashattention]]  (see-also: FlashAttention optimizes attention computation directly rather than cache storage)
- [[context-length]]  (see-also: mentioned in this page's text)
- [[batch-size]]  (see-also: mentioned in this page's text)
- [[llama-2]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch09-model-optimization]]
