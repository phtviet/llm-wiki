---
type: concept
sources: [ch07-finetuning-overview]
---
# Self-Supervised Finetuning (Continued Pre-training)

Self-supervised finetuning, also called continued pre-training, finetunes a pre-trained model with [[self-supervision]] using cheap task-related data, before finetuning it on expensive, task-specific annotated data (AIE p.309). For example, to finetune a model for legal question answering, one can first finetune it on raw legal documents before finetuning on expensive annotated (question, answer) data; to finetune a model for Vietnamese book summarization, one can first finetune it on a large collection of Vietnamese text (AIE p.309-310).

## Key figures
None.

## Related
- [[finetuning]]  (part-of: a preparatory finetuning stage that precedes supervised finetuning on expensive labeled data)
- [[self-supervision]]  (prerequisite: uses the same label-free learning approach as pre-training, applied to task-related data)
- [[supervised-finetuning]]  (prerequisite: typically precedes supervised finetuning on annotated data)
- [[pre-training]]  (contrast: continues training on unlabeled task-related data rather than starting from randomly initialized weights)

## Provenance
- [[sources/ch07-finetuning-overview]]
