---
type: concept
sources: [ch07-finetuning-overview]
---
# Sample Efficiency

Sample efficiency describes a model's ability to learn effectively from fewer training samples. It is the main benefit [[transfer-learning]] confers: much of what a model needs to learn is already present in a base model from [[pre-training]], so [[finetuning]] just refines its behavior rather than learning from scratch (AIE p.309).

## Key figures
- Training a model from scratch for legal question answering may need millions of examples, while finetuning a good base model might require only a few hundred (AIE p.309)

## Related
- [[transfer-learning]]  (part-of: sample efficiency is the practical payoff of transfer learning)
- [[finetuning]]  (prerequisite: finetuning a good base model is what achieves the sample-efficiency gain)

## Provenance
- [[sources/ch07-finetuning-overview]]
