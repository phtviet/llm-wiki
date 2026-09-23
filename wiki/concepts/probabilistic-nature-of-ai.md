---
type: concept
sources: [ch02-the-probabilistic-nature-of-ai]
---
# Probabilistic Nature of AI

AI models sample their responses probabilistically rather than deterministically: given a prompt, a model assigns probabilities across possible answers and samples according to them, so the same question can get different answers on different calls (AIE p.105). This contrasts with a deterministic process, where the outcome never varies. Because foundation models are trained on large aggregations of the opinions of the masses, anything with a non-zero probability of appearing in that data -- however far-fetched or wrong -- can be generated, which is both what makes AI useful for creative, open-ended tasks and what causes its two main failure modes: [[inconsistency]] and [[hallucination]] (AIE p.105).

## Key figures
None.

## Examples
- [[inconsistency]]  (same or slightly different input yields drastically different outputs)
- [[hallucination]]  (model outputs a response ungrounded in facts)

## Related
- [[sampling]]  (prerequisite: probabilistic behavior arises from how a model samples outputs)
- [[temperature]]  (part-of: fixing sampling variables like temperature is one way to reduce randomness, though not eliminate it)
- [[inconsistency]]  (example-of: a consequence of the model's probabilistic sampling)
- [[hallucination]]  (example-of: another consequence of the model's probabilistic sampling)

## Provenance
- [[sources/ch02-the-probabilistic-nature-of-ai]]
