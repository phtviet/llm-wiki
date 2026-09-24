---
type: concept
sources: [ch07-quantization]
---
# Quantization-Aware Training (QAT)

Quantization-aware training (QAT) aims to produce a model with high quality when run in low precision at inference. During QAT, the model simulates low-precision (e.g., 8-bit) behavior while training, letting it learn to produce high-quality outputs once actually quantized (AIE p.331). This addresses the risk that [[post-training|post-training]] quantization degrades a model's quality.

QAT does not reduce training time or cost, since its computations still run in high precision during training -- and it can even increase training time due to the overhead of simulating low-precision behavior (AIE p.331). This contrasts with training a model directly in lower precision (e.g., via [[mixed-precision-training]]), which can both improve inference quality in low precision and reduce training time and cost, though it is harder to do since backpropagation is more sensitive to reduced precision (AIE p.331). An example combining sensitivity-aware precision choices is LLM-QAT (Liu et al., 2023), which quantizes weights and activations to 4 bits but keeps embeddings in 16 bits (AIE p.331).

## Key figures
None.

## Related
- [[quantization]]  (part-of: QAT is one training-time quantization technique, distinct from post-training quantization)
- [[mixed-precision-training]]  (contrast: QAT simulates low precision while training in high precision, vs. mixed precision which actually computes some values in lower precision during training)
- [[backpropagation]]  (boundary: backpropagation is more sensitive to lower precision, which is why direct low-precision training is harder than QAT)
- [[post-training]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch07-quantization]]
