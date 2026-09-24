---
type: concept
sources: [ch07-finetuning-tactics]
---
# Prompt Loss Weight

In instruction finetuning, each training example has a prompt and a response, and both can contribute to the model's loss. Since prompts are user-provided at inference time and the model only needs to generate responses, response tokens should contribute more to the training loss than prompt tokens. The prompt loss weight controls this balance: at 100% prompts contribute to the loss as much as responses, meaning the model learns equally from both; at 0% the model learns only from responses. The weight is typically set to 10% by default, so the model learns mostly from responses but somewhat from prompts too (AIE p.361).

## Key figures
- Default prompt loss weight: 10% (AIE p.361)

## Related
- [[finetuning-hyperparameters]]  (part-of: one of the frequently tuned finetuning hyperparameters)
- [[demonstration-data]]  (see-also: governs how prompt-response demonstration pairs contribute to training loss)

## Provenance
- [[sources/ch07-finetuning-tactics]]
