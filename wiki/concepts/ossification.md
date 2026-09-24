---
type: concept
sources: [ch08-data-quantity]
---
# Ossification

Ossification is a phenomenon in which pre-training freezes a model's weights so that they do not adapt well to finetuning data, making finetuning worse than training from scratch in some cases -- particularly when a large amount of finetuning data is available (Hernandez et al., 2021) (AIE p.372). Smaller models are more susceptible to ossification than larger models (AIE p.372).

Ossification is a key reason to evaluate whether training a model from scratch would outperform finetuning when very large amounts of task-specific data are available, since finetuning on top of a pre-trained model is normally more efficient (AIE p.372).

## Key figures
None.

## Related
- [[data-quantity]]  (part-of: a data-volume consideration that argues against finetuning when a lot of data is available)
- [[finetuning]]  (boundary: marks a case where finetuning underperforms training from scratch)
- [[pre-training]]  (prerequisite: ossification arises from the pre-training phase's effect on weights)

## Provenance
- [[sources/ch08-data-quantity]]
