---
type: concept
sources: [ch07-parameter-efficient-finetuning]
---
# Partial Finetuning

Partial finetuning updates only some of a model's parameters, typically the layers closest to the output, which tend to be more task-specific, while freezing earlier layers that capture more general features (AIE p.332). For example, freezing the first nine of ten layers and finetuning only the last reduces trainable parameters to 10% of full finetuning (AIE p.332).

The technique reduces memory footprint but is parameter-inefficient: it needs many trainable parameters to approach full-finetuning performance. Houlsby et al. (2019) showed that with BERT large, approximately 25% of parameters must be updated to match full finetuning on the GLUE benchmark (AIE p.333). This inefficiency is what motivated the search for methods that are parameter-efficient, i.e. [[peft]] (AIE p.334).

## Key figures
- Freezing 9 of 10 layers, finetuning only the last, reduces trainable parameters to 10% of full finetuning (AIE p.332)
- Houlsby et al. (2019): ~25% of BERT large's parameters must be updated to match full-finetuning performance on GLUE (AIE p.333)

## Related
- [[full-finetuning]] (contrast: updates all parameters instead of a subset)
- [[peft]] (boundary: partial finetuning reduces memory but not parameter count needed for comparable performance, unlike PEFT)
- [[bert]] (example-of: BERT large is the model Houlsby et al. used to measure partial-finetuning's parameter inefficiency)

## Provenance
- [[sources/ch07-parameter-efficient-finetuning]]
