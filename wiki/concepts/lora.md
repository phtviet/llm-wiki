---
type: concept
sources: [ch07-parameter-efficient-finetuning]
---
# LoRA (Low-Rank Adaptation)

LoRA (Hu et al., 2021) is an adapter-based [[peft]] technique that, unlike the original Houlsby et al. adapter method, adds no extra inference latency: instead of inserting new layers, it decomposes a weight matrix into two smaller matrices that can be merged back into the original layer (AIE p.338).

Given a weight matrix W of dimension n x m, LoRA chooses a rank r, constructs matrices A (n x r) and B (r x m), and adds their product WAB to W to form a new matrix W' = W + (alpha/r) x WAB, where alpha is a hyperparameter controlling WAB's contribution. During finetuning, only A and B are updated; W stays intact (AIE p.339). This rests on low-rank factorization: a large matrix is approximated as the product of two smaller ones, cutting parameter count (e.g. a 9x9 matrix's 81 parameters shrink to 18 across two 9x1/1x9 factors), at the cost of lossy approximation whose fidelity improves with higher rank (AIE p.339-340).

LoRA is applied most commonly to the four attention-module weight matrices -- query (Wq), key (Wk), value (Wv), and output projection (Wo) -- uniformly across all matrices of the same type in the model (AIE p.341-342). Under a fixed trainable-parameter budget, Hu et al. (2021) found applying rank-2 LoRA to all four matrices gave the best results on WikiSQL and MultiNLI, though if only two matrices can be chosen, query and value generally perform best (AIE p.342). Empirically, small ranks (r between 4 and 64) are usually sufficient, and increasing r does not reliably improve performance and can even cause overfitting, though Raschka (2023) found r=256 best for his tasks; applying LoRA to feedforward matrices as well as attention matrices, as Databricks found, can yield the biggest performance boost (AIE p.343).

Why LoRA works ties to the finding that LLMs have low intrinsic dimension after pre-training, larger models having even lower intrinsic dimension, suggesting pre-training itself acts as a compression framework that makes small-parameter, small-data finetuning sufficient (AIE p.340). Low-rank pre-training (training a factorized model from scratch, e.g. ReLoRA up to 1.3B parameters and GaLore at 1B-7B parameters) remains an open research direction, since full-rank pre-training may still be needed to sufficiently reduce intrinsic dimension before low-rank training can work (AIE p.340-341).

LoRA's main drawback is weaker performance than full finetuning, and applying it requires understanding the target model's architecture (AIE p.345). LoRA adapters are modular: they can be merged into the base model before serving (no added latency, best for single-model serving) or kept separate and merged at inference time (adds latency, but enables multi-LoRA serving of many finetuned variants sharing one base model, at far less storage) (AIE p.343-344).

## Key figures
- GPT-3: comparable or better performance than full finetuning using ~4.7M trainable parameters, 0.0027% of full finetuning (AIE p.340)
- GPT-3 175B finetuning budget of 18M trainable parameters (0.01% of total): rank-2 LoRA on all four attention matrices = (12,288 x 2 x 2) x 4 = 196,608 parameters/layer, 18,874,368 total across 96 layers (AIE p.342)
- WikiSQL/MultiNLI at 18M-parameter budget: all four matrices at rank 2 reach 73.7% WikiSQL / 91.7% MultiNLI, the best combination tested (AIE p.342)
- SqueezeNet reaches AlexNet-level ImageNet accuracy using 50x fewer parameters via factorization strategies (AIE p.340)
- Example matrix: 4096x4096 (16.8M parameters) base matrix; rank-8 LoRA adds 4096x8x2 = 65,536 parameters; 100-customer multi-LoRA serving needs 16.8M + 65,536x100 = 23.3M parameters vs. 1.68B for 100 separately merged models (AIE p.344)
- Typical alpha:r ratio between 1:8 and 8:1 (AIE p.343)

## Examples
- [[qlora]] (quantized variant storing weights in 4-bit NF4)

## Related
- [[peft]] (part-of: LoRA is the dominant adapter-based PEFT technique)
- [[adam-optimizer]] (see-also: full finetuning's optimizer whose memory cost LoRA's parameter efficiency avoids)
- [[quantization]] (prerequisite: QLoRA combines LoRA with quantization of model weights)
- [[alexnet]] (example-of: SqueezeNet's low-rank factorization matches AlexNet-level accuracy with 50x fewer parameters)
- [[model-merging]] (see-also: LoRA-adapter merging back into base weights parallels, but is distinct from, merging separate whole models)

## Provenance
- [[sources/ch07-parameter-efficient-finetuning]]
