---
type: entity
sources: [ch07-memory-math]
---
# Adam Optimizer

Adam is the dominant optimizer for transformer-based models, used in backpropagation's backward pass to update trainable parameters. Unlike a vanilla SGD optimizer, which stores no additional state, or a momentum optimizer, which stores one value per trainable parameter, Adam stores two values per trainable parameter (in addition to the gradient itself), for three stored values per trainable parameter total (AIE p.323).

This makes Adam's memory cost for gradients and optimizer states three times the parameter count at a given byte precision: for a 13B-parameter model at 2 bytes per value, gradients and optimizer states require 13B x 3 x 2 bytes = 78 GB; for 1B trainable parameters the same calculation gives 6 GB (AIE p.323).

## Key figures
- Stores 2 optimizer-state values per trainable parameter (3 total with gradient) (AIE p.323)
- 13B trainable parameters: 78 GB for gradients and optimizer states at 2 bytes/value (AIE p.323)
- 1B trainable parameters: 6 GB for gradients and optimizer states at 2 bytes/value (AIE p.323)

## Related
- [[training-memory-calculation]]  (part-of: Adam's per-parameter state values are the basis of the training memory formula's gradient/optimizer-state term)
- [[backpropagation]]  (part-of: Adam operates during the backward pass to update trainable parameters)
- [[trainable-parameters]]  (prerequisite: Adam's memory cost scales with the count of trainable parameters)

## Provenance
- [[sources/ch07-memory-math]]
