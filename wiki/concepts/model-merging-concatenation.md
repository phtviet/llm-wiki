---
type: concept
sources: [ch07-model-merging-and-multi-task-finetuning]
---
# Model Merging by Concatenation

Concatenation merges constituent models by concatenating their parameters rather than summing or stacking them. The merged component's parameter count is the sum of the constituents' counts: merging two LoRA adapters of ranks r1 and r2 produces a merged adapter of rank r1 + r2 (AIE p.356).

Concatenation is not generally recommended because it does not reduce the memory footprint compared to serving the constituent models separately; any performance gain may not justify the extra parameters (AIE p.357).

## Key figures
- Merging two LoRA adapters of rank r1 and r2 via concatenation yields a merged adapter of rank r1 + r2 (AIE p.356)

## Related
- [[model-merging]]  (part-of: concatenation is one of the three main merging approaches)
- [[model-merging-summing]]  (contrast: concatenation grows parameter count vs. summing keeps it fixed)
- [[peft]]  (example-of: LoRA adapters are the concrete case used to illustrate concatenation)

## Provenance
- [[sources/ch07-model-merging-and-multi-task-finetuning]]
