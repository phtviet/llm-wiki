---
type: concept
sources: [ch02-model-size]
---
# Model Size

Model size refers to a foundation model's number of parameters, usually appended to its name (e.g., Llama-13B). Increasing a model's parameter count generally increases its capacity to learn, and a larger model within the same family typically outperforms a smaller one (AIE p.67). However, newer-generation models tend to outperform older, same-sized ones as training techniques improve: Llama 3-8B (2024) outperforms Llama 2-70B (2023) on MMLU despite far fewer parameters (AIE p.67).

Parameter count also estimates compute needs: a 7-billion-parameter model stored at 2 bytes per parameter needs at least 14 GB of GPU memory for inference (AIE p.67). Parameter count can mislead for [[sparse-models]], where many parameters are zero-valued, so raw counts overstate effective compute (AIE p.68).

A larger model can still underperform a smaller one if undertrained relative to its size, which is why dataset size (measured in tokens, see [[training-tokens]]) must be considered alongside parameter count (AIE p.68). Three numbers together signal a model's scale: number of parameters (learning capacity), number of training tokens (how much it learned), and number of [[flop]] (training cost) (AIE p.71).

## Key figures
- 7B parameters at 2 bytes/parameter requires at least 14 GB GPU memory for inference (AIE p.67)
- Llama 3-8B (2024) outperforms Llama 2-70B (2023) on the MMLU benchmark (AIE p.67)

## Examples
- [[llama-2]]
- [[llama-3]]
- [[mixture-of-experts]]

## Related
- [[training-tokens]]  (prerequisite: dataset size measured in tokens must be considered alongside parameter count to judge a model's true capability)
- [[flop]]  (part-of: FLOPs form the third of the three numbers, alongside parameters and tokens, that signal model scale)
- [[chinchilla-scaling-law]]  (prerequisite: scaling law determines the compute-optimal ratio of model size to dataset size)
- [[mixture-of-experts]]  (boundary: parameter count is misleading for sparse MoE models since only a subset of parameters is active per token)

## Provenance
- [[sources/ch02-model-size]]
