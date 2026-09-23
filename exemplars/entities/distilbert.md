---
type: entity
sources: [ch08-model-distillation]
---
# DistilBERT

DistilBERT is a compact language model distilled from BERT: a smaller, faster student
trained to reproduce the behaviour of the larger BERT teacher (Sanh et al., 2019). In
the book it is the example of a student **trained from scratch**, as distinct from
distillation by finetuning an existing pre-trained model (the Alpaca route). See
[[model-distillation]] for the general method (AIE p.395).

## Key figures
- Reduces BERT's size by 40%, retains 97% of its language comprehension, and is 60% faster (AIE p.395)

## Related
- [[model-distillation]] (example-of: the canonical trained-from-scratch student)
- [[alpaca]]  (contrast: trained from scratch vs. finetuned from a pre-trained model)

## Provenance
- [[sources/ch08-model-distillation]]
