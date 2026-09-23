---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Model Adaptation

Model adaptation is the umbrella term for techniques that make a pretrained foundation model behave the way an application needs. It splits into two categories based on whether they update model weights: [[prompt-engineering]], which adapts a model without changing its weights, and [[finetuning]], which adapts a model by changing its weights (AIE p.40). AI engineering focuses less on modeling and training from scratch, and more on adapting existing models this way (AIE p.39).

Prompt-based techniques are easier to start with, require less data, and let you experiment across more models, increasing the chance of finding one unexpectedly good for your use case — but they may not suffice for complex tasks or strict performance requirements. Finetuning is more complicated and data-hungry, but can significantly improve quality, latency, and cost, and enables things impossible without changing weights, such as adapting a model to a task unseen during training (AIE p.40).

How much data an adaptation technique needs follows a rough ordering: training a model from scratch needs more data than finetuning, which needs more data than prompt engineering (AIE p.42).

## Key figures
None.

## Examples
- [[prompt-engineering]]  (adapts without updating weights)
- [[finetuning]]  (adapts by updating weights)

## Related
- [[prompt-engineering]]  (part-of: one of the two model-adaptation categories; requires no weight updates)
- [[finetuning]]  (part-of: one of the two model-adaptation categories; requires weight updates)
- [[model-distillation]]  (contrast: distillation trains a new small student model rather than adapting an existing one via prompting or finetuning)
- [[ai-engineering-vs-ml-engineering]]  (part-of: model adaptation is the central shift the synthesis describes)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
