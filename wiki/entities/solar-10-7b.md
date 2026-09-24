---
type: entity
sources: [ch07-model-merging-and-multi-task-finetuning]
---
# SOLAR 10.7B

SOLAR 10.7B (Kim et al., 2023) is a model created via depthwise scaling, a layer-stacking upscaling technique, from a single 7B-parameter model with 32 layers. The procedure copies the original pre-trained model, merges the two copies by summing 16 carefully selected layers and stacking the rest, then further trains the upscaled model toward target performance (AIE p.355).

## Key figures
- Built from a 7B-parameter, 32-layer base model; 16 layers are summed, leaving a final model of 32 x 2 - 16 = 48 layers (AIE p.355)

## Related
- [[model-merging-layer-stacking]]  (example-of: depthwise-scaling model-upscaling case)

## Provenance
- [[sources/ch07-model-merging-and-multi-task-finetuning]]
