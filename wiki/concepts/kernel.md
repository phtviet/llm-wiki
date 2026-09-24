---
type: concept
sources: [ch09-model-optimization]
---
# Kernel

A kernel is a piece of code specialized for a particular hardware accelerator (e.g. GPU or TPU), typically written to perform computationally intensive routines executed repeatedly and in parallel to maximize accelerator performance -- e.g. matrix multiplication, attention computation, and convolution (AIE p.437). Writing kernels requires deep understanding of the hardware's memory hierarchy (caches, global memory, shared memory, registers) and how data moves between levels. Kernels are typically written in low-level languages such as CUDA (NVIDIA GPUs), Triton (OpenAI's language for custom kernels), and ROCm (AMD GPUs), which give fine-grained control over threads and memory but are harder to learn than languages like Python (AIE p.437).

Historically writing kernels was a niche skill: chip makers like NVIDIA and AMD employ optimization engineers to write kernels for their hardware, while frameworks like PyTorch and TensorFlow employ kernel engineers to optimize across accelerators. Rising inference-optimization demand and accelerator ubiquity have broadened interest in kernel writing among AI engineers (AIE p.437-438).

Four common kernel-speedup techniques: vectorization (processing multiple contiguous data elements at once instead of one at a time), parallelization (dividing an array into independent chunks processed simultaneously across cores/threads), loop tiling (optimizing data-access order for the hardware's memory layout and cache, itself hardware-dependent), and operator fusion (combining multiple operators into a single pass to avoid redundant memory access) (AIE p.438). Operator fusion requires deeper understanding of a model's specific operators and architecture than the other three techniques (AIE p.438).

Because kernels are hardware-specific, new hardware requires new kernels; FlashAttention, for instance, was rewritten as FlashAttention-3 for newer GPUs (AIE p.438).

## Key figures
None.

## Examples
- [[flashattention]]  (kernel fusing common transformer operations for faster attention computation)

## Related
- [[compiler]]  (prerequisite: compilers convert model operations into kernels where possible during lowering)
- [[attention-mechanism-optimization]]  (part-of: kernel writing is one of the three attention-optimization buckets)
- [[ai-accelerator]]  (prerequisite: kernels are written for and optimized to specific accelerator hardware)

## Provenance
- [[sources/ch09-model-optimization]]
