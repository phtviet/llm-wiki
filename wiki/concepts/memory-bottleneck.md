---
type: concept
sources: [ch07-memory-bottlenecks]
---
# Memory Bottleneck (Finetuning)

Because of the scale of foundation models, memory is a bottleneck for working with them, both for inference and for finetuning. The memory needed for finetuning is typically much higher than the memory needed for inference, because of the way neural networks are trained (AIE p.319).

The key contributors to a model's memory footprint during finetuning are its number of parameters, its number of [[trainable-parameters]], and its numerical representations (precision). The more trainable parameters a finetuning method updates, the higher its memory footprint; reducing the number of trainable parameters is the motivation behind [[peft]] (AIE p.319). Reducing numerical precision, via [[quantization]], is a separate, straightforward way to cut a model's memory footprint (AIE p.319).

Training is more sensitive to numerical precision than inference, so it is harder to train a model in low precision. Training is typically done in [[mixed-precision-training]], with some operations done in higher precision (e.g., 32-bit) and others in lower precision (e.g., 16-bit or 8-bit), whereas inference is typically done using as few bits as possible, such as 16-bit, 8-bit, or even 4-bit (AIE p.320).

## Key figures
None. The general size/precision arithmetic (e.g. 13B-parameter FP32 example) is concept-general and lives on [[quantization]]; this page states no figure of its own beyond those already placed there.

## Examples
- [[peft]]  (memory-reduction strategy: cuts trainable-parameter count)
- [[quantization]]  (memory-reduction strategy: cuts numerical precision)

## Related
- [[trainable-parameters]]  (prerequisite: memory footprint during finetuning scales with the count of trainable parameters)
- [[peft]]  (prerequisite: motivated directly by reducing this bottleneck's trainable-parameter contributor)
- [[quantization]]  (prerequisite: reducing numerical representation size is one direct fix for this bottleneck)
- [[mixed-precision-training]]  (part-of: training addresses the bottleneck by mixing precisions rather than using low precision uniformly)
- [[finetuning]]  (boundary: the bottleneck is much larger for finetuning than for inference on the same model)

## Provenance
- [[sources/ch07-memory-bottlenecks]]
