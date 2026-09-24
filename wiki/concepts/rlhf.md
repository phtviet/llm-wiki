---
type: concept
sources: [ch02-preference-finetuning]
---
# RLHF (Reinforcement Learning from Human Feedback)

RLHF is the earliest successful, still widely used preference finetuning algorithm. It consists of two parts: (1) train a reward model that scores the foundation model's outputs, and (2) optimize the foundation model to generate responses that the reward model scores maximally (AIE p.84). The optimization step is commonly done with proximal policy optimization (PPO), a reinforcement learning algorithm OpenAI released in 2017 (AIE p.87).

The [[reward-model]] is trained on [[comparison-data]] rather than direct pointwise scores, since asking labelers to score a response directly produces inconsistent results -- the same labeler can give different scores to the same (prompt, response) pair on different occasions (AIE p.84). Comparing two responses and picking the better one is an easier labeling task, though it still takes significant time and cost (AIE p.85).

During the second stage, prompts are randomly drawn from a distribution (such as existing user prompts), fed to the SFT model, and the resulting responses are scored by the reward model to further train the SFT model (AIE p.87).

## Key figures
None. RLHF's own figures (cost, timing, inter-labeler agreement) belong to the [[comparison-data]] and [[reward-model]] pages that describe the underlying data-collection process.

## Examples
- None named as distinct RLHF implementations in this section beyond Llama 2's use of it.

## Related
- [[preference-finetuning]]  (part-of: RLHF is the featured algorithm implementing preference finetuning)
- [[reward-model]]  (prerequisite: RLHF requires a trained reward model before the optimization step)
- [[comparison-data]]  (prerequisite: the reward model is trained on comparison data, not pointwise scores)
- [[best-of-n]]  (contrast: some companies use the reward model alone with best-of-N sampling instead of RLHF's optimization step)

## Provenance
- [[sources/ch02-preference-finetuning]]
