---
type: entity
sources: [ch09-ai-accelerators]
---
# GPU (Graphics Processing Unit)

The GPU is the dominant type of [[ai-accelerator]]. Unlike CPUs, which have a few powerful cores tuned for single-thread and sequential work, GPUs have thousands of smaller cores optimized for highly parallelizable tasks such as graphics rendering and the matrix multiplication that dominates machine learning workloads (AIE p.420).

GPUs were central to the 2012 revival of deep learning: [[alexnet]] is commonly credited as the first paper to successfully train neural networks using GPUs, making large-scale training far more accessible than the thousands of CPUs it would otherwise have required (AIE p.419).

Modern GPUs increasingly include tensor cores optimized for matrix/tensor computation in addition to their traditional vector-operation support (AIE p.421). High-end GPUs use HBM (high-bandwidth memory), a 3D-stacked memory technology offering much higher bandwidth than CPU DRAM, which is one reason GPU memory is more expensive than CPU memory (AIE p.422). NVIDIA's proprietary CUDA and AMD's open source ROCm are GPU programming languages used to get finer-grained control of memory access than frameworks like PyTorch and TensorFlow currently expose (AIE p.423).

## Key figures
- NVIDIA H100 SXM FLOP/s by precision (with sparsity): TF32 Tensor Core 989 teraFLOP/s, BFLOAT16 Tensor Core 1,979 teraFLOP/s, FP16 Tensor Core 1,979 teraFLOP/s, FP8 Tensor Core 3,958 teraFLOP/s (AIE p.422)
- Consumer GPU HBM: roughly 24-80 GB (AIE p.423)
- GPU HBM bandwidth: typically 256 GB/s to over 1.5 TB/s (AIE p.423)
- GPU on-chip SRAM: typically 40 MB or under, with data transfer speeds often exceeding 10 TB/s (AIE p.423)
- NVIDIA A100: 54 billion transistors; NVIDIA H100: 80 billion transistors (AIE p.424)
- NVIDIA H100 running at peak for a year: approximately 7,000 kWh, versus ~10,000 kWh average annual US household electricity consumption (AIE p.424)

## Related
- [[ai-accelerator]]  (example-of: GPUs are the dominant AI accelerator type)
- [[tpu]]  (contrast: TPUs use tensor operations as their primary compute primitive vs. GPUs' historically vector-oriented, now mixed, compute units)
- [[alexnet]]  (see-also: AlexNet's GPU training is credited with sparking the deep learning research boom)
- [[accelerator-memory-hierarchy]]  (part-of: GPU HBM and on-chip SRAM are levels of the accelerator memory hierarchy)
- [[computational-capabilities]]  (example-of: H100 FLOP/s figures illustrate how numerical precision affects computational throughput)
- [[power-consumption]]  (example-of: A100/H100 transistor counts and H100 annual energy use illustrate accelerator power consumption)

## Provenance
- [[sources/ch09-ai-accelerators]]
