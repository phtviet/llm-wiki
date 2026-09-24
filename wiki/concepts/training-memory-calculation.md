---
type: concept
sources: [ch07-memory-math]
---
# Training Memory Calculation

Training requires memory for the model's weights and activations (as in inference) plus memory for gradients and optimizer states, which scales with the number of trainable parameters: training memory = model weights + activations + gradients + optimizer states (AIE p.323).

During the backward pass, each trainable parameter needs one value for its gradient plus zero to two additional values for optimizer state, depending on the optimizer: a vanilla SGD optimizer stores no additional state, a momentum optimizer stores one value per trainable parameter, and an [[adam-optimizer]] stores two values per trainable parameter (AIE p.323).

The formula assumes activation memory is smaller than weight memory, but in practice, if activations are stored for gradient computation, activation memory can dwarf weight memory, as shown for Megatron models at different scales (Korthikanti et al., 2022) (AIE p.324).

## Key figures
- Adam optimizer: 3 values per trainable parameter (1 gradient + 2 optimizer states) (AIE p.323)
- 13B trainable parameters with Adam at 2 bytes/value: 13B x 3 x 2 bytes = 78 GB for gradients and optimizer states (AIE p.323)
- 1B trainable parameters with Adam at 2 bytes/value: 1B x 3 x 2 bytes = 6 GB for gradients and optimizer states (AIE p.323)

## Examples
- [[adam-optimizer]]  (dominant optimizer for transformer models; stores 2 values per trainable parameter)

## Related
- [[inference-memory-calculation]]  (contrast: training adds gradient and optimizer-state memory on top of the weights-plus-activations footprint used for inference)
- [[trainable-parameters]]  (prerequisite: the number of trainable parameters determines gradient and optimizer-state memory)
- [[gradient-checkpointing]]  (see-also: technique to reduce activation memory during training at the cost of recomputation time)
- [[memory-bottleneck]]  (part-of: training memory footprint is the larger half of the memory-bottleneck comparison between finetuning and inference)
- [[adam-optimizer]]  (example-of: concrete optimizer whose 2-value-per-parameter state is used in the worked training memory examples)

## Provenance
- [[sources/ch07-memory-math]]
