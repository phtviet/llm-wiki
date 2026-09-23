---
type: entity
sources: [ch02-model-size]
---
# Mixtral 8x7B

Mixtral 8x7B is a mixture-of-experts model made of eight experts, each with seven billion parameters. It is used in the book as the worked example of how MoE parameter counts and active-compute costs diverge from a naive multiplication (AIE p.68).

## Key figures
- If no experts shared parameters, the model would have 8 × 7B = 56 billion parameters; due to parameter sharing, it actually has 46.7 billion parameters (AIE p.68)
- Only two experts are active per token, so only 12.9 billion parameters are active per token, giving it the cost and speed of a 12.9-billion-parameter model despite its 46.7 billion total parameters (AIE p.68)

## Related
- [[mixture-of-experts]]  (example-of: the book's worked example of an MoE model's parameter counting and active compute)

## Provenance
- [[sources/ch02-model-size]]
