---
type: concept
sources: [ch04-step-3-define-evaluation-methods-and-data]
---
# Simpson's Paradox

Simpson's paradox is a phenomenon in which model A performs better than model B on aggregated data but worse than model B on every subset of that data (AIE p.205). It is one of the motivating reasons for [[slice-based-evaluation]]: looking only at an overall score can hide a model's true relative performance within meaningful subgroups (AIE p.205).

## Key figures
- Worked example: Model A scores 93% (81/87) on Group 1 and 73% (192/263) on Group 2, beating Model B on both subgroups; but overall Model A scores 78% (273/350) versus Model B's 83% (289/350), so B wins in aggregate despite losing on every subgroup (AIE p.205)

## Related
- [[slice-based-evaluation]]  (part-of: Simpson's paradox is the specific failure pattern that motivates evaluating data by slice rather than in aggregate)

## Provenance
- [[sources/ch04-step-3-define-evaluation-methods-and-data]]
