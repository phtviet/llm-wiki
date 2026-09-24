---
type: concept
sources: [ch07-finetuning-overview]
---
# Infilling Finetuning

Infilling finetuning finetunes a model to fill in the blank using tokens both before and after a gap, rather than predicting only the next token (AIE p.310). It is especially useful for tasks such as text editing and code debugging, and a model can be finetuned for infilling even if it was pre-trained autoregressively (AIE p.310).

## Key figures
None.

## Related
- [[supervised-finetuning]]  (part-of: an alternative training objective within supervised finetuning, alongside next-token prediction)
- [[masked-language-model]]  (contrast: infilling finetuning applies a fill-in-the-blank objective during finetuning, whereas masked language models are pre-trained with that objective from the start)
- [[autoregressive-language-model]]  (boundary: an autoregressively pre-trained model can still be finetuned for infilling)

## Provenance
- [[sources/ch07-finetuning-overview]]
