---
type: concept
sources: [ch02-structured-outputs]
---
# Finetuning for Structured Outputs

Finetuning a model on examples that follow the desired output format is described as the most effective and general approach for getting structured outputs: it can work with any expected format, and while it doesn't guarantee the model always outputs the expected format, it is much more reliable than prompting (AIE p.104).

For certain tasks the output format can be guaranteed by modifying the model's architecture before finetuning — for example, appending a classifier head to the foundation model so it outputs only one of a set of pre-specified classes. This approach is also called feature-based transfer. During finetuning, the whole model can be retrained end-to-end, or only part of it (such as the classifier head); end-to-end training requires more resources but promises better performance (AIE p.104).

## Key figures
None.

## Related
- [[structured-outputs]]  (part-of: one of the layers at which structured generation can be guided; the most intensive treatment alongside constrained sampling)
- [[constrained-sampling]]  (contrast: alternative intensive-treatment approach; trains the model itself vs. constrains its sampling)
- [[finetuning]]  (example-of: finetuning for a structured-output format is a specific application of finetuning)

## Provenance
- [[sources/ch02-structured-outputs]]
