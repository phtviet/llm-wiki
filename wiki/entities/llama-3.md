---
type: entity
sources: [ch02-model-architecture]
---
# Llama 3

Llama 3 (Dubey et al., 2024) is a family of transformer-based language models from Meta, presented in the book alongside Llama 2 to show how dimension values scale across model sizes and generations, including a much larger vocabulary and context length than Llama 2 (AIE p.64).

## Key figures
- Llama 3-7B: 32 transformer blocks, model dimension 4,096, feedforward dimension 14,336, vocab size 128K, context length 128K (AIE p.64)
- Llama 3-70B: 80 transformer blocks, model dimension 8,192, feedforward dimension 28,672, vocab size 128K, context length 128K (AIE p.64)
- Llama 3-405B: 126 transformer blocks, model dimension 16,384, feedforward dimension 53,248, vocab size 128K, context length 128K (AIE p.64)

## Related
- [[llama-2]]  (contrast: predecessor family with smaller vocabulary and much shorter context length)
- [[transformer-architecture]]  (example-of: worked example used to illustrate transformer dimension sizing)

## Provenance
- [[sources/ch02-model-architecture]]
