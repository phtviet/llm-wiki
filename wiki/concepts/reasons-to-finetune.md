---
type: concept
sources: [ch07-reasons-to-finetune]
---
# Reasons to Finetune

The primary reason to finetune a model is to improve its quality, both in general capabilities and on task-specific capabilities. Finetuning is commonly used to improve a model's ability to generate outputs following specific structures, such as JSON or YAML (AIE p.311).

A general-purpose model performing well on broad benchmarks may still fail on a specific task it wasn't sufficiently trained on. For example, a model good at standard SQL might fail on a less common SQL dialect, or fail on customer-specific queries even while handling common ones well; finetuning on data covering that dialect or those queries addresses the gap (AIE p.311).

Another use case is bias mitigation: if a base model perpetuates biases from its training data (such as consistently assigning CEOs male-sounding names), exposing it to carefully curated data during finetuning can counteract this (Wang and Russakovsky, 2023). Garimella et al. (2022) found finetuning BERT-like models on text authored by women reduced gender bias, while finetuning on text by African authors reduced racial bias (AIE p.312).

Finetuning smaller models is much more common than finetuning big ones, since smaller models require less memory, making them easier, cheaper, and faster to finetune and to run in production. A small model finetuned on a specific task can outperform a much larger out-of-the-box model on that task (AIE p.312).

A related but distinct approach is finetuning a small model to imitate a larger model's behavior using data the larger model generated -- this is [[model-distillation]], a form of [[data-synthesis]] (AIE p.312).

In the early days of foundation models, the strongest models were commercial with limited finetuning access, leaving few competitive models to finetune. As the open source community has produced high-quality models across sizes and domains, finetuning has become more viable and attractive (AIE p.312).

## Key figures
None. See [[finetuning]] for general framing; entity-specific figures (e.g. Grammarly's Flan-T5 results) are noted inline above as illustrative, not load-bearing to this concept.

## Examples
- [[model-distillation]]  (finetuning a small model on a larger model's generated outputs)

## Related
- [[finetuning]]  (part-of: reasons to finetune motivate when to use finetuning generally)
- [[model-distillation]]  (example-of: distillation is finetuning a small model on a larger model's outputs)
- [[reasons-not-to-finetune]]  (contrast: counterarguments and costs against finetuning)
- [[peft]]  (see-also: smaller models being easier to finetune connects to memory-efficient finetuning approaches)
- [[data-synthesis]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch07-reasons-to-finetune]]
