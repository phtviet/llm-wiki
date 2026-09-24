---
type: concept
sources: [ch02-preference-finetuning]
---
# Best of N

Best of N is a strategy in which a model generates multiple output candidates for a prompt and the ones given high scores by a trained reward model are selected, skipping the reinforcement-learning optimization step of RLHF entirely (AIE p.88). Some companies, such as Stitch Fix and Grab, find that having the reward model alone, combined with best-of-N sampling, is good enough for their applications, without further RL-based finetuning (AIE p.88). The approach leverages how a model samples outputs to improve its effective performance (AIE p.88).

## Key figures
None.

## Examples
- None named beyond Stitch Fix and Grab's use of the approach.

## Related
- [[reward-model]]  (prerequisite: best-of-N requires a trained reward model to score candidates)
- [[rlhf]]  (contrast: skips RLHF's optimization stage in favor of sampling and selection)
- [[preference-finetuning]]  (boundary: an alternative to full reinforcement-learning-based preference finetuning)

## Provenance
- [[sources/ch02-preference-finetuning]]
