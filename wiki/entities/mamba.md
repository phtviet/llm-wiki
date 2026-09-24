---
type: entity
sources: [ch02-model-architecture]
---
# Mamba

Mamba, introduced in 'Mamba: Linear-Time Sequence Modeling with Selective State Spaces' (Gu and Dao, 2023), is a [[state-space-models|state space model]] that scales SSMs to three billion parameters. On language modeling, Mamba-3B outperforms transformers of the same size and matches transformers twice its size. Its inference computation scales linearly with sequence length, compared to quadratic scaling for transformers, and its authors show performance improvements on real data up to million-length sequences (AIE p.66).

## Key figures
- Scales SSMs to 3 billion parameters; Mamba-3B outperforms same-size transformers and matches transformers twice its size (AIE p.66)
- Inference computation scales linearly with sequence length, versus quadratic scaling for transformers (AIE p.66)

## Related
- [[state-space-models]]  (example-of: Mamba is a specific SSM technique in the lineage from S4 and H3)
- [[jamba]]  (prerequisite: Jamba interleaves Mamba layers with transformer layers to scale SSMs further)
- [[transformer-architecture]]  (contrast: linear vs. quadratic inference scaling with sequence length)

## Provenance
- [[sources/ch02-model-architecture]]
