---
type: concept
sources: [ch02-post-training]
---
# Supervised Finetuning (SFT)

Supervised finetuning is the first step of [[post-training]]: finetuning a pre-trained model on high-quality instruction data to optimize it for conversations instead of text completion (AIE p.78). It addresses the mismatch created by self-supervised [[pre-training|pre-training]], which trains a model to complete text rather than respond to instructions (AIE p.78).

In the Shoggoth-with-a-smiley-face analogy the book uses, self-supervised pre-training produces a rogue, untamed model trained on indiscriminate internet data; supervised finetuning on higher-quality data -- Stack Overflow, Quora, or human annotations -- makes this model more socially acceptable, prior to preference finetuning polishing it further (AIE p.79).

Some authors use the term 'instruction finetuning' to refer to supervised finetuning specifically, while others use it to cover both supervised finetuning and preference finetuning; the book avoids the term for this reason (AIE p.79).

## Key figures
None.

## Related
- [[post-training]]  (part-of: SFT is the first of post-training's two steps)
- [[preference-finetuning]]  (prerequisite: SFT typically precedes preference finetuning in the post-training workflow)
- [[finetuning]]  (example-of: SFT is a specific finetuning technique applied to conversational alignment)
- [[self-supervision]]  (contrast: pre-training's self-supervision optimizes for completion, while SFT uses labeled instruction data to optimize for conversation)
- [[pre-training]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-post-training]]
