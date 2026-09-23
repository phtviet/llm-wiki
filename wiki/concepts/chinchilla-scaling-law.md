---
type: concept
sources: [ch02-model-size]
---
# Chinchilla Scaling Law

The Chinchilla scaling law, proposed in "Training Compute-Optimal Large Language Models" (DeepMind, 2022), is the rule for calculating the optimal model size and dataset size given a fixed compute budget — a model achieving the best performance under that budget is called compute-optimal (AIE p.72). The DeepMind authors trained 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens to derive it (AIE p.72).

The law's key finding: for compute-optimal training, the number of training tokens should be approximately 20 times the model's parameter count, and model size and training tokens should scale together — doubling one requires doubling the other (AIE p.72). The law was developed for dense models trained predominantly on human-generated data; adapting it to sparse models like [[mixture-of-experts]] and to synthetic data is an active research area (AIE p.72).

The scaling law optimizes for model quality given a compute budget, but production systems value more than quality alone: Llama's authors chose smaller, suboptimal-for-compute models over bigger ones because smaller models are cheaper to run and easier to adopt, prioritizing usability over raw quality-per-compute (AIE p.72). Sardana et al. (2023) modified the Chinchilla law to account for this inference-time cost when calculating optimal parameter count and pre-training data size (AIE p.72).

## Key figures
- Trained 400 models from 70 million to over 16 billion parameters, on 5 to 500 billion tokens, to derive the law (AIE p.72)
- Compute-optimal training needs training tokens ≈ 20× the parameter count (e.g., a 3B-parameter model needs ~60B training tokens) (AIE p.72)

## Examples
- [[llama-2]]

## Related
- [[model-size]]  (prerequisite: the law defines the compute-optimal trade-off between parameter count and dataset size)
- [[training-tokens]]  (part-of: the law's core ratio is expressed as training tokens per parameter)
- [[flop]]  (prerequisite: the law operates under a fixed FLOP compute budget)
- [[mixture-of-experts]]  (boundary: the law was derived for dense models; extending it to sparse MoE models is still open research)

## Provenance
- [[sources/ch02-model-size]]
