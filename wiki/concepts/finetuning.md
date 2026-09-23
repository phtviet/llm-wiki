---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Finetuning

Finetuning means continuing to train a previously trained model: weights start from a prior training run rather than random initialization (AIE p.42). Because the model already carries knowledge from [[pre-training]], finetuning typically requires fewer resources (data and compute) than pre-training (AIE p.42). It is a [[model-adaptation]] technique that, unlike [[prompt-engineering]], requires updating model weights; it is more complicated and data-hungry, but can significantly improve a model's quality, latency, and cost, and can adapt a model to tasks it wasn't exposed to during training (AIE p.40).

Finetuning and [[post-training]] are conceptually the same process — continuing training after pre-training — but the terms are sometimes used to signal who performs it: model developers typically call it post-training (e.g., OpenAI making a model better at following instructions before release), while application developers call it finetuning (e.g., finetuning an already post-trained OpenAI model to their own needs) (AIE p.42).

## Key figures
None.

## Examples
- [[alpaca]]  (finetuned from a pre-trained Llama-7B on teacher-generated outputs)

## Related
- [[model-adaptation]]  (part-of: the weight-updating adaptation category)
- [[prompt-engineering]]  (contrast: adapts by updating weights vs. adapts via input/context only)
- [[pre-training]]  (prerequisite: finetuning continues training from a pre-trained model's weights)
- [[post-training]]  (see-also: conceptually the same process, distinguished mainly by who performs it and why)
- [[model-distillation]]  (boundary: a distilled student may be finetuned from a pre-trained model, like Alpaca, but distillation specifically trains on a teacher's generated outputs)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
