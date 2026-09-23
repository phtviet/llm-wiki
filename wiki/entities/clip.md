---
type: entity
sources: [ch01-from-large-language-models-to-foundation-models]
---
# CLIP

CLIP is a language-image model developed by OpenAI (OpenAI, 2021), trained using a variant of self-supervision called natural language supervision: instead of manually generating labels for each image, OpenAI found (image, text) pairs that co-occurred on the internet (AIE p.9). CLIP is not a generative model -- it was not trained to produce open-ended outputs -- but an embedding model, trained to produce joint embeddings of both text and images (AIE p.9). It was the first model able to generalize to multiple image classification tasks without requiring additional training, and it serves as the backbone for generative multimodal models such as Flamingo, LLaVA, and Gemini (AIE p.9).

## Key figures
- Trained on a dataset of 400 million (image, text) pairs, 400 times larger than ImageNet, gathered without manual labeling cost (AIE p.9)

## Related
- [[multimodal-model]]  (example-of: a multimodal embedding model, backbone for generative multimodal models)
- [[self-supervision]]  (example-of: trained via natural language supervision, a self-supervised variant)

## Provenance
- [[sources/ch01-from-large-language-models-to-foundation-models]]
