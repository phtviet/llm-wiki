---
type: concept
sources: [ch09-inference-overview]
---
# Computational Bottlenecks (Compute-Bound vs. Memory Bandwidth-Bound)

Optimization means identifying bottlenecks and addressing them. Inference workloads face two main computational bottlenecks (AIE p.407):

- **Compute-bound**: time-to-complete is determined by the computation the task needs, such as password decryption's intensive mathematical calculations (AIE p.407).
- **Memory bandwidth-bound** (often loosely called memory-bound): time-to-complete is constrained by the data transfer rate within the system, such as moving data from CPU memory to GPU memory (AIE p.407-408). The term 'memory-bound' is used ambiguously: some use it for this bandwidth constraint, others for memory-capacity constraints (e.g., an out-of-memory/OOM error when hardware lacks enough memory to hold a task) (AIE p.408). A capacity limitation can often be mitigated by splitting a task across memory tiers (e.g., splitting a model across GPU and CPU memory), though this slows computation via added data transfer -- ultimately making capacity limits a bandwidth issue too (AIE p.408).

Mathematically, whether an operation is compute-bound or memory bandwidth-bound is determined by its arithmetic intensity -- the number of arithmetic operations per byte of memory accessed -- a classification introduced in the Roofline paper (Williams et al., 2009) (AIE p.408). Profiling tools like NVIDIA Nsight visualize this via a roofline chart (AIE p.408).

Different architectures and workloads land on different sides: image generators like Stable Diffusion are typically compute-bound, while [[autoregressive-language-model]] inference is typically memory bandwidth-bound (AIE p.408-409). Different optimization techniques target different bottlenecks -- a compute-bound workload benefits from more chips or higher FLOP/s hardware, while a memory bandwidth-bound workload benefits from higher-bandwidth hardware (AIE p.408).

For transformer-based language models, inference splits into prefill and decode steps with opposite profiles: prefill is compute-bound and decode is memory bandwidth-bound (AIE p.409). [[context-length]], output length, and request batching strategies affect how much prefilling and decoding computation occurs, and thus which bottleneck dominates; long context typically produces a memory bandwidth-bound workload, though optimization techniques can remove this bottleneck (AIE p.409-410). As of the book's writing, the prevalence of the [[transformer-architecture]] and current accelerator limitations mean many AI workloads are memory bandwidth-bound, though future hardware and software may shift this toward compute-bound (AIE p.410).

## Key figures
None.

## Examples
- [[prefill-and-decode]]  (compute-bound prefill vs. memory bandwidth-bound decode in transformer inference)

## Related
- [[prefill-and-decode]]  (example-of: the prefill/decode split in transformer inference illustrates the compute-bound/memory bandwidth-bound distinction)
- [[inference-server]]  (prerequisite: an inference server's design must address these bottlenecks)
- [[gpu]]  (see-also: accelerator choice interacts with which bottleneck a workload hits)
- [[flop]]  (see-also: FLOP/s measures compute capability relevant to compute-bound workloads)
- [[autoregressive-language-model]]  (see-also: mentioned in this page's text)
- [[transformer-architecture]]  (see-also: mentioned in this page's text)
- [[context-length]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch09-inference-overview]]
