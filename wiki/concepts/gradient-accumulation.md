---
type: concept
sources: [ch07-finetuning-tactics]
---
# Gradient Accumulation

Gradient accumulation is a technique for handling small, compute-constrained batch sizes: instead of updating model weights after every batch, gradients are accumulated across several batches and the weights are updated once enough reliable gradients have built up. This reduces the instability that comes from updating on too-small batches when memory limits prevent larger ones (AIE p.360).

## Key figures
None.

## Related
- [[batch-size]]  (prerequisite: motivated by the instability of small batch sizes forced by memory limits)
- [[finetuning-hyperparameters]]  (part-of: a technique for managing the batch-size hyperparameter's practical constraints)

## Provenance
- [[sources/ch07-finetuning-tactics]]
