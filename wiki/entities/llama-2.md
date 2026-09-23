---
type: entity
sources: [ch02-model-architecture]
---
# Llama 2

Llama 2 (Touvron et al., 2023) is a family of transformer-based language models from Meta used in the book as the worked example for transformer dimension sizing, spanning 7B, 13B, and 70B parameter variants (AIE p.61-64).

## Key figures
- Llama 2-7B: 32 transformer blocks, model dimension 4,096, feedforward dimension 11,008, vocab size 32K, context length 4K (AIE p.64)
- Llama 2-13B: 40 transformer blocks, model dimension 5,120, feedforward dimension 13,824, vocab size 32K, context length 4K (AIE p.64)
- Llama 2-70B: 80 transformer blocks, model dimension 8,192, feedforward dimension 22,016, vocab size 32K, context length 4K (AIE p.64)
- Llama 2-7B's hidden dimension of 4,096 gives 4,096 x 4,096 query/key/value matrices; with 32 attention heads, each K/V/Q vector splits into 32 vectors of dimension 128 (AIE p.61)

## Related
- [[llama-3]]  (contrast: successor family with larger vocabulary and much longer context length at comparable layer counts)
- [[transformer-architecture]]  (example-of: worked example used to illustrate transformer dimension sizing)

## Provenance
- [[sources/ch02-model-architecture]]
