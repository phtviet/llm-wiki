---
type: concept
sources: [ch07-finetuning-tactics]
---
# Finetuning Development Path

OpenAI's finetuning best practices document describes two development paths for choosing and iterating on base models when finetuning (AIE p.357).

The **progression path** starts cheap and scales up: (1) test finetuning code on the cheapest, fastest model to confirm the code works; (2) test the data by finetuning a middling model, watching that training loss decreases with more data; (3) run further experiments with the best model to see how far performance can be pushed; (4) once results are good, train all candidate models to map the price/performance frontier and select the model that fits the use case (AIE p.357-358).

The **distillation path** starts strong and shrinks down: (1) train the best possible model on a small dataset using the strongest affordable base model, which needs less data because it starts strong; (2) use this finetuned model to generate more training data; (3) use that generated dataset to train a cheaper model (AIE p.358).

Because finetuning usually follows prompt-engineering experiments, teams should already understand different models' behaviors by the time they choose a development path, and should plan the path based on that understanding (AIE p.358).

## Key figures
None.

## Related
- [[finetuning]]  (prerequisite: development paths structure how finetuning experiments are sequenced)
- [[model-selection]]  (part-of: base-model selection criteria from model selection apply to choosing a finetuning starting model)
- [[model-distillation]]  (see-also: the distillation path's naming echoes model distillation, using a finetuned model to generate training data for a cheaper model, though it is a finetuning workflow rather than the teacher/student distillation method)

## Provenance
- [[sources/ch07-finetuning-tactics]]
