---
type: concept
sources: [ch04-step-3-define-evaluation-methods-and-data]
---
# Slice-Based Evaluation

Slice-based evaluation separates evaluation data into subsets and examines a system's performance on each subset separately, rather than only looking at an aggregate score (AIE p.205). A finer-grained understanding of system performance serves several purposes: avoiding bias against minority user groups, debugging why a system underperforms on a subset (e.g. by length, topic, or format), finding areas for improvement (e.g. a different technique for long inputs), and avoiding [[simpsons-paradox]] (AIE p.205).

A robust evaluation setup uses multiple evaluation sets representing different slices: one matching the overall production data distribution, sets sliced by tier (paying vs. free users), traffic source (mobile vs. web), or usage; a set of examples the system is known to frequently get wrong; a set reflecting common user mistakes (e.g. typos); and an out-of-scope set of inputs the application should decline to engage with (AIE p.205-206). The guiding principle is: if you care about something, put a test set on it (AIE p.206).

## Key figures
None.

## Examples
- [[simpsons-paradox]]  (the failure mode aggregate-only evaluation can hide)

## Related
- [[evaluation-guideline]]  (part-of: slicing is part of specifying how an application's evaluation data should be curated)
- [[simpsons-paradox]]  (example-of: a concrete failure pattern that slicing is designed to catch)
- [[evaluation-set-sizing]]  (see-also: both concern how evaluation data should be curated and sized for reliability)

## Provenance
- [[sources/ch04-step-3-define-evaluation-methods-and-data]]
