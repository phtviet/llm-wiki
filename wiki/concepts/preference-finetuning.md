---
type: concept
sources: [ch02-post-training]
---
# Preference Finetuning

Preference finetuning is the second step of [[post-training]]: further finetuning a
supervised-finetuned model to output responses that align with human preference (AIE
p.78). It is typically done with reinforcement learning. Techniques include
reinforcement learning from human feedback ([[rlhf]]), used by GPT-3.5 and Llama 2;
DPO (Direct Preference Optimization), used by Llama 3; and reinforcement learning from
AI feedback (RLAIF), potentially used by Claude (AIE p.78). In the book's
Shoggoth-with-a-smiley-face analogy, preference finetuning is the final polish that
makes the model customer-appropriate -- giving the monster its smiley face (AIE p.79).

## Key figures
None.

## Examples
- [[rlhf]]  (used by GPT-3.5 and Llama 2)

## Related
- [[post-training]]  (part-of: preference finetuning is the second of post-training's two steps)
- [[supervised-finetuning]]  (contrast: aligns with human preference vs. optimizes for conversational instruction-following; prerequisite: typically follows SFT)
- [[rlhf]]  (example-of: a preference finetuning technique used by GPT-3.5 and Llama 2)

## Provenance
- [[sources/ch02-post-training]]
