---
type: concept
sources: [ch09-ai-accelerators]
---
# AI Accelerator

An accelerator is a chip designed to speed up a specific type of computational workload; an AI accelerator is designed for AI workloads. The dominant type of AI accelerator is the GPU, and NVIDIA is the biggest economic driver of the AI-accelerator market in the early 2020s (AIE p.420).

CPUs are designed for general-purpose usage, with a few powerful cores (up to around 64 on high-end consumer machines) suited to high single-thread performance and sequential processes. GPUs instead have thousands of smaller, less powerful cores optimized for tasks that decompose into many small independent calculations, such as the matrix multiplication that dominates ML workloads. This parallel-processing focus improves computational throughput but creates challenges for memory design and power consumption (AIE p.420).

While many chips handle both training and inference, a growing theme is specialized inference chips. Training demands more memory (due to [[backpropagation]]) and generally resists lower precision, and emphasizes throughput, whereas inference aims to minimize latency; consequently inference-oriented chips are often optimized for lower precision and faster memory access rather than large memory capacity (AIE p.420-421). A model architecture can also be co-designed for a chip -- the transformer was originally designed by Google to run fast on TPUs before being optimized for GPUs (AIE p.420).

When selecting an accelerator, the deciding questions are whether the hardware can run the workload, how long that takes, and how much it costs. Compute-bound workloads favor chips with higher FLOP/s; memory-bound workloads favor chips with higher bandwidth and more memory (AIE p.425).

## Key figures
- Inference can account for up to 90% of machine learning costs for deployed AI systems, per a survey by Desislavov et al. (2023) (AIE p.420)
- CPU cores: up to ~64 on high-end consumer machines (AIE p.420)

## Examples
- [[gpu]]  (dominant AI accelerator type)
- [[tpu]]  (Google's tensor-primitive accelerator)

## Related
- [[gpu]]  (example-of: GPUs are the dominant AI accelerator)
- [[tpu]]  (example-of: TPUs are a tensor-optimized AI accelerator)
- [[computational-capabilities]]  (part-of: FLOP/s is one of the three characteristics used to evaluate an accelerator)
- [[accelerator-memory-hierarchy]]  (part-of: memory size and bandwidth is one of the three characteristics used to evaluate an accelerator)
- [[power-consumption]]  (part-of: power draw is one of the three characteristics used to evaluate an accelerator)
- [[inference-optimization]]  (prerequisite: understanding accelerator hardware enables deeper inference-time optimization)
- [[alexnet]]  (see-also: AlexNet's use of GPUs for training is cited as the reason for its impact on the deep learning revolution)
- [[backpropagation]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch09-ai-accelerators]]
