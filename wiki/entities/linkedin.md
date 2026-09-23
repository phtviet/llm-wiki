---
type: entity
sources: [ch01-summary, ch02-structured-outputs]
---
# LinkedIn

LinkedIn reported reaching 80% of its desired AI product experience within one month, then underestimating the effort needed for the remaining 20% (AIE p.28 or similar, see ch01-summary). Separately, LinkedIn built a defensive YAML parser for structured outputs: their underlying model, GPT-4, worked with both JSON and YAML, but they chose YAML as the output format because it is less verbose and requires fewer output tokens than JSON. The defensive parser raised the percentage of correct YAML outputs from 90% to 99.99% (Bottaro and Ramgopal, 2020) (AIE p.102).

## Key figures
- Defensive YAML parser increased correct YAML output rate from 90% to 99.99% (AIE p.102)

## Related
- [[post-processing]]  (example-of: the defensive YAML parser is a concrete post-processing technique)
- [[structured-outputs]]  (see-also: LinkedIn's format choice illustrates practical structured-output tradeoffs)

## Provenance
- [[sources/ch02-structured-outputs]]
