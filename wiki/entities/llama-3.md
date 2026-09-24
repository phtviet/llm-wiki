---
type: entity
sources: [ch02-model-architecture]
---
# Llama 3

Llama 3 (Dubey et al., 2024) is a successor family to [[llama-2]], used alongside it in the book's table of transformer dimension values. Compared to Llama 2, Llama 3 models keep similar model and feedforward dimensions at equivalent depths but expand vocabulary size fourfold and [[context-length]] thirtytwofold (AIE p.64). Increased context length affects a model's memory footprint but not its total parameter count (AIE p.64).

## Key figures
- Llama 3-7B: 32 transformer blocks, model dim 4,096, feedforward dim 14,336, vocab size 128K, context length 128K (AIE p.64)
- Llama 3-70B: 80 transformer blocks, model dim 8,192, feedforward dim 28,672, vocab size 128K, context length 128K (AIE p.64)
- Llama 3-405B: 126 transformer blocks, model dim 16,384, feedforward dim 53,248, vocab size 128K, context length 128K (AIE p.64)

## Related
- [[llama-2]]  (contrast: predecessor family with smaller vocabulary and much shorter context length)
- [[transformer-block]]  (example-of: Llama 3's dimensions illustrate block-dimension scaling)
- [[context-length]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-model-architecture]]
