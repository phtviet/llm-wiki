---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Inference Optimization

Inference optimization means making models faster and cheaper to run; it is one of the three main responsibilities of [[model-development]] and has always mattered for ML engineering, but matters even more with foundation models because of their higher cost and latency at scale (AIE p.43). A core challenge is that many foundation models are autoregressive, generating tokens sequentially: at 10 ms per token, a 100-token output takes a full second, and longer outputs take proportionally longer. Getting AI application latency down to the ~100 ms expected of a typical internet application is a major challenge, making inference optimization an active subfield in both industry and academia (AIE p.43).

Inference optimization techniques include [[quantization]], [[model-distillation]], and parallelism (AIE p.43).

## Key figures
- At 10 ms per token, generating 100 tokens takes about 1 second (AIE p.43)

## Related
- [[model-development]]  (part-of: one of model development's three main responsibilities)
- [[model-distillation]]  (example-of: one inference optimization technique)
- [[quantization]]  (example-of: one inference optimization technique)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
