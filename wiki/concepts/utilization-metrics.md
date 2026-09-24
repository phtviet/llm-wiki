---
type: concept
sources: [ch09-inference-performance-metrics]
---
# Utilization Metrics (GPU Utilization, MFU, MBU)

Utilization metrics measure how efficiently a resource is used: the proportion of a resource's total capacity actively in use. NVIDIA's nvidia-smi tool reports GPU utilization as the percentage of time the GPU is actively processing tasks, but 'actively processing' does not mean processing efficiently -- a GPU can report 100% utilization while performing only a tiny fraction of its capable operations per second, making this metric not very useful for judging efficiency (AIE p.416).

A more informative metric is MFU (Model FLOP/s Utilization): the ratio of observed throughput (tokens/s) to the theoretical maximum throughput of a system running at its peak advertised FLOP/s. The term was introduced in the PaLM paper (Chowdhery et al., 2022) (AIE p.416-417). MBU (Model Bandwidth Utilization) measures the percentage of achievable memory bandwidth actually used, computed as (parameter count x bytes/param x tokens/s) / theoretical bandwidth (AIE p.417).

Throughput, MFU, and MBU are linearly related, so some people use throughput as a stand-in for either. What counts as good MFU/MBU depends on model, hardware, and workload: compute-bound workloads tend toward higher MFU and lower MBU, while bandwidth-bound workloads show the reverse. Training MFU is typically higher than inference MFU because training workloads are more predictable and benefit more from batching; within inference, prefill (compute-bound) typically has higher MFU than decode (memory bandwidth-bound) (AIE p.417). Higher utilization is not itself the goal -- what matters is getting jobs done faster and cheaper, so a higher utilization rate that comes with higher cost and latency is not actually beneficial (AIE p.418).

## Key figures
- MBU worked example: a 7B-parameter model in FP16 (2 bytes/param) at 100 tokens/s uses 7B x 2 x 100 = 700 GB/s of bandwidth; on an A100-80GB GPU with 2 TB/s theoretical bandwidth, MBU = 700/2000 = 70% (AIE p.417)
- MFU examples from the PaLM paper: GPT-3 (175B, V100) 21.3%; Gopher (280B, 4096 TPU v3) 32.5%; Megatron-Turing NLG (530B, 2240 A100) 30.2%; PaLM (540B, 6144 TPU v4) 46.2% (AIE p.417)
- For model training, an MFU above 50% is generally considered good, though hard to achieve on specific hardware (AIE p.417)

## Examples
- None.

## Related
- [[throughput-and-goodput]]  (see-also: throughput and MFU/MBU are linearly related, so throughput sometimes substitutes for either)
- [[quantization]]  (prerequisite: MBU calculation depends on bytes per parameter, so quantization directly changes bandwidth used)
- [[gpu]]  (example-of: nvidia-smi's GPU-utilization metric is measured on GPUs specifically, and is the metric MFU/MBU are contrasted against)
- [[tpu]]  (example-of: TPU v3 and TPU v4 appear among the PaLM-paper MFU examples)

## Provenance
- [[sources/ch09-inference-performance-metrics]]
