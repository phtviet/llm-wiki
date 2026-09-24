---
type: concept
sources: [ch07-finetuning, ch07-finetuning-intro]
---
# Finetuning

Finetuning is the process of adapting a model to a specific task by further training the whole model or part of the model, adjusting its weights. This contrasts with prompt-based methods (prompt engineering, [[context-construction]]), which adapt a model by giving it instructions, context, and tools without changing weights (AIE p.307).

Finetuning can enhance a model's domain-specific capabilities (e.g. coding or medical question answering) and strengthen its safety, but it is most often used to improve instruction-following ability, particularly adherence to specific output styles and formats (AIE p.307). It requires more up-front investment than prompting, and a common practical question is when to finetune versus when to do RAG (AIE p.307).

Compared to prompt-based methods, finetuning incurs a much higher memory footprint: at the scale of today's foundation models, naive finetuning often requires more memory than is available on a single GPU, making it expensive and challenging. Reducing memory requirements motivates many finetuning techniques, including [[peft]] (AIE p.307).

Finetuning continues training a previously trained model, and is cheaper than pre-training from scratch (AIE p.307).

## Key figures
None.

## Examples
- [[peft]]  (dominant memory-efficient finetuning approach)

## Related
- [[peft]]  (part-of: PEFT is a memory-efficient category of finetuning technique)
- [[pre-training]]  (contrast: finetuning continues training an existing model vs. pre-training starts from randomly initialized weights)
- [[prompt-engineering]]  (contrast: adapts model behavior via input alone vs. finetuning adjusts weights)
- [[rag]]  (contrast: alternative adaptation strategy; common practical choice against finetuning)
- [[finetuning-versus-rag]]  (see-also: synthesis contrasting finetuning and RAG as adaptation strategies)
- [[trainable-parameters]]  (prerequisite: finetuning updates trainable parameters, whose gradients and optimizer states drive memory footprint)

## Provenance
- [[sources/ch07-finetuning]]
