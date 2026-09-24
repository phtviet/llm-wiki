---
type: concept
sources: [ch02-test-time-compute]
---
# Beam Search

Beam search is a strategy for generating multiple output candidates during sequence generation more strategically than independent sampling: instead of generating all outputs independently (which can include many weak candidates), beam search generates a fixed number of the most promising candidates (the beam) at each step of sequence generation (AIE p.96).

## Key figures
None.

## Related
- [[test-time-compute]]  (part-of: beam search is one strategy for generating the multiple outputs test time compute relies on; contrast: strategic fixed-beam generation vs. independent best-of-N sampling)
- [[best-of-n]]  (contrast: beam search prunes to promising candidates at each step, vs. best-of-N generating full outputs independently and selecting after the fact)

## Provenance
- [[sources/ch02-test-time-compute]]
