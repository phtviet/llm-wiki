---
type: concept
sources: [ch07-finetuning-tactics]
---
# Epoch

An epoch is one full pass over the training data; the number of epochs determines how many times each training example is trained on. Small datasets typically need more epochs than large ones: a dataset of millions of examples may need only 1-2 epochs, while a dataset of thousands of examples may still improve after 4-10 epochs (AIE p.360).

The gap between training loss and validation loss diagnoses the right epoch count: if both keep decreasing, more epochs (and more data) may help; if training loss keeps decreasing while validation loss rises, the model is overfitting and the epoch count should be lowered (AIE p.360).

## Key figures
- Datasets of millions of examples: 1-2 epochs may suffice (AIE p.360)
- Datasets of thousands of examples: may still improve after 4-10 epochs (AIE p.360)

## Related
- [[finetuning-hyperparameters]]  (part-of: one of the frequently tuned finetuning hyperparameters)

## Provenance
- [[sources/ch07-finetuning-tactics]]
