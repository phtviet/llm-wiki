---
type: concept
sources: [ch07-backpropagation-and-trainable-parameters]
---
# Trainable Parameters

A trainable parameter is a parameter that can be updated during finetuning; parameters kept unchanged are called frozen parameters. The number of trainable parameters is a key factor determining a model's memory footprint during finetuning (AIE p.320).

Update behavior differs by training phase: during [[pre-training|pre-training]], all model parameters are updated; during inference, no parameters are updated; during finetuning, some or all parameters may be updated (AIE p.320). If a parameter is not trainable, it needs no gradient computed for it, since there's nothing to update (AIE p.320).

Each trainable parameter carries additional memory overhead beyond its own value: a gradient and optimizer states, computed and stored during the backward pass of [[backpropagation]]. More trainable parameters therefore mean more memory needed during training (AIE p.321).

## Key figures
None.

## Related
- [[backpropagation]]  (prerequisite: backpropagation is the mechanism that computes gradients for and updates trainable parameters)
- [[finetuning]]  (part-of: which parameters are trainable vs. frozen is decided during finetuning)
- [[model-parameters]]  (part-of: trainable parameters are the subset of a model's parameters eligible for update)
- [[pre-training]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch07-backpropagation-and-trainable-parameters]]
