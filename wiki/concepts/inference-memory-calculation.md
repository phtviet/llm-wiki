---
type: concept
sources: [ch07-memory-math]
---
# Inference Memory Calculation

During inference, only the forward pass runs, so memory is needed for the model's weights plus activation values. Given parameter count N and memory per parameter M, the weight memory is N x M. Activation and key-value vector memory for the [[attention-mechanism]] grows linearly with sequence length and [[batch-size]], but for many applications can be approximated as 20% of the weight memory, bringing the total footprint to N x M x 1.2 (AIE p.322).

A model's memory footprint grows rapidly with size, making memory a bottleneck for operating larger models (AIE p.323).

## Key figures
- Total inference memory approximated as N x M x 1.2, where the 0.2 term covers activation and key-value vector memory (AIE p.322)
- A 13B-parameter model at 2 bytes/parameter needs 26 GB for weights and 31.2 GB total for inference (AIE p.322)
- A 70B-parameter model at 2 bytes/parameter needs 140 GB just for its weights (AIE p.323)

## Examples
- [[adam-optimizer]]  (contrast: relevant to training memory, not inference)

## Related
- [[training-memory-calculation]]  (contrast: covers the separate training memory profile, which adds gradients and optimizer states on top of weights and activations)
- [[model-parameters]]  (prerequisite: parameter count N is the base variable in the inference memory formula)
- [[memory-bottleneck]]  (part-of: inference memory footprint is one half of the memory-bottleneck comparison between finetuning and inference)
- [[quantization]]  (see-also: reducing bytes per parameter M directly shrinks inference memory footprint)
- [[attention-mechanism]]  (see-also: mentioned in this page's text)
- [[batch-size]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch07-memory-math]]
