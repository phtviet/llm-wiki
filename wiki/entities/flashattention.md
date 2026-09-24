---
type: entity
sources: [ch09-model-optimization]
---
# FlashAttention

FlashAttention (Dao et al., 2022) is a kernel -- code optimized for a specific hardware accelerator -- that fuses together many operations commonly used in a transformer-based model to make attention computation run faster (AIE p.436). It was originally developed primarily for NVIDIA A100 GPUs; FlashAttention-3 was later introduced for H100 GPUs (Shah et al., 2024) (AIE p.438).

## Key figures
None.

## Related
- [[kernel]]  (example-of: a kernel written for attention computation)
- [[attention-mechanism-optimization]]  (part-of: the kernel-writing approach to attention optimization)

## Provenance
- [[sources/ch09-model-optimization]]
