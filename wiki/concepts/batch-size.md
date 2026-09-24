---
type: concept
sources: [ch07-finetuning-tactics]
---
# Batch Size

Batch size determines how many examples a model learns from in each step before updating its weights. Batch sizes smaller than eight can lead to unstable training, since a larger batch aggregates signal across more examples for more stable and reliable updates. Larger batches let a model move through training examples faster but require more memory, so batch size is ultimately limited by available hardware -- a cost-versus-efficiency trade-off where more expensive compute permits faster finetuning (AIE p.360).

Because compute is often a bottleneck, models are frequently constrained to small batch sizes, which can destabilize weight updates. [[gradient-accumulation]] addresses this by accumulating gradients across several batches before updating weights, rather than updating after every batch (AIE p.360).

## Key figures
- Batch sizes below eight can cause unstable training (AIE p.360)

## Related
- [[finetuning-hyperparameters]]  (part-of: one of the frequently tuned finetuning hyperparameters)
- [[gradient-accumulation]]  (prerequisite: small batch sizes forced by memory constraints motivate gradient accumulation)
- [[learning-rate]]  (see-also: both are core training hyperparameters)

## Provenance
- [[sources/ch07-finetuning-tactics]]
