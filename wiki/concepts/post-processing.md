---
type: concept
sources: [ch02-structured-outputs]
---
# Post-Processing (Structured Outputs)

Post-processing corrects a model's output after generation, and is simple and cheap but can work surprisingly well. Models tend to repeat similar mistakes across queries, much like students repeating similar errors; once the common mistakes are identified, a script can correct them, such as adding a missing closing bracket to a JSON object (AIE p.102). Post-processing only works if the mistakes are easy to fix, which usually holds when a model's outputs are already mostly correctly formatted with occasional small errors (AIE p.102).

[[linkedin]]'s defensive YAML parser raised the percentage of correct YAML outputs from 90% to 99.99% (Bottaro and Ramgopal, 2020) (AIE p.102).

## Key figures
None (see [[linkedin]] for its entity-specific figures).

## Related
- [[structured-outputs]]  (part-of: post-processing is one of the five layers for enforcing structured outputs)
- [[linkedin]]  (example-of: LinkedIn's defensive YAML parser is a concrete case of post-processing)

## Provenance
- [[sources/ch02-structured-outputs]]
