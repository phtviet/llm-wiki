---
type: entity
sources: [ch01-from-large-language-models-to-foundation-models]
---
# CLIP

CLIP is OpenAI's language-image model, trained using a variant of self-supervision called natural language supervision (OpenAI, 2021) (AIE p.9). Instead of manually labeling images, OpenAI found (image, text) pairs that co-occurred on the internet to build its training data (AIE p.9). CLIP is not a generative model; it is an embedding model, trained to produce joint embeddings of text and images (AIE p.9). It was the first model able to generalize to multiple image classification tasks without requiring additional training (AIE p.9). Multimodal embedding models like CLIP serve as the backbones of generative multimodal models such as Flamingo, LLaVA, and Gemini (AIE p.9).

## Key figures
- Trained on a dataset of 400 million (image, text) pairs, 400 times larger than ImageNet, gathered without manual labeling cost (AIE p.9)

## Related
- [[multimodal-model]]  (example-of: CLIP is the book's example multimodal embedding model)
- [[self-supervision]]  (example-of: CLIP's natural language supervision is a variant of self-supervision)
- [[gpt-4]]  (contrast: CLIP is an embedding model, not generative, unlike generative multimodal models such as GPT-4V)

## Provenance
- [[sources/ch01-from-large-language-models-to-foundation-models]]
