---
type: concept
sources: [ch02-test-time-compute]
---
# Model Robustness

A model is considered robust if it doesn't dramatically change its outputs with small variations in the input (AIE p.99). The less robust a model is, the more it can benefit from test-time-compute techniques that sample multiple outputs, since resampling can recover a correct result that a single pass misses (AIE p.99). As an illustration, a project extracting information from product images found the model could read the information only about half the time on a single try, but sampling three times per image let it extract correct information for most images (AIE p.99).

## Key figures
- In one project, a model correctly read product-image information only about half the time on a single attempt; sampling three times per image extracted the correct information for most images (AIE p.99)

## Related
- [[test-time-compute]]  (prerequisite: robustness (or lack of it) determines how much benefit sampling multiple outputs provides)

## Provenance
- [[sources/ch02-test-time-compute]]
