---
type: concept
sources: [ch02-preference-finetuning]
---
# Comparison Data

Comparison data is labeled data in the format (prompt, winning_response, losing_response), produced by having labelers compare two generated responses to the same prompt and decide which is better, rather than scoring each response independently (AIE p.84-85). This pointwise-vs-comparison distinction matters because pointwise scoring is unreliable: the same labeler can give different scores to an identical pair on different occasions (AIE p.84).

Comparing responses is still labor-intensive: LMSYS found manual comparison took three to five minutes on average, since it requires fact-checking each response (Chiang et al., 2024) (AIE p.85). [[llama-2]] author Thomas Scialom reported each comparison cost $3.50, much cheaper than writing a response outright, which cost $25 (AIE p.85). OpenAI's [[instructgpt]] labelers gave scores from 1 to 7 and ranked responses in preference order, but only the ranking was used to train the reward model; inter-labeler agreement was around 73%, meaning roughly 7 of 10 labelers agree on a ranking for the same pair (AIE p.85). To speed labeling, annotators rank multiple responses at once: a ranked set of three (A > B > C) yields three ranked pairs (A > B, A > C, B > C) (AIE p.85).

## Key figures
- Manual response comparison takes 3-5 minutes on average (AIE p.85)
- Each comparison cost $3.50, versus $25 to write a response from scratch (AIE p.85)
- OpenAI InstructGPT labelers' inter-labeler ranking agreement: approximately 73% (AIE p.85)

## Examples
- None named beyond Anthropic's HH-RLHF dataset example and OpenAI's InstructGPT labeling interface.

## Related
- [[reward-model]]  (prerequisite: comparison data is what the reward model is trained on)
- [[rlhf]]  (part-of: comparison data collection is the data-gathering step underlying RLHF's reward model training)
- [[preference-finetuning]]  (prerequisite: preference finetuning depends on comparison-labeled data)
- [[instructgpt]]  (see-also: mentioned in this page's text)
- [[llama-2]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-preference-finetuning]]
