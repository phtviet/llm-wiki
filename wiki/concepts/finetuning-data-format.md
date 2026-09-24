---
type: concept
sources: [ch08-format-data]
---
# Finetuning Data Format

Once training data is deduplicated and cleaned, it must be put into the exact format expected by the model being finetuned: each model uses a specific tokenizer and expects a specific [[chat-template]]; using the wrong chat template can cause strange bugs (AIE p.401).

For [[supervised-finetuning]], data is typically formatted as (instruction, response), where the instruction can be further decomposed into (system prompt, user prompt). Instructions used for finetuning often differ from those used during [[prompt-engineering]]: because finetuning learns expected behavior directly from many examples, its instructions typically don't need the task descriptions or few-shot examples a prompt-engineered instruction would need (AIE p.401). A few-shot prompt used with a base model can be converted directly into finetuning training examples, one training example per shot, and the model can then be queried post-finetuning with a much shorter prompt than the original few-shot version -- reducing input tokens and helping manage inference cost (AIE p.401-402).

Different finetuning data formats can affect the finetuned model's performance, so experimenting to find the best format is worthwhile. Once finetuned, a model must be queried using prompts that exactly match the training data's format: deviations such as a missing end token, an added prefix, or an extra appended space can all cause issues (AIE p.402).

## Key figures
None.

## Examples
- Food classification: a three-shot 'Label the following item as either edible or inedible' prompt is converted into per-example (item --> label) training rows, then queried post-finetuning as simply '{INPUT} -->' (AIE p.401-402)

## Related
- [[supervised-finetuning]]  (prerequisite: this format applies to the instruction-response data supervised finetuning trains on)
- [[chat-template]]  (prerequisite: correct formatting depends on matching the model's expected chat template)
- [[prompt-versus-context]]  (contrast: finetuning instructions can drop the task descriptions and examples a prompt-engineered instruction needs)
- [[data-quality]]  (see-also: correct formatting is a distinct concern from the data-quality criteria applied earlier in processing)
- [[prompt-engineering]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch08-format-data]]
