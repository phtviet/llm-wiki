---
type: concept
sources: [ch01-from-large-language-models-to-foundation-models]
---
# Multimodal Model

A multimodal model is a model that can work with more than one data modality, for example text and images (AIE p.9). Where a language model generates the next token conditioned only on preceding text tokens, a multimodal model generates the next token conditioned on tokens from multiple modalities -- text and image, or whichever modalities it supports (AIE p.9). A generative multimodal model is also called a large multimodal model (LMM) (AIE p.9).

Multimodal models need data to scale, and self-supervision extends to them as well. OpenAI trained its language-image model [[clip]] using a variant of self-supervision called natural language supervision, pairing images with text that co-occurred on the internet rather than manually labeling images (AIE p.9). Multimodal embedding models like CLIP serve as the backbone for generative multimodal models such as Flamingo, LLaVA, and Gemini (AIE p.9).

## Key figures
None. (CLIP's dataset-size figures are entity-specific and live on [[clip]].)

## Examples
- [[clip]]  (embedding model trained via natural language supervision on image-text pairs; backbone for generative multimodal models)

## Related
- [[foundation-model]]  (part-of: multimodality is a defining trait of most foundation models)
- [[self-supervision]]  (prerequisite: natural language supervision is a self-supervised variant used to train multimodal models)
- [[language-model]]  (contrast: conditions next-token generation on text only, vs. multimodal models conditioning on multiple modalities)

## Provenance
- [[sources/ch01-from-large-language-models-to-foundation-models]]
