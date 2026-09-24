---
type: concept
sources: [ch07-model-merging-and-multi-task-finetuning]
---
# Model Merging by Layer Stacking

Layer stacking (also called passthrough or frankenmerging) takes different layers from one or more models and stacks them on top of each other, e.g. the first layer from model 1 and the second from model 2. This can create models with unique architectures and parameter counts. Unlike summing, layer-stacked models typically need further finetuning to perform well (AIE p.354).

Layer stacking can build mixture-of-experts models via sparse upcycling (Komatsuzaki et al., 2022): take a pre-trained model, copy certain layers or modules multiple times, add a router to send each input to the most suitable copy, then further train the merged model and router together. Komatsuzaki et al. showed this can outperform MoE models trained from scratch; Together AI used the approach to mix six weaker open source models into Mixture-of-Agents, achieving performance comparable to GPT-4o on some benchmarks (Wang et al., 2024) (AIE p.354).

A related use case is **model upscaling** -- creating a larger model from an existing one using fewer resources than training from scratch, useful when new hardware allows serving a bigger model than originally targeted. One upscaling approach, **depthwise scaling**, copies the original pre-trained model, merges the two copies by summing some layers and stacking the rest (chosen to hit a target size), then further trains the result (AIE p.355).

## Key figures
None at the concept level; see [[goliath-120b]] and [[solar-10-7b]] for model-specific figures.

## Examples
- [[goliath-120b]]  (early frankenmerging success)
- [[solar-10-7b]]  (depthwise-scaling upscaling example)

## Related
- [[model-merging]]  (part-of: layer stacking is one of the three main merging approaches)
- [[model-merging-summing]]  (contrast: stacking arranges layers spatially vs. summing combines parameter values directly)
- [[mixture-of-experts]]  (prerequisite: sparse upcycling uses layer stacking plus a router to build an MoE model from a dense checkpoint)

## Provenance
- [[sources/ch07-model-merging-and-multi-task-finetuning]]
