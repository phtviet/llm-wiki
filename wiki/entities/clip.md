---
type: entity
sources: [ch01-three-layers-of-the-ai-stack, ch02-domain-specific-models]
---
# CLIP

CLIP is OpenAI's embedding model trained on 400 million image-text pairs via natural language supervision. It maps images and text into a shared embedding space.

The book uses CLIP (and Open CLIP) benchmark performance across image datasets to illustrate how a model's domain coverage can be inferred from its benchmark results, given the lack of direct domain-distribution analyses for vision data (AIE p.56).

## Key figures
- Trained on 400M image-text pairs
- Accuracy of ViT-B/32 (OpenAI) on benchmarks: ImageNet 63.2, Birdsnap 37.8, Country211 17.8, Oxford 102 Flower 66.7, German Traffic Sign Recognition 32.2, Stanford Cars 59.4, UCF101 64.5 (AIE p.56)

## Related
- [[domain-specific-models]]  (example-of: benchmark performance used to infer a general-purpose model's domain coverage)
- [[foundation-model]]  (part-of: an embedding model built on a foundation-model-scale training set)

## Provenance
- [[sources/ch01-three-layers-of-the-ai-stack]]
- [[sources/ch02-domain-specific-models]]
