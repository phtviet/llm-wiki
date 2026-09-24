---
type: concept
sources: [ch07-memory-math]
---
# Gradient Checkpointing

Gradient checkpointing, also called activation recomputation, is a technique to reduce the memory needed for activations during training. Instead of storing activations for reuse in the backward pass, the technique recomputes them when needed. This reduces memory requirements but increases training time due to the recomputation (AIE p.324).

## Key figures
None.

## Related
- [[training-memory-calculation]]  (part-of: addresses the activation-memory term in the training memory formula)
- [[backpropagation]]  (prerequisite: recomputation applies to activations needed for the backward pass's gradient computation)

## Provenance
- [[sources/ch07-memory-math]]
