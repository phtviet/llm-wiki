---
type: concept
sources: [ch02-model-size]
---
# Mixture-of-Experts (MoE)

Mixture-of-experts (MoE) is a type of sparse model architecture that has gained popularity in recent years (Shazeer et al., 2017). An MoE model is divided into groups of parameters called experts, and only a subset of experts is active to process each token, making the model's cost and speed comparable to a much smaller dense model despite its larger total parameter count (AIE p.68).

A [[sparse-models|sparse model]] more generally has a large percentage of zero-value parameters, which allows for more efficient data storage and computation, meaning a large sparse model can require less compute than a small dense model (AIE p.68). The Chinchilla scaling law was developed for dense models trained on predominantly human-generated data; adapting it for sparse MoE models and synthetic data remains an active research area (AIE p.72).

## Key figures
- Mixtral 8x7B: 8 experts of 7 billion parameters each; would be 56 billion parameters if no sharing occurred, but has 46.7 billion parameters due to shared parameters (AIE p.68)
- Only two experts active per token in Mixtral 8x7B, giving 12.9 billion active parameters per token, matching the cost/speed of a 12.9B-parameter model despite 46.7B total parameters (AIE p.68)

## Examples
- [[mixtral-8x7b]]

## Related
- [[model-size]]  (boundary: parameter count is misleading for sparse MoE models since only a subset of parameters is active per token)
- [[chinchilla-scaling-law]]  (boundary: the scaling law was developed for dense models; adapting it to sparse MoE models is still an open research question)

## Provenance
- [[sources/ch02-model-size]]
