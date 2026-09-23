---
type: concept
sources: [ch02-sampling-fundamentals]
---
# Best of N Strategy

Best of N is a strategy that leverages a model's sampling process to improve performance: the model generates multiple outputs, and the ones given high scores by a reward model are selected (AIE p.88). Some companies find this sufficient without further reinforcement learning -- [[stitch-fix]] and [[grab]] find that having a reward model alone, combined with best-of-N selection, is good enough for their applications, letting them skip reinforcement learning altogether (AIE p.88).

## Key figures
None.

## Related
- [[sampling]]  (part-of: relies on a model's sampling process to generate multiple candidate outputs)
- [[reward-model]]  (prerequisite: candidate outputs are ranked by a reward model's scores)
- [[preference-finetuning]]  (contrast: reward-model-based selection at inference vs. training-time alignment via RL)

## Provenance
- [[sources/ch02-sampling-fundamentals]]
