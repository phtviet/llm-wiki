---
type: entity
sources: [ch03-what-models-can-act-as-judges]
---
# Prometheus

Prometheus (Kim et al., 2023) is a reference-based judge that takes (prompt, generated response, reference response, scoring rubric) as input and outputs a quality score, assuming the reference response earns the top score (AIE p.147).

## Key figures
- Outputs a quality score on a 1-to-5 scale, with the reference response assumed to score 5 (AIE p.147)

## Related
- [[specialized-ai-judges]]  (example-of: a reference-based judge)
- [[bleurt]]  (contrast: both are reference-based judges, but BLEURT outputs a similarity score while Prometheus outputs a rubric-based quality score)

## Provenance
- [[sources/ch03-what-models-can-act-as-judges]]
