---
type: concept
sources: [ch09-inference-service-optimization]
---
# Parallelism Strategies

Accelerators are designed for parallel processing, and parallelism strategies are foundational to serving models efficiently at scale. The book covers two families applicable to all models -- data/replica parallelism and model parallelism -- plus context and sequence parallelism, applied specifically to LLMs for efficient long-input processing (AIE p.444).

**Replica parallelism** creates multiple replicas of a model to serve, allowing more concurrent requests at the cost of more chips; fitting differently-sized models onto differently-sized chips is a bin-packing problem (AIE p.444-445).

**Model parallelism** splits a single model across multiple machines when it is too large to fit on one. The most common inference approach is **tensor parallelism** (intra-operator parallelism), which partitions the tensors within an operator (e.g. columnwise matrix-multiplication splits) across devices, executing pieces in parallel; this both enables serving oversized models and can reduce latency, though communication overhead can offset the latency gain (AIE p.445). **Pipeline parallelism** divides a model's computation into stages assigned to different devices, streaming micro-batches through the stages so computation overlaps; it enables serving large models across machines but adds per-request latency from inter-stage communication, so latency-sensitive applications favor replica parallelism over pipeline parallelism, while pipeline parallelism remains common in training for its throughput benefit (AIE p.446).

**Context parallelism** splits the input sequence itself across devices (e.g. first half on machine 1, second half on machine 2). **Sequence parallelism** splits the operators needed across the whole input across machines (e.g. attention on machine 1, feedforward on machine 2). Both target efficient processing of long input sequences (AIE p.446).

## Key figures
None.

## Examples
- Replica parallelism -- multiple full model copies serving requests concurrently (AIE p.444)
- Tensor parallelism -- columnwise split of a matrix multiplication across devices (AIE p.445)
- Pipeline parallelism -- four-machine staged execution with micro-batches (AIE p.446)

## Related
- [[prefill-and-decode]]  (see-also: disaggregating prefill and decode onto separate instances is a related service-level parallelism decision)
- [[inference-latency]]  (boundary: tensor and pipeline parallelism both add communication overhead that can offset their throughput/capacity benefits)
- [[gpu]]  (prerequisite: parallelism strategies distribute computation across multiple accelerator chips)

## Provenance
- [[sources/ch09-inference-service-optimization]]
