---
type: concept
sources: [ch02-model-size]
---
# Mixture-of-Experts (MoE)

Mixture-of-experts is a type of sparse model architecture that has gained popularity in recent years (Shazeer et al., 2017). An MoE model is divided into groups of parameters called experts, and only a subset of experts is active to process each token (AIE p.68). Because only a fraction of parameters are active per token, an MoE model's inference cost and speed can match a much smaller dense model despite having a far larger total parameter count (AIE p.68).

## Key figures
None. The concept carries no intrinsic load-bearing figure of its own; [[mixtral-8x7b]]'s figures (56B nominal / 46.7B actual / 12.9B active parameters) are entity-specific and live on its page.

## Examples
- [[mixtral-8x7b]]  (eight 7B experts, two active per token)

## Related
- [[model-size]]  (part-of: MoE is the architecture the book uses to show parameter count can mislead about compute cost)
- [[mixtral-8x7b]]  (example-of: canonical MoE model in this section)
- [[scaling-law]]  (boundary: the Chinchilla scaling law was developed for dense models; adapting it to sparse MoE models is an active research area)

## Provenance
- [[sources/ch02-model-size]]
