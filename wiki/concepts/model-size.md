---
type: concept
sources: [ch02-model-size]
---
# Model Size

Model size is most commonly measured by [[model-parameters]]: the number of parameters is usually appended to a model's name (e.g. Llama-13B), and increasing a model's parameter count generally increases its capacity to learn, so within a model family more parameters tends to mean better performance (AIE p.67). Newer-generation models can outperform older, larger ones of the same size class: Llama 3-8B (2024) outperforms [[llama-2]]-70B (2023) on MMLU (AIE p.67).

Parameter count can mislead when a model is sparse. A sparse model has a large percentage of zero-value parameters, so a 7B-parameter model that is 90% sparse has only 700 million non-zero parameters; sparsity allows more efficient storage and computation, so a large sparse model can require less compute than a small dense model (AIE p.68). [[mixture-of-experts]] is the popular sparse architecture the book uses to illustrate this.

A larger model can also underperform a smaller one if it is not trained on enough data, which is why model size must be considered alongside dataset size: three numbers together signal a model's scale -- number of parameters (learning capacity), number of training tokens (how much the model learned), and number of FLOPs (training cost) (AIE p.68, p.71).

## Key figures
- A 7B-parameter model at 90% sparsity has only 700 million non-zero parameters (AIE p.68)

## Related
- [[model-parameters]]  (prerequisite: parameter count is the base unit model size is measured in)
- [[mixture-of-experts]]  (example-of: sparse architecture that decouples parameter count from compute cost)
- [[dataset-size]]  (see-also: model size must be considered jointly with the size of training data)
- [[scaling-law]]  (prerequisite: relates model size to dataset size and compute budget)
- [[flop]]  (see-also: third of the three numbers, alongside parameters and tokens, that signal a model's scale)
- [[llama-2]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-model-size]]
