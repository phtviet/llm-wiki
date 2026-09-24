---
type: concept
sources: [ch02-the-probabilistic-nature-of-ai]
---
# Probabilistic Nature of AI

AI models are probabilistic rather than deterministic: sampled outputs vary because the model assigns probabilities to different possible responses and samples according to that distribution, rather than always returning one fixed answer. For example, a model that believes Vietnamese cuisine has a 70% chance of being 'the best cuisine' and Italian cuisine a 30% chance will answer 'Vietnamese cuisine' 70% of the time (AIE p.105). This contrasts with a deterministic process, whose outcome has no random variation (AIE p.105).

This property makes AI well suited to creative tasks, since it can explore beyond the most common answer, but the same property is a liability for tasks that need reliability (AIE p.105). Foundation models are trained on large aggregations of the opinions of many people, so anything with a non-zero probability -- however far-fetched or wrong -- can be generated (AIE p.105). Much of AI engineering effort is aimed at harnessing and mitigating this probabilistic nature (AIE p.105). Two major failure modes follow directly from it: [[inconsistency]] and [[hallucination]].

## Key figures
None. The concept itself carries no intrinsic figure; the illustrative 70%/30% cuisine example is illustrative, not load-bearing.

## Examples
- [[inconsistency]]  (same or slightly different prompt yields drastically different output)
- [[hallucination]]  (model produces a response not grounded in facts)

## Related
- [[inconsistency]]  (part-of: a direct consequence of sampling randomly from a probability distribution)
- [[hallucination]]  (part-of: a direct consequence of the model's probabilistic generation, though not explained by sampling alone)
- [[sampling]]  (prerequisite: probabilistic behavior arises from the sampling process used to pick outputs)
- [[temperature]]  (see-also: a sampling variable that can be fixed to reduce randomness, but does not guarantee full consistency)

## Provenance
- [[sources/ch02-the-probabilistic-nature-of-ai]]
