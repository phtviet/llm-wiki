---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Pre-training

Pre-training refers to training a model from scratch, with weights randomly initialized (AIE p.41). For LLMs, pre-training often means training the model for text completion. It is, out of all training steps, typically the most resource-intensive by a long shot, and it also takes a long time; a small mistake during pre-training can cause significant financial loss and set a project back substantially. Because of this resource intensity, pre-training expertise is a rare, highly sought-after art (AIE p.41).

Pre-training and [[post-training]]/[[finetuning]] form a spectrum, with similar processes and tooling, though pre-training is distinguished by starting from random weights rather than a prior training run (AIE p.41).

## Key figures
- For the InstructGPT model, pre-training takes up to 98% of the overall compute and data resources (AIE p.41)

## Related
- [[finetuning]]  (contrast: trains from randomly initialized weights vs. continues training from existing weights)
- [[post-training]]  (prerequisite: post-training/finetuning builds on a model already produced by pre-training)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
