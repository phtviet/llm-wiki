---
type: concept
sources: [ch02-post-training, ch02-supervised-finetuning]
---
# Supervised Finetuning

Supervised finetuning (SFT) is the first post-training step: it finetunes a pre-trained
model on demonstration data to shift it from completion behavior toward conversational
behavior (AIE p.80). A pre-trained model, left alone, tends to continue a prompt rather
than answer it -- given "How to make pizza", it might add context, ask follow-up
questions, or actually give instructions; only the last is the appropriate conversational
response (AIE p.80).

Demonstration data consists of (prompt, response) pairs showing the model how it should
behave; this process is sometimes called behavior cloning, since the model clones the
demonstrated behavior (AIE p.81). Because different request types (question answering,
summarization, translation, etc.) need different responses, demonstration data should
cover the full range of tasks the model is meant to handle (AIE p.81).

Good demonstration data requires good labelers. Unlike traditional data labeling, which
often needs little domain expertise, writing demonstration responses can require critical
thinking, information gathering, and judgment about the appropriateness of a request, so
companies often use highly educated labelers (AIE p.81-82). This makes demonstration
data substantially more expensive to produce than typical labeled data (AIE p.82).

## Key figures
- Among InstructGPT's demonstration-data labelers, ~90% had at least a college degree and more than one-third had a master's degree (AIE p.82)
- Generating one (prompt, response) pair could take up to 30 minutes for tasks like summarization (AIE p.82)
- At $10 per pair, OpenAI's 13,000 demonstration pairs for InstructGPT would cost $130,000, not counting task design, labeler recruiting, or quality control (AIE p.82)

## Examples
- [[instructgpt]]  (OpenAI model finetuned on demonstration data covering question answering, summarization, translation, and more)

## Related
- [[preference-finetuning]]  (prerequisite: SFT precedes preference finetuning as the second post-training step)
- [[post-training]]  (part-of: SFT is the first of the two post-training steps)
- [[pre-training]]  (contrast: pre-trained model is optimized for completion, not conversation, motivating SFT)
- [[dataset-engineering]]  (prerequisite: demonstration data is a curated, labeled dataset requiring careful design and quality control)

## Provenance
- [[sources/ch02-post-training]]
- [[sources/ch02-supervised-finetuning]]
