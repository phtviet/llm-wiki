---
type: concept
sources: [ch02-model-architecture]
---
# State Space Models (SSMs)

State space models (SSMs) are an alternative architecture to the transformer that has shown a lot of promise for long-range memory, introduced in 2021 (Gu et al., 2021a) (AIE p.65). Modeling long sequences remains a core challenge in developing LLMs, and multiple techniques have made SSMs progressively more efficient, better at long-sequence processing, and scalable to larger model sizes (AIE p.65):

- **S4** ( Gu et al., 2021b ), developed to make SSMs more computationally efficient (AIE p.66).
- **H3** ( Fu et al., 2022 ), which adds a mechanism to recall early tokens and compare tokens across sequences, serving a purpose similar to the transformer's attention mechanism but more efficiently (AIE p.66).
- **Mamba** ( Gu and Dao, 2023 ), which scales SSMs to three billion parameters; Mamba-3B outperforms transformers of the same size and matches transformers twice its size on language modeling, and its inference computation scales linearly with sequence length (versus quadratic scaling for transformers), showing improved performance on real data up to million-length sequences (AIE p.66).
- **Jamba** ( Lieber et al., 2024 ), which interleaves transformer and Mamba layers, released as a mixture-of-experts model with strong performance on standard benchmarks and long-context evaluation up to 256K tokens, with a smaller memory footprint than vanilla transformers (AIE p.66).

A separate RNN-based alternative, RWKV (Peng et al., 2023), can be parallelized for training and, due to its RNN nature, in theory has no fixed context-length limitation like transformers, though in practice this doesn't guarantee good long-context performance (AIE p.65).

## Key figures
- Mamba scales SSMs to 3 billion parameters, with inference computation scaling linearly (vs. quadratic for transformers) with sequence length (AIE p.66)
- Jamba: mixture-of-experts model with 52B total available parameters (12B active), fits a single 80GB GPU, strong performance up to 256K token context (AIE p.66)

## Related
- [[transformer-architecture]]  (contrast: alternative architecture aiming to overcome transformer limitations like context-length scaling)
- [[attention-mechanism]]  (contrast: H3's recall/comparison mechanism serves a similar purpose to attention but more efficiently)

## Provenance
- [[sources/ch02-model-architecture]]
