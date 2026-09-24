---
type: concept
sources: [ch01-from-large-language-models-to-foundation-models]
---
# Multimodal Model

A multimodal model is a model that can work with more than one data modality (AIE p.9). Where a [[language-model]] generates the next token conditioned only on preceding text tokens, a multimodal model generates the next token conditioned on both text and image tokens, or whichever modalities it supports (AIE p.9). A generative multimodal model is also called a large multimodal model (LMM) (AIE p.9).

Multimodal models need data to scale, and self-supervision extends to them as it does to language models. OpenAI trained its language-image model [[clip]] using a variant of self-supervision called natural language supervision, pairing images with co-occurring text found on the internet rather than manually generating labels (AIE p.9).

Not all multimodal models are generative: [[clip]] is an embedding model rather than a generative one, and multimodal embedding models like it serve as the backbones of generative multimodal models such as Flamingo, LLaVA, and Gemini (AIE p.9).

## Key figures
None. The dataset-scale figure (400 million image-text pairs) is CLIP-specific and lives on the CLIP entity page per fact-placement.

## Examples
- [[clip]]  (multimodal embedding model trained via natural language supervision)
- [[gpt-4]]  (GPT-4V understands images and text)

## Related
- [[foundation-model]]  (part-of: multimodal models are a category of foundation model)
- [[self-supervision]]  (prerequisite: multimodal models scale using self-supervision, as language models do)
- [[clip]]  (example-of: the book's example multimodal embedding model)
- [[language-model]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch01-from-large-language-models-to-foundation-models]]
