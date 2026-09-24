---
type: concept
sources: [ch09-ai-accelerators]
---
# Computational Capabilities (Accelerators)

An accelerator's computational capability is typically measured by the number of operations it can perform in a given time, most commonly FLOP/s (floating-point operations per second, also written FLOPS). Achieving the theoretical peak FLOP/s in practice is rare; the ratio of actual to theoretical FLOP/s is a utilization metric (AIE p.421-422).

The number of operations a chip can perform per second depends on numerical precision: higher precision requires more computation per operation (e.g. adding two 32-bit numbers generally costs about twice the computation of adding two 16-bit numbers), though the exact ratio between precisions varies by chip optimization (AIE p.422).

## Key figures
- NVIDIA H100 SXM FLOP/s by precision (with sparsity): TF32 Tensor Core 989 teraFLOP/s, BFLOAT16 Tensor Core 1,979 teraFLOP/s, FP16 Tensor Core 1,979 teraFLOP/s, FP8 Tensor Core 3,958 teraFLOP/s (AIE p.422)

## Examples
- [[gpu]]  (H100 FLOP/s specs across precision formats)

## Related
- [[ai-accelerator]]  (part-of: computational capability is one of three characteristics used to evaluate an accelerator)
- [[numerical-representations]]  (prerequisite: FLOP/s throughput depends on the numerical precision format used)
- [[flop]]  (example-of: FLOP/s is the standard metric for computational capability, applied here to accelerator hardware)

## Provenance
- [[sources/ch09-ai-accelerators]]
