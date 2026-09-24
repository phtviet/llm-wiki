---
type: entity
sources: [ch02-domain-specific-models]
---
# Open CLIP

Open CLIP is an open replication of OpenAI's [[clip]], compared against CLIP in the book on a set of image classification benchmarks (ImageNet, Birdsnap, Country211, Oxford 102 Flowers, German Traffic Sign Recognition, Stanford Cars, UCF101) to illustrate how domain coverage affects performance across categories (AIE p.56).

## Key figures
- ViT-B/32 accuracy on ImageNet: 62.9% (vs. CLIP's 63.2%) (AIE p.56)
- ViT-B/32 accuracy on ImageNet v2: 62.6% (CLIP not reported) (AIE p.56)
- ViT-B/32 accuracy on Birdsnap: 46.0% (vs. CLIP's 37.8%) (AIE p.56)
- ViT-B/32 accuracy on Country211: 14.8% (vs. CLIP's 17.8%) (AIE p.56)
- ViT-B/32 accuracy on Oxford 102 Category Flower: 66.0% (vs. CLIP's 66.7%) (AIE p.56)
- ViT-B/32 accuracy on German Traffic Sign Recognition Benchmark: 42.0% (vs. CLIP's 32.2%) (AIE p.56)
- ViT-B/32 accuracy on Stanford Cars: 79.3% (vs. CLIP's 59.4%) (AIE p.56)
- ViT-B/32 accuracy on UCF101: 63.1% (vs. CLIP's 64.5%) (AIE p.56)

## Related
- [[clip]]  (contrast: alternative image-language embedding model benchmarked against CLIP on the same datasets)
- [[domain-specific-models]]  (example-of: benchmark comparison illustrating domain coverage gaps in general-purpose vision-language models)

## Provenance
- [[sources/ch02-domain-specific-models]]
