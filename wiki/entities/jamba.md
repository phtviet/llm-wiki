---
type: entity
sources: [ch02-model-architecture]
---
# Jamba

Jamba, introduced in 'Jamba: A Hybrid Transformer-Mamba Language Model' (Lieber et al., 2024), interleaves blocks of transformer and [[mamba]] layers to scale up state space models further. The released model is a mixture-of-experts model designed to fit in a single 80GB GPU. Jamba shows strong performance on standard language model benchmarks and long-context evaluations, and has a small memory footprint compared to vanilla transformers (AIE p.66).

## Key figures
- 52B total available parameters, 12B active parameters, designed to fit in a single 80GB GPU (AIE p.66)
- Strong long-context evaluation performance for context lengths up to 256K tokens (AIE p.66)

## Related
- [[mamba]]  (prerequisite: Jamba interleaves Mamba layers with transformer layers)
- [[state-space-models]]  (example-of: Jamba is a hybrid SSM/transformer technique extending the SSM lineage)
- [[transformer-architecture]]  (contrast: hybrid interleaving of transformer and SSM layers vs. pure transformer)

## Provenance
- [[sources/ch02-model-architecture]]
