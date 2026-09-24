---
type: concept
sources: [ch02-structured-outputs]
---
# Constrained Sampling

Constrained sampling guides text generation toward satisfying certain constraints by filtering the model's logit vector at each generation step, keeping only tokens that meet the constraint, then sampling from among those valid tokens (AIE p.102).

For most real formats the constraint isn't a simple filter: a grammar must specify what is and isn't allowed at each step (for example, JSON grammar disallows an unescaped `{` right after another `{` unless it's inside a string). Building and integrating such a grammar into sampling is nontrivial, so constrained sampling is less generalizable — each output format (JSON, YAML, regex, CSV, etc.) needs its own grammar, and its use is limited to formats supported by external tools or the team's own tooling. Grammar verification can also increase generation latency (Brandon T. Willard, 2024) (AIE p.102-103). Some practitioners argue against constrained sampling, preferring to invest resources in training models to follow instructions better instead (AIE p.103).

## Key figures
None.

## Related
- [[structured-outputs]]  (part-of: one of the layers at which structured generation can be guided)
- [[logit-vector]]  (prerequisite: constrained sampling filters the logit vector to remove tokens that violate the constraint)
- [[post-processing]]  (contrast: filters during sampling vs. fixes after generation)
- [[finetuning-for-structure]]  (contrast: alternative intensive-treatment approach; trains the model itself vs. constrains its sampling)

## Provenance
- [[sources/ch02-structured-outputs]]
