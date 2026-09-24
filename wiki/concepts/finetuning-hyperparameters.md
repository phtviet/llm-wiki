---
type: concept
sources: [ch07-finetuning-tactics]
---
# Finetuning Hyperparameters

Many hyperparameters can be tuned to improve finetuning efficiency; the specific set depends on the base model and finetuning method, but several recur across projects: [[learning-rate]], [[batch-size]], [[gradient-accumulation]], number of [[epoch|epochs]], and [[prompt-loss-weight]] (AIE p.359).

## Key figures
None.

## Examples
- [[learning-rate]]
- [[batch-size]]
- [[gradient-accumulation]]
- [[epoch]]
- [[prompt-loss-weight]]

## Related
- [[finetuning]]  (part-of: hyperparameters govern how a finetuning run executes)
- [[backpropagation]]  (prerequisite: hyperparameters like learning rate and batch size shape how backpropagation's gradient updates are applied)

## Provenance
- [[sources/ch07-finetuning-tactics]]
