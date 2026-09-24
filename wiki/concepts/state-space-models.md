---
type: concept
sources: [ch02-model-architecture]
---
# State Space Models (SSMs)

State space models (SSMs) (Gu et al., 2021a) are an alternative to the transformer architecture that has shown a lot of promise in long-range memory, a core challenge in developing LLMs. Since their 2021 introduction, multiple techniques have improved SSMs' efficiency, long-sequence handling, and scalability (AIE p.65).

Key steps in the SSM lineage described in the book: S4 (Gu et al., 2021b) made SSMs more efficient. H3 (Fu et al., 2022) added a mechanism to recall early tokens and compare tokens across sequences, serving a purpose similar to attention but more efficiently. [[mamba]] (Gu and Dao, 2023) scaled SSMs to 3 billion parameters, and [[jamba]] (Lieber et al., 2024) interleaves transformer and Mamba layers to scale SSMs further (AIE p.65-66).

## Key figures
None. Model-specific figures (Mamba's parameter scale, Jamba's active/total parameters and [[context-length]]) live on their entity pages.

## Examples
- [[mamba]]  (SSM scaled to 3B parameters, outperforming similarly-sized transformers)
- [[jamba]]  (hybrid transformer-Mamba mixture-of-experts model)

## Related
- [[transformer-architecture]]  (contrast: alternative architecture family avoiding attention's quadratic scaling)
- [[attention-mechanism]]  (boundary: H3's recall mechanism serves a similar purpose to attention but more efficiently)
- [[context-length]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-model-architecture]]
