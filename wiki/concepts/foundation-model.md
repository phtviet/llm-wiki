---
type: concept
sources: [ch01-from-large-language-models-to-foundation-models]
---
# Foundation Model

A foundation model is a model built on such scale that it can be adapted to a wide range of downstream tasks, marking a break from the earlier structure of AI research where fields were divided by data modality: NLP handled only text, computer vision only images, and audio-only models handled speech recognition and synthesis (AIE p.9). Many models still popularly called "LLMs," such as Gemini and GPT-4V, are better characterized as foundation models because they extend beyond text into other modalities and can be built upon for many different needs -- hence "foundation" (AIE p.9). This book uses "foundation models" to refer to both large language models and large multimodal models (AIE p.9).

Foundation models also mark the shift from task-specific models to general-purpose models. A model previously trained for sentiment analysis could not also do translation; a foundation model, out of the box, can perform relatively well across many tasks, and can further be adapted -- via [[prompt-engineering]], [[retrieval-augmented-generation]], or [[finetuning]] -- to maximize performance on a specific task (AIE p.10-11).

## Key figures
None.

## Examples
- [[clip]]  (embedding-based foundation model, not generative)
- GPT-4V, Claude 3, Gemini -- multimodal foundation models mentioned as examples

## Related
- [[language-model]]  (prerequisite: foundation models extend language models to more modalities and general-purpose scale)
- [[multimodal-model]]  (part-of: incorporating additional modalities is a defining feature of most foundation models)
- [[self-supervision]]  (prerequisite: scaling foundation models to this size relies on self-supervised training on massive unlabeled data)
- [[prompt-engineering]]  (example-of: one of the common techniques for adapting a foundation model to a specific need)
- [[retrieval-augmented-generation]]  (example-of: another common adaptation technique, supplementing instructions with a database)
- [[finetuning]]  (example-of: further training a foundation model on task-specific data)

## Provenance
- [[sources/ch01-from-large-language-models-to-foundation-models]]
