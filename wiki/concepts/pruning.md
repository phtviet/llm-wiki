---
type: concept
sources: [ch09-model-optimization]
---
# Pruning

Pruning is a model compression technique with two distinct meanings. One removes entire nodes from a neural network, changing its architecture and reducing its parameter count. The other finds parameters least useful to predictions and sets them to zero, which does not reduce the total parameter count but increases sparsity, reducing storage and speeding up computation (AIE p.427). Pruned models can be used as-is or further finetuned to restore performance degraded by pruning. Pruning can also help discover promising smaller architectures that can be trained from scratch (Liu et al., 2018; Zhu et al., 2017) (AIE p.427).

Despite encouraging results in the literature, pruning is less common in practice as of this writing: it requires understanding the original model's architecture, its performance boost is often smaller than other approaches, and it produces sparse models that not all hardware is designed to exploit (AIE p.427).

## Key figures
- Certain pruning techniques reduce non-zero parameter counts by over 90% without compromising accuracy (Frankle and Carbin, 2019) (AIE p.427)

## Examples
None.

## Related
- [[quantization]]  (contrast: reduces numerical precision rather than zeroing/removing parameters; quantization is more popular in practice)
- [[model-distillation]]  (see-also: both spring from the idea that a large model's behavior can be captured by fewer effective parameters)

## Provenance
- [[sources/ch09-model-optimization]]
