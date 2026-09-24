---
type: concept
sources: [ch02-model-size]
---
# Scaling Extrapolation

Scaling extrapolation (also called hyperparameter transferring) is a research subfield that tries to predict, for a large model, what hyperparameters will give the best performance, since large models are usually too expensive to train more than once to search hyperparameters directly (AIE p.74). The approach studies how hyperparameters affect models much smaller than the target size, then extrapolates the results upward; a 2022 Microsoft/OpenAI paper showed hyperparameters could be transferred from a 40M model to a 6.7B model (AIE p.74).

The technique remains a niche topic, both because few people have the resources to study large-model training and because of the sheer number of hyperparameters and their interactions -- ten hyperparameters would require studying 1,024 combinations (AIE p.74). Emergent abilities, capabilities only present at scale and not observable in smaller models (Wei et al., 2022), make extrapolation less accurate (AIE p.74).

A [[model-parameters|parameter]] is distinguished from a hyperparameter: a parameter is learned during training, while a hyperparameter (e.g. number of layers, model dimension, vocabulary size, batch size, epochs, [[learning-rate]]) is set by users to configure the model and control how it learns (AIE p.74).

## Key figures
- Hyperparameters transferred from a 40M model to a 6.7B model (Microsoft/OpenAI, 2022) (AIE p.74)
- Ten hyperparameters implies 1,024 combinations to study exhaustively (AIE p.74)

## Related
- [[scaling-law]]  (see-also: both are tools for planning large, expensive training runs in advance)
- [[model-parameters]]  (contrast: parameters are learned; hyperparameters are set by users)
- [[learning-rate]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-model-size]]
