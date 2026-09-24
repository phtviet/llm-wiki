---
type: concept
sources: [ch07-parameter-efficient-finetuning]
---
# Full Finetuning

Full finetuning updates every parameter in a previously trained model: the number of trainable parameters equals the model's total parameter count. It resembles training, but starts from previously trained weights rather than randomly initialized ones (AIE p.332).

Full finetuning is memory-intensive: for a 7B-parameter model in FP16, loading the weights alone takes 14 GB, and finetuning with the Adam optimizer (also FP16) adds another 7B x 3 x 2 bytes = 42 GB, for a 56 GB total that exceeds most consumer GPUs' 12-48 GB capacity, before even counting activation memory (AIE p.333). Full finetuning, especially supervised and preference finetuning, also typically requires large amounts of high-quality annotated data that most practitioners can't afford (AIE p.333). These costs motivated partial finetuning and, subsequently, [[peft]] (AIE p.333).

## Key figures
- 7B-parameter model in FP16: 14 GB to load weights, +42 GB for Adam-optimizer gradients/states, 56 GB total (AIE p.333)

## Related
- [[partial-finetuning]] (contrast: updates only some parameters instead of all, trading memory for parameter inefficiency)
- [[peft]] (contrast: achieves near-full-finetuning performance with orders of magnitude fewer trainable parameters)
- [[training-memory-calculation]] (example-of: the 14 GB + 42 GB memory-math example instantiates the general training-memory formula)
- [[finetuning]] (part-of: full finetuning is one mode of finetuning, distinguished by updating all parameters)

## Provenance
- [[sources/ch07-parameter-efficient-finetuning]]
