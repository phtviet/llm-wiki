---
type: concept
sources: [ch02-post-training, ch08-model-distillation]
---
# Post-Training

Post-training starts with a pre-trained model and addresses two problems left by pre-training: self-supervised pre-training optimizes a model for text completion, not conversation, and a model trained on indiscriminately scraped internet data can produce racist, sexist, rude, or wrong outputs (AIE p.78). Post-training generally consists of two steps: [[supervised-finetuning]], which finetunes the pre-trained model on high-quality instruction data to optimize for conversation instead of completion, and [[preference-finetuning]], which further finetunes the model to output responses aligned with human preference, typically via reinforcement learning (AIE p.78).

Pre-training optimizes token-level quality -- predicting the next token accurately -- while post-training optimizes for the quality of the entire response as judged by users. One analogy: pre-training is like reading to acquire knowledge, post-training is like learning how to use that knowledge (AIE p.78). Post-training consumes a small portion of resources compared to pre-training -- [[instructgpt]] used only 2% of compute for post-training and 98% for pre-training -- so post-training can be thought of as unlocking capabilities the pre-trained model already has but that are hard to access via prompting alone (AIE p.79).

The combination of pre-training, supervised finetuning, and preference finetuning (e.g. via RLHF) is the popular recipe for building foundation models today, but it is not the only one; any of these steps can be skipped (AIE p.79). The term 'instruction finetuning' is ambiguous: some use it to mean supervised finetuning alone, others to mean both supervised and preference finetuning combined (AIE p.79).

## Key figures
- InstructGPT used only 2% of compute for post-training and 98% for pre-training (AIE p.79)

## Related
- [[supervised-finetuning]]  (part-of: first step of post-training, optimizes for conversation over completion)
- [[preference-finetuning]]  (part-of: second step of post-training, aligns responses with human preference)
- [[pre-training]]  (contrast: optimizes token-level next-token prediction vs. post-training's optimization for full-response quality; prerequisite: post-training starts from a pre-trained model)
- [[finetuning]]  (see-also: post-training is conceptually the same as finetuning but usually performed by model developers)
- [[self-supervision]]  (prerequisite: pre-training uses self-supervision, which post-training then corrects for conversational use)
- [[instructgpt]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-post-training]]
