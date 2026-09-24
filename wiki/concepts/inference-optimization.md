---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Inference Optimization

Inference optimization means making models faster and cheaper to run (AIE p.43). It has always mattered in ML engineering, but foundation models' higher inference cost and latency make it even more important in AI engineering (AIE p.43).

A specific challenge is that many foundation models are autoregressive, generating tokens sequentially: if a model takes 10 ms per token, a 100-token output takes a second, and longer outputs take proportionally longer. Getting AI application latency down to the roughly 100 ms expected of a typical internet application is a major challenge, and inference optimization has become an active subfield in both industry and academia (AIE p.43). Techniques discussed elsewhere in the book include [[quantization]], [[model-distillation]], and parallelism.

## Key figures
- A model generating tokens at 10 ms/token takes about a second to produce 100 tokens (AIE p.43)

## Related
- [[model-development]]  (part-of: one of the three main responsibilities of model development)
- [[dataset-engineering]]  (see-also: sibling responsibility within model development)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
