---
type: entity
sources: [ch02-model-architecture]
---
# Llama 2

Llama 2 (Touvron et al., 2023) is a family of open transformer-based language models used in the book to illustrate how [[transformer-block]] dimension values determine [[model-size]]. Llama 2-7B has a hidden dimension of 4096 and 32 attention heads, giving each of its key/query/value matrices dimension 4096x4096 and each attention head a dimension of 128 (AIE p.61, p.63-64).

## Key figures
- Llama 2-7B: 32 transformer blocks, model dim 4,096, feedforward dim 11,008, vocab size 32K, [[context-length]] 4K (AIE p.64)
- Llama 2-13B: 40 transformer blocks, model dim 5,120, feedforward dim 13,824, vocab size 32K, context length 4K (AIE p.64)
- Llama 2-70B: 80 transformer blocks, model dim 8,192, feedforward dim 22,016, vocab size 32K, context length 4K (AIE p.64)

## Related
- [[transformer-block]]  (example-of: Llama 2's dimensions illustrate how block dimension values set model size)
- [[llama-3]]  (contrast: successor family with larger vocabulary and much longer context length at comparable depths)
- [[context-length]]  (see-also: mentioned in this page's text)
- [[model-size]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-model-architecture]]
