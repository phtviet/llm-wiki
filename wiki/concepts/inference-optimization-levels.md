---
type: concept
sources: [ch09-inference-optimization-2]
---
# Inference Optimization Levels

Inference optimization can be done at three levels: model, hardware, and service. The book uses an archery analogy: model-level optimization is like crafting better arrows, hardware-level optimization is like training a stronger and better archer, and service-level optimization is like refining the entire shooting process, including the bow and aiming conditions (AIE p.426).

Ideally, optimizing a model for speed and cost should not change its quality, but many optimization techniques can cause model degradation. An experiment by Cerebras (2024) showed the same Llama models achieving different benchmark performance when served by different inference service providers, since providers may apply optimization techniques that alter model behavior (AIE p.426). Because hardware design is outside the book's scope, only model-level and service-level techniques are discussed further; in production, optimization typically combines techniques from more than one level (AIE p.426).

## Key figures
None.

## Related
- [[model-distillation]]  (see-also: distillation and quantization are model-level compression techniques that fall under this optimization framing)
- [[quantization]]  (see-also: quantization is a model-level inference-optimization technique)

## Provenance
- [[sources/ch09-inference-optimization-2]]
