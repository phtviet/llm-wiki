---
type: concept
sources: [ch07-reasons-not-to-finetune]
---
# Reasons Not to Finetune

Many improvements attributed to finetuning can also be achieved without it, through carefully crafted [[prompt-engineering]] and [[context-construction]] (AIE p.312). Finetuning also carries costs and risks that argue for trying other approaches first.

Finetuning a model for one specific task can degrade its performance on other tasks, which is frustrating for an application expecting diverse prompts. Fixes include finetuning on the full mix of tasks a model must handle, using separate models per task, or merging separate finetuned models back into one via [[model-merging]] (AIE p.312-313).

Finetuning is rarely the right first step in a new project, since it requires high up-front investment and continual maintenance. First, it needs annotated data, which is slow and expensive to acquire, though open source and AI-generated data can mitigate cost at the expense of variable effectiveness. Second, it requires the knowledge to evaluate and choose base models, tune training knobs (optimizer, [[learning-rate]], data volume, overfitting/underfitting), and debug the training process, even when finetuning frameworks and APIs automate steps. Third, once finetuned, the model must be served, requiring a decision between self-hosting and an API service, plus [[inference-optimization]] work that is nontrivial for large models (AIE p.313).

Finetuning also demands an ongoing policy and budget for monitoring, maintaining, and updating the model, since new base models are released faster than a finetuned model can typically be improved, raising the recurring question of when a better base model justifies switching (AIE p.313).

The recommended path is to start [[ai-engineering]] experiments with prompting and only explore finetuning or other advanced solutions once systematic, well-designed prompt experiments prove inadequate; many complaints about prompting's ineffectiveness trace back to unclear instructions, unrepresentative examples, and poorly defined metrics rather than a genuine limit of prompting (AIE p.314). Both prompting and finetuning experiments benefit from the same systematic processes: an evaluation pipeline, [[data-annotation]] guidelines, and experiment tracking (AIE p.314).

Before [[prompt-caching]] existed, one genuine benefit of finetuning was reducing token usage: instead of repeating examples in every prompt (which raises latency and cost and is capped by [[context-length]]), a model could be finetuned on those examples once, allowing a much shorter prompt with no limit on how many examples were used to train it. Prompt caching, which lets repetitive prompt segments be cached for reuse, has largely removed this benefit (AIE p.315).

## Key figures
None. The figures in this section (BloombergGPT's parameter count and training cost, the [[gpt-4|GPT-4]]-0314 vs. BloombergGPT benchmark scores) are entity-specific and live on the [[bloomberggpt]] page.

## Examples
- [[bloomberggpt]]  (domain-specific model outperformed by a general-purpose model on its own domain benchmarks)

## Related
- [[finetuning]]  (boundary: this page covers when finetuning is not the right choice, contrasted with finetuning's own definition and benefits)
- [[domain-specific-models]]  (boundary: general-purpose models increasingly match or beat domain-specific models, undercutting the case for training/finetuning narrow models)
- [[prompt-engineering]]  (prerequisite: recommended first step before attempting finetuning)
- [[model-adaptation-workflow]]  (part-of: this reasoning underlies the book's staged prompting-then-RAG-then-finetuning progression)
- [[model-merging]]  (see-also: offered as a way to combine per-task finetuned models instead of maintaining several)
- [[inference-optimization]]  (prerequisite: serving a finetuned model requires solving inference optimization, a nontrivial cost of choosing to finetune)
- [[data-annotation]]  (see-also: mentioned in this page's text)
- [[ai-engineering]]  (see-also: mentioned in this page's text)
- [[prompt-caching]]  (see-also: mentioned in this page's text)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch07-reasons-not-to-finetune]]
