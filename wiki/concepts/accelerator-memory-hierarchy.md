---
type: concept
sources: [ch09-ai-accelerators]
---
# Accelerator Memory Hierarchy

An AI accelerator such as a GPU interacts with three levels of memory. Because many cores work in parallel, data must move quickly from memory to cores, so data transfer speed (bandwidth and latency) matters as much as capacity (AIE p.422).

- **CPU memory (DRAM)**: also called system or host memory; accelerators are usually deployed alongside CPUs and can access it. It has the lowest bandwidth of the three levels (AIE p.422-423).
- **GPU high-bandwidth memory (HBM)**: dedicated GPU memory located close to the chip for faster access than CPU memory; uses a 3D-stacked structure (versus CPU DDR SDRAM's 2D structure), making it more expensive (AIE p.422-423).
- **GPU on-chip SRAM**: integrated directly into the chip (L1/L2, sometimes L3 caches, register files, shared memory) for near-instant access to frequently used data; the fastest but smallest tier (AIE p.423).

Popular frameworks like PyTorch and TensorFlow do not yet allow fine-grained control of memory access across this hierarchy, which has driven interest in GPU programming languages such as CUDA, OpenAI's Triton, and ROCm (AIE p.423).

## Key figures
- CPU memory bandwidth: 25-50 GB/s; typical size 16-64 GB (laptops) up to 1 TB+ (high-end workstations) (AIE p.423)
- GPU HBM bandwidth: 256 GB/s to over 1.5 TB/s; consumer GPU HBM size: ~24-80 GB (AIE p.423)
- GPU on-chip SRAM: bandwidth often exceeding 10 TB/s; size typically 40 MB or under (AIE p.423)

## Examples
- [[gpu]]  (HBM and on-chip SRAM figures)

## Related
- [[ai-accelerator]]  (part-of: memory size and bandwidth is one of three characteristics used to evaluate an accelerator)
- [[gpu]]  (example-of: GPU memory hierarchy spans CPU DRAM, GPU HBM, and on-chip SRAM)
- [[numerical-representations]]  (see-also: memory footprint also depends on the numerical precision of stored data)

## Provenance
- [[sources/ch09-ai-accelerators]]
