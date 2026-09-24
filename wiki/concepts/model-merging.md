---
type: concept
sources: [ch07-parameter-efficient-finetuning]
---
# Model Merging

Model merging combines multiple models -- often separately finetuned models -- into one. It is generally not considered a form of finetuning, since finetuning tailors one model to specific needs while merging combines several, but it is complementary to finetuning: new model types and finetuning techniques have inspired a range of creative merging techniques (AIE p.332).

## Key figures
None.

## Examples
- [[model-merging-summing]]
- [[model-merging-layer-stacking]]
- [[model-merging-concatenation]]

## Related
- [[peft]] (contrast: PEFT adapts one model efficiently; merging instead combines multiple already-trained models)
- [[lora]] (see-also: merging LoRA adapters back into base weights is a related but distinct operation from merging whole separate models)
- [[finetuning]] (contrast: complementary technique to, but not itself a form of, finetuning)

## Provenance
- [[sources/ch07-parameter-efficient-finetuning]]
