---
type: concept
sources: [ch01-summary, ch02-post-training]
---
# Post-Training

Post-training starts with a pre-trained model and addresses two problems left by
pre-training: self-supervision optimizes a model for text completion, not conversation,
and a model trained on indiscriminately scraped internet data can produce outputs that
are racist, sexist, rude, or wrong (AIE p.78). Post-training generally consists of two
steps: (1) [[supervised-finetuning]] on high-quality instruction data, to optimize the
model for conversations instead of completion, and (2) [[preference-finetuning]],
typically done with reinforcement learning, to align outputs with human preference
(AIE p.78).

While pre-training optimizes token-level quality -- predicting the next token accurately
-- users care about the quality of the entire response, which is what post-training
optimizes for. Pre-training is compared to reading to acquire knowledge; post-training is
like learning how to use that knowledge (AIE p.79). Because post-training consumes a
small portion of resources compared to pre-training, it can be understood as unlocking
capabilities the pre-trained model already has but that are hard to access via prompting
alone (AIE p.78-79).

Terminology note: some people use "instruction finetuning" to mean supervised finetuning
alone, others to mean both supervised and preference finetuning; the book avoids the term
for this reason (AIE p.78).

## Key figures
- InstructGPT used about 2% of compute for post-training and 98% for pre-training (AIE p.78)

## Examples
- [[supervised-finetuning]]  (first post-training step, on instruction data)
- [[preference-finetuning]]  (second post-training step, aligns with human preference)

## Related
- [[pre-training]]  (prerequisite: post-training starts from a pre-trained model; contrast: optimizes response quality vs. token-level prediction)
- [[finetuning]]  (part-of: post-training is conceptually the same as finetuning, applied after pre-training)
- [[supervised-finetuning]]  (part-of: first of the two post-training steps)
- [[preference-finetuning]]  (part-of: second of the two post-training steps)
- [[self-supervision]]  (boundary: pre-training uses self-supervision to optimize for completion; post-training corrects what self-supervision leaves unaddressed)

## Provenance
- [[sources/ch02-post-training]]
