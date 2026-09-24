---
type: concept
sources: [ch02-preference-finetuning, ch02-post-training]
---
# Preference Finetuning

Preference finetuning is the second step of post-training, aiming to get a model to behave according to human preference rather than just imitate [[demonstration-data]] (AIE p.83). Demonstration data (used in [[supervised-finetuning]]) teaches a model to hold a conversation but not what kind of conversation it should have; preference finetuning addresses that gap. The goal assumes both that a universal human preference exists and that it can be embedded into AI -- an ambitious, arguably impossible, goal, since people disagree widely on controversial questions (abortion, gun control, immigration, etc.) (AIE p.83).

The earliest successful and still-popular algorithm is [[rlhf]]. Newer approaches such as DPO (Rafailov et al., 2023) are gaining traction; Meta switched from RLHF for [[llama-2]] to DPO for [[llama-3]] to reduce complexity (AIE p.84). The book features RLHF over DPO because RLHF, while more complex, gives more flexibility to tweak the model. Llama 2's authors argued that LLMs' superior writing abilities, where they surpass human annotators on some tasks, are fundamentally driven by RLHF (Touvron et al., 2023) (AIE p.84).

Empirically, both RLHF and DPO improve performance over SFT alone, though as of writing there is debate over why they work (AIE p.87). Some companies skip reinforcement learning altogether and rely on the [[reward-model]] alone with a [[best-of-n]] sampling strategy (AIE p.88). Both SFT and preference finetuning exist to correct for the low quality of [[pre-training|pre-training]] data; better pre-training methods could eventually reduce the need for either (AIE p.87).

## Key figures
None. Cost and process figures (labeler comparison time, per-comparison cost) are specific to the [[comparison-data]] collection process and are recorded there.

## Examples
- [[rlhf]]  (the featured algorithm, using a reward model plus PPO)

## Related
- [[supervised-finetuning]]  (prerequisite: SFT precedes preference finetuning in post-training)
- [[rlhf]]  (example-of: the earliest and still-popular preference finetuning algorithm)
- [[comparison-data]]  (prerequisite: preference finetuning is trained from comparison-labeled data)
- [[best-of-n]]  (contrast: sampling-and-selection alternative to full reinforcement learning)
- [[post-training]]  (part-of: preference finetuning is the second post-training step, after SFT)
- [[demonstration-data]]  (see-also: mentioned in this page's text)
- [[pre-training]]  (see-also: mentioned in this page's text)
- [[reward-model]]  (see-also: mentioned in this page's text)
- [[llama-2]]  (see-also: mentioned in this page's text)
- [[llama-3]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-preference-finetuning]]
