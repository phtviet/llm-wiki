---
type: entity
sources: [ch07-quantization]
---
# BitNet b1.58

BitNet b1.58 is a transformer-based [[language-model]] introduced by Microsoft researchers (Ma et al., 2024), requiring only 1.58 bits per parameter. The authors framed it as marking the start of an era of 1-bit LLMs (AIE p.329). Its performance is comparable to 16-bit Llama 2 (Touvron et al., 2023) up to 3.9B parameters, benchmarked across ARCe, ARCc, HellaSwag, BoolQ, OpenBookQA, PIQA, and WinoGrande (AIE p.329).

It follows earlier 1-bit representation attempts such as BinaryConnect (Courbariaux et al., 2015), Xnor-Net (Rastegari et al., 2016), and BitNet (Wang et al., 2023) (AIE p.329).

## Key figures
- Requires 1.58 bits per parameter (AIE p.329)
- At 3.9B parameters, BitNet b1.58 scores an average of 51.2 across seven benchmarks, versus Llama 2 16-bit's 49.7 average at 3B parameters (AIE p.329)
- At 700M, 1.3B, and 3B parameter sizes, BitNet b1.58's average benchmark scores (44.3, 45.4, 50.2) track closely with Llama 2 16-bit's (45.5, 46.2, 49.7) (AIE p.329)

## Related
- [[quantization]]  (example-of: an extreme, 1-bit-scale case of precision reduction)
- [[llama-2]]  (contrast: BitNet b1.58 is benchmarked directly against Llama 2 16-bit at matched parameter sizes)
- [[language-model]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch07-quantization]]
