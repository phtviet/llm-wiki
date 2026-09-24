---
type: concept
sources: [ch01-from-large-language-models-to-foundation-models]
---
# Foundation Model

Foundation models are the successor category to large language models: models built to be extended and built upon for different needs, capable of working with more than just text (AIE p.9). The book uses the term to refer to both large language models and large multimodal models (AIE p.9). Foundation models mark two breaks from prior AI research. First, they cross the traditional divide by data modality: NLP handled only text, computer vision handled only images, and audio models handled only speech, whereas a foundation model can incorporate multiple modalities such as text, images, video, 3D assets, or protein structures (AIE p.8-9). Second, they mark a transition from task-specific models to general-purpose models: previously a model trained for one task (e.g., sentiment analysis) could not do another (e.g., translation), while a foundation model can do both out of the box and can further be adapted to a specific task (AIE p.10).

Adapting an existing foundation model to a task is generally far easier than building a task-specific model from scratch, though task-specific models retain benefits such as being smaller, faster, and cheaper to run (AIE p.11). The three common adaptation techniques the book covers are [[prompt-engineering]], [[retrieval-augmented-generation]], and [[finetuning]] (AIE p.10-11).

## Key figures
- Adapting a foundation model can take roughly ten examples and one weekend, versus about 1 million examples and six months to build a task-specific model from scratch (AIE p.11)

## Examples
- [[gpt-4]]  (GPT-4V understands images and text)
- [[clip]]  (multimodal embedding model, backbone of generative multimodal models)

## Related
- [[multimodal-model]]  (part-of: multimodal models are a category of foundation model, generating from more than one modality)
- [[language-model]]  (contrast: language models are text-only; foundation models extend beyond text)
- [[prompt-engineering]]  (example-of: one of three common techniques for adapting a foundation model)
- [[finetuning]]  (example-of: one of three common techniques for adapting a foundation model)
- [[retrieval-augmented-generation]]  (example-of: one of three common techniques for adapting a foundation model)

## Provenance
- [[sources/ch01-from-large-language-models-to-foundation-models]]
