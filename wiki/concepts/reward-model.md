---
type: concept
sources: [ch02-preference-finetuning]
---
# Reward Model

A reward model, central to [[rlhf]], is trained to take a (prompt, response) pair and output a scalar score for how good the response is (AIE p.84). Scoring a response directly (pointwise evaluation) produces inconsistent labels: the same labeler may score the same pair differently on different occasions. An easier labeling task is comparison: labelers judge which of two responses is better, producing comparison data in the format (prompt, winning_response, losing_response) (AIE p.84-85).

Given only comparison data, the reward model is trained to maximize the difference between its scalar scores for the winning and losing response, using a loss based on the sigmoid of that difference (the formula used by InstructGPT) (AIE p.86). The reward model can be trained from scratch or finetuned from another model, such as the pretrained or SFT model; finetuning from the strongest available foundation model tends to perform best. Some believe the reward model must be at least as powerful as the model it scores, but judging is generally believed easier than generating, so a weaker model can judge a stronger one (AIE p.86).

Once trained, the reward model is used to further train the SFT model: prompts are sampled, the model's responses are scored by the reward model, and the model is updated to maximize those scores, typically via proximal policy optimization (PPO), a reinforcement learning algorithm released by OpenAI in 2017 (AIE p.87).

## Key figures
- OpenAI's InstructGPT labelers had inter-labeler agreement of around 73% when ranking responses (AIE p.85)
- Comparing two responses took LMSYS labelers an average of three to five minutes each, due to fact-checking (AIE p.85)
- Llama 2 author Thomas Scialom reported each comparison cost $3.50, versus $25 to write a response from scratch (AIE p.85)

## Examples
- [[rlhf]]  (uses a reward model as its first stage)

## Related
- [[rlhf]]  (part-of: the reward model is trained in RLHF's first stage, then used to optimize the foundation model in the second)
- [[preference-finetuning]]  (part-of: the reward model implements the scoring half of preference finetuning)
- [[supervised-finetuning]]  (prerequisite: the SFT model is often the starting point that gets further tuned against the reward model's scores)

## Provenance
- [[sources/ch02-preference-finetuning]]
