---
type: concept
sources: [ch02-model-size]
---
# Scaling Law (Chinchilla)

The Chinchilla scaling law, from 'Training Compute-Optimal Large Language Models' (DeepMind, 2022), gives a rule for calculating the optimal model size and dataset size given a fixed compute budget -- a model achieving the best performance for its compute budget is called compute-optimal (AIE p.71-72). Training 400 language models from 70 million to over 16 billion parameters on 5-500 billion tokens, the authors found that compute-optimal training needs training tokens to be approximately 20 times the model's parameter count, and that model size and training tokens should scale equally: doubling model size means doubling training tokens (AIE p.72).

This calculation assumes [[data-acquisition]] is much cheaper than compute; the Chinchilla paper proposes a separate calculation for when training-data cost is nontrivial. The scaling law was derived for dense models trained mostly on human-generated data -- adapting it to sparse models (e.g. [[mixture-of-experts]]) and to synthetic data is an active research area (AIE p.72). The law also optimizes for model quality alone, not production usability: Llama's authors chose smaller, suboptimal-performance models over what their compute budget could have bought, because smaller models are cheaper to run and easier to adopt; Sardana et al. (2023) modified the Chinchilla law to account for this inference-cost tradeoff (AIE p.72).

Diminishing returns compound: the cost of achieving a given model performance falls over time (cost for 93% ImageNet accuracy halved from 2019 to 2021), but the cost of *improving* performance further stays high -- going from 90% to 95% accuracy is more expensive than 85% to 90%, and a model with a 2% error rate may need an order of magnitude more data, compute, or energy than one with a 3% error rate (AIE p.73). In language modeling, dropping cross-entropy loss from about 3.4 to 2.8 nats requires 10 times more training data (AIE p.73).

## Key figures
- Compute-optimal training tokens ~= 20x parameter count (AIE p.72)
- 400 models trained, 70 million to 16+ billion parameters, on 5-500 billion tokens (AIE p.72)
- Cost to reach 93% ImageNet accuracy halved from 2019 to 2021 (AIE p.73)
- Dropping cross-entropy loss from 3.4 to 2.8 nats requires 10x more training data (AIE p.73)

## Related
- [[model-size]]  (prerequisite: scaling law relates model size to dataset size and compute)
- [[dataset-size]]  (prerequisite: derives the compute-optimal ratio of training tokens to parameters)
- [[flop]]  (prerequisite: compute budget is expressed in FLOPs)
- [[mixture-of-experts]]  (boundary: law was derived for dense models; sparse-model adaptation is an open research area)
- [[llama-2]]  (contrast: Llama's authors chose smaller, less compute-optimal models for better usability)
- [[scaling-extrapolation]]  (see-also: both address how to make good decisions about large-model training in advance)
- [[data-acquisition]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-model-size]]
