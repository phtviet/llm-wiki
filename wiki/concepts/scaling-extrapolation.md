---
type: concept
sources: [ch02-model-size]
---
# Scaling Extrapolation

Scaling extrapolation (also called hyperparameter transferring) is a research subfield that tries to predict, for large models, which hyperparameters will give the best performance, since training a large model multiple times to search hyperparameters directly is rarely feasible (AIE p.74). The approach studies how hyperparameters affect models much smaller than the target size, then extrapolates the findings to the target scale (AIE p.74). A 2022 paper by Microsoft and OpenAI showed hyperparameters could be transferred from a 40M-parameter model to a 6.7B-parameter model (AIE p.74).

This differs from a model **parameter**, which is learned during training, versus a **hyperparameter**, which is set by users to configure the model (e.g., number of layers, model dimension, vocabulary size) or control how it learns (e.g., batch size, epochs, learning rate) (AIE p.74).

Extrapolation is difficult because of the sheer number of hyperparameters and their interactions — ten hyperparameters implies 1,024 possible combinations to study — and because emergent abilities (Wei et al., 2022), present only at scale, make smaller-model behavior a less reliable predictor of large-model behavior (AIE p.74-75).

## Key figures
- Hyperparameters successfully transferred from a 40M-parameter model to a 6.7B-parameter model (AIE p.74)
- Ten hyperparameters implies 1,024 combinations to study exhaustively (AIE p.75)

## Examples
- None

## Related
- [[model-size]]  (prerequisite: extrapolation is needed because large-model hyperparameter search is infeasible at scale)
- [[chinchilla-scaling-law]]  (contrast: scaling law predicts optimal size/data trade-off, whereas scaling extrapolation predicts optimal hyperparameters)

## Provenance
- [[sources/ch02-model-size]]
