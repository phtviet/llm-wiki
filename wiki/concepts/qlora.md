---
type: concept
sources: [ch07-parameter-efficient-finetuning]
---
# QLoRA

QLoRA (Dettmers et al., 2023) is a quantized variant of [[lora]]: rather than storing model weights in 16 bits as in the original LoRA paper, QLoRA stores them in 4 bits and dequantizes them back to BF16 when computing the forward and backward pass (AIE p.346). It uses the NF4 (NormalFloat-4) format, which quantizes values based on the insight that pre-trained weights typically follow a normal distribution centered at zero, plus paged optimizers that automatically move data between CPU and GPU when GPU memory runs out, especially with long sequences (AIE p.346).

These techniques let a 65B-parameter model be finetuned on a single 48 GB GPU. The authors finetuned Llama models from 7B to 65B in 4-bit mode, producing the Guanaco model family, which showed competitive performance on public benchmarks and in comparative evaluation against GPT-4 and ChatGPT (AIE p.346). QLoRA's main limitation is that NF4 quantization is computationally expensive, so it can increase training time despite reducing memory (AIE p.346-347).

## Key figures
- 65B-parameter model finetunable on a single 48 GB GPU using 4-bit NF4 quantization plus paged optimizers (AIE p.346)
- Guanaco 65B: 41 GB, Elo 1022 vs. GPT-4's 1348 and ChatGPT's 966, as judged by GPT-4 in May 2023 (AIE p.346)
- Guanaco 33B: 21 GB, Elo 992; Guanaco 13B: 10 GB, Elo 916; Guanaco 7B: 6 GB, Elo 879 (AIE p.346)

## Related
- [[lora]] (example-of: QLoRA is a quantized version of LoRA)
- [[quantization]] (example-of: QLoRA applies quantization specifically to a LoRA-finetuned model's weights)
- [[ai-as-a-judge]] (example-of: Guanaco's Elo ratings were produced using GPT-4 as a comparative judge)

## Provenance
- [[sources/ch07-parameter-efficient-finetuning]]
