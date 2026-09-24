---
type: entity
sources: [ch05-information-extraction]
---
# LAMA (Language Model Analysis)

LAMA is a benchmark introduced by Meta's AI lab in 2019 for factual probing: figuring out what relational knowledge a language model has memorized from its training data (Petroni et al., 2019). Relational knowledge takes the form 'X [relation] Y', such as 'X was born in Y' or 'X is a Y', and is probed via fill-in-the-blank statements like 'Winston Churchill is a _ citizen', which a model with the right knowledge should complete as 'British' (AIE p.243).

## Key figures
None.

## Related
- [[information-extraction]]  (prerequisite: the same fill-in-the-blank probing technique LAMA uses for factual probing can be repurposed to extract sensitive training data)

## Provenance
- [[sources/ch05-information-extraction]]
