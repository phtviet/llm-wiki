---
type: concept
sources: [ch09-model-optimization]
---
# Parallel Decoding

Parallel decoding techniques break the sequential dependency of autoregressive generation by attempting to generate multiple future tokens (xt+1, xt+2, ..., xt+k) simultaneously, rather than one at a time, on the premise that the existing sequence often carries enough information to guess several tokens ahead (AIE p.431). Parallel tokens can come from the same decoder repeatedly refining its guesses (Lookahead decoding, Fu et al., 2024) or from separate decoding heads trained to predict tokens at specific future positions, as in Medusa (Cai et al., 2024) (AIE p.431).

Because tokens generated this way are not produced sequentially, they must be verified for coherence and integrated. Lookahead decoding (also called Jacobi decoding after the underlying Jacobi method) generates K future tokens, verifies them, and regenerates only the tokens that fail, repeating until all pass (AIE p.432). Medusa instead uses a tree-based attention mechanism: each head proposes several token options per position, organized into a tree to select the most promising combination (AIE p.432). Parallel decoding is considered non-intuitive and, for techniques like Medusa, challenging to implement (AIE p.432).

## Key figures
- NVIDIA reports Medusa boosted Llama 3.1 token generation by up to 1.9x on HGX H200 GPUs (Eassa et al., 2024) (AIE p.432)

## Examples
- [[medusa]]

## Related
- [[autoregressive-decoding-bottleneck]]  (prerequisite: one solution to this bottleneck)
- [[speculative-decoding]]  (contrast: verifies a draft-model-generated sequence rather than breaking sequential dependency directly)
- [[medusa]]  (example-of: multi-head parallel decoding implementation)

## Provenance
- [[sources/ch09-model-optimization]]
