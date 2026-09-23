---
type: concept
sources: [ch02-structured-outputs]
---
# Constrained Sampling

Constrained sampling guides text generation toward satisfying certain constraints, and is typically the technique behind structured-output tools. To generate a token, the model first outputs a logit vector, one logit per possible token; constrained sampling filters this vector to keep only tokens meeting the constraints, then samples from the remaining valid tokens (AIE p.102-103).

Most real constraints require a grammar specifying what is and isn't allowed at each generation step -- for example, JSON grammar disallows an unescaped `{` immediately after another `{` unless inside a string. Building and incorporating such a grammar into the sampling process is nontrivial, and because each output format (JSON, YAML, regex, CSV, etc.) needs its own grammar, constrained sampling is less generalizable, limited to formats whose grammars are supported by external tools or the team itself. Grammar verification can also increase generation latency (Brandon T. Willard, 2024). Some practitioners argue the resources spent on constrained sampling would be better invested in training models to follow instructions better (AIE p.103).

## Key figures
None.

## Related
- [[structured-outputs]]  (part-of: one of the five layers for enforcing structured outputs, and the more intensive of the two "treatment" approaches)
- [[logits]]  (prerequisite: constrained sampling filters the logit vector before sampling)
- [[finetuning]]  (contrast: the other intensive-treatment approach, training the model itself rather than filtering its outputs)

## Provenance
- [[sources/ch02-structured-outputs]]
