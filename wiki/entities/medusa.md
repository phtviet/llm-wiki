---
type: entity
sources: [ch09-model-optimization]
---
# Medusa

Medusa (Cai et al., 2024) is a parallel decoding technique that extends an existing model with multiple additional decoding heads, each a small neural network layer trained to predict a future token at a specific position beyond the next one: if the base model predicts xt+1, the kth Medusa head predicts xt+k+1. The heads train alongside the original model, which stays frozen (AIE p.431). Medusa verifies and integrates the resulting token options using a tree-based [[attention-mechanism]], organizing each head's proposed options into a tree structure to select the most promising combination (AIE p.432).

## Key figures
- NVIDIA reports Medusa boosted [[llama-3]].1 token generation by up to 1.9x on HGX H200 GPUs (Eassa et al., 2024) (AIE p.432)

## Related
- [[parallel-decoding]]  (example-of: Medusa is a parallel decoding technique using multiple decoding heads)
- [[speculative-decoding]]  (contrast: uses trained extra heads on the frozen base model rather than a separate draft model)
- [[attention-mechanism]]  (see-also: mentioned in this page's text)
- [[llama-3]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch09-model-optimization]]
