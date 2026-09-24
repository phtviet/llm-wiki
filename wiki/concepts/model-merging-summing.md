---
type: concept
sources: [ch07-model-merging-and-multi-task-finetuning]
---
# Model Merging by Summing

Summing is a model-merging approach that adds the weight values of constituent models together. If the models' parameters are on different scales, they can be rescaled before summing so their values fall in the same range (AIE p.350). The book covers two summing methods: linear combination and spherical linear interpolation (SLERP), and a pruning step used before merging.

**Linear combination** includes both simple averaging and weighted averaging: Merge(A, B) = (wA*A + wB*B) / (wA + wB). The idea of linearly combining multiple models dates to the early 1990s (Perrone, 1993) and is often used in federated learning (Wang et al., 2020). Model soups (Wortsman et al., 2022) showed that averaging the entire weights of multiple finetuned models can improve accuracy without increasing inference time, though it is more common to linearly combine specific components such as adapters (AIE p.350-351).

Linear combination is most effective for models finetuned on the same base model, where it can be understood via **task vectors** (also called delta parameters): subtracting the base model from a finetuned model gives a vector capturing the task's essence. Task vectors support **task arithmetic** (Ilharco et al., 2022) -- adding task vectors to combine capabilities, or subtracting one to remove an undesirable behavior such as an invasive capability or a pre-training bias. If finetuning uses LoRA, the task vector can be constructed from the LoRA weights. Linear combination can also work across differing architectures or sizes by projecting layers into a shared dimension, and some approaches align models before averaging so functionally related parameters combine together, though alignment is challenging and less common than naive linear combination (AIE p.351-352).

**Spherical linear interpolation (SLERP)** treats each model component as a point on a sphere and interpolates along the shortest path between two such points, with an interpolation factor between 0 and 1 controlling how close the merged result sits to each source (a factor of 0.5 is the exact midpoint). SLERP is defined for only two vectors at a time; merging more than two requires applying it sequentially (AIE p.352).

**Pruning redundant task-specific parameters**: most parameter adjustments made during finetuning are minor and do not meaningfully affect task performance. TIES-Merging (Yadav et al., 2023) and DARE (Yu et al., 2023) prune these redundant task-vector parameters -- resetting them to the base model's original value -- before merging, which significantly improves merged-model quality; pruning matters more as more models are merged, since there are more chances for one task's redundant parameters to interfere with another's (AIE p.353).

## Key figures
- Yadav et al. found that keeping the top 20% of task vector parameters gives performance comparable to keeping 100% (AIE p.353)

## Examples
- None named beyond the techniques themselves.

## Related
- [[model-merging]]  (part-of: summing is one of the three main merging approaches)
- [[model-merging-layer-stacking]]  (contrast: summing combines parameter values directly vs. layer stacking arranges layers spatially)
- [[peft]]  (prerequisite: task vectors can be constructed from LoRA adapter weights)

## Provenance
- [[sources/ch07-model-merging-and-multi-task-finetuning]]
