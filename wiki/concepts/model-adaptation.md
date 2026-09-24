---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Model Adaptation

Model adaptation is the process of adjusting a foundation model to a specific application, and it is the activity that AI engineering centers on, in place of the modeling and training that traditional ML engineering centers on (AIE p.40). Adaptation techniques split into two categories depending on whether they update model weights (AIE p.40).

Prompt-based techniques, including [[prompt-engineering]], adapt a model without updating its weights: instructions and context are given to the model instead of changing the model itself. Prompt engineering is easier to start with, needs less data, and lets a builder experiment across more models, but it may not suffice for complex tasks or applications with strict performance requirements (AIE p.40).

[[finetuning]] instead updates the model's weights. It is more complicated and needs more data than prompting, but can improve quality, latency, and cost significantly, and enables things prompting cannot, such as adapting a model to a task it never saw during training (AIE p.40).

## Key figures
None.

## Examples
- [[prompt-engineering]]
- [[finetuning]]

## Related
- [[prompt-engineering]]  (part-of: a weight-preserving category of model adaptation)
- [[finetuning]]  (part-of: a weight-updating category of model adaptation)
- [[ai-engineering-versus-full-stack-engineering]]  (see-also: model adaptation is the activity AI engineering emphasizes over training)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
