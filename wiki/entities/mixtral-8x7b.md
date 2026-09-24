---
type: entity
sources: [ch02-model-size]
---
# Mixtral 8x7B

Mixtral 8x7B is a [[mixture-of-experts]] model made of eight experts, each with seven billion parameters. If no parameters were shared between experts it would have 8 x 7 billion = 56 billion parameters, but due to parameter sharing it has only 46.7 billion parameters (AIE p.68). At each layer, for each token, only two of the eight experts are active, so only 12.9 billion parameters are active per token -- meaning the model's cost and speed match a 12.9-billion-parameter dense model despite its larger total size (AIE p.68).

## Key figures
- Nominal 8 x 7B = 56 billion parameters if experts shared nothing (AIE p.68)
- Actual total: 46.7 billion parameters, due to parameter sharing (AIE p.68)
- 12.9 billion parameters active per token (two of eight experts active per layer) (AIE p.68)

## Related
- [[mixture-of-experts]]  (example-of: canonical MoE model illustrating sparse-vs-active parameter counts)

## Provenance
- [[sources/ch02-model-size]]
