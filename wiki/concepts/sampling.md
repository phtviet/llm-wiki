---
type: concept
sources: [ch02-sampling-fundamentals]
---
# Sampling

Sampling is the process by which a model constructs its outputs from computed probabilities. Given an input, a neural network first computes the probability of each possible outcome; for a classification model these are the available classes, while for a language model this is a probability distribution over every token in the vocabulary (AIE p.88). These probabilities come from a logit vector output by the network, with one logit per possible value -- for a language model, one logit per vocabulary token, so the vector's size equals the vocabulary size (AIE p.89).

Sampling makes a model's outputs probabilistic rather than deterministic, which underlies behaviors like inconsistency and hallucination (AIE p.88). Rather than always choosing the single highest-probability outcome, a model can sample the next token according to the full probability distribution: if "red" has a 30% chance and "green" a 50% chance of following "My favorite color is ...", "red" is picked 30% of the time and "green" 50% of the time (AIE p.89).

## Key figures
None. The worked example's percentages (30%/50%, 90%/10%) are illustrative, not load-bearing figures about sampling in general.

## Examples
- [[greedy-sampling]]  (always picks the highest-probability outcome)

## Related
- [[greedy-sampling]]  (part-of: one strategy for choosing among the probabilities sampling computes)
- [[best-of-n-sampling]]  (part-of: leverages sampling to generate multiple outputs and pick the best)
- [[reward-model]]  (see-also: scores sampled outputs so the best can be selected)
- [[language-model]]  (prerequisite: sampling operates on the probability distribution a language model produces)

## Provenance
- [[sources/ch02-sampling-fundamentals]]
