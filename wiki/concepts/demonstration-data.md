---
type: concept
sources: [ch02-supervised-finetuning]
---
# Demonstration Data

Demonstration data consists of (prompt, response) pairs that show a model examples of appropriate responses, used to train it to converse rather than merely complete text. Since a pre-trained model is optimized for completion, it has no concept that a prompt is meant to start a conversation; demonstration data teaches it the desired behavior. Some call this process behavior cloning: labelers demonstrate how the model should behave, and the model clones this behavior (AIE p.80).

Demonstration data should span the range of request types the model is meant to handle, such as question answering, summarization, and translation (AIE p.80). Unlike traditional data labeling, which often needs little domain expertise, demonstration data can require complex responses involving critical thinking, information gathering, and judgment about the appropriateness of a request, so companies often use highly educated labelers to produce it (AIE p.81-82).

Generating demonstration data is expensive: a single (prompt, response) pair can take up to 30 minutes to write, especially for long-context tasks like summarization (AIE p.82). Teams seeking cheaper alternatives to high-quality human annotation are increasingly turning to AI-generated (synthetic) data (AIE p.82).

## Key figures
- Generating one (prompt, response) pair can take up to 30 minutes (AIE p.82)
- At $10 per pair, InstructGPT's 13,000 demonstration pairs would cost $130,000, excluding data design, labeler recruiting, and quality control (AIE p.82)

## Examples
- [[instructgpt]]  (OpenAI's demonstration-data distribution across task types)
- [[laion]]  (volunteer-generated multilingual demonstration conversations)

## Related
- [[supervised-finetuning]]  (part-of: demonstration data is the training data used in the supervised finetuning step)
- [[data-synthesis]]  (contrast: AI-generated synthetic data as an alternative to costly human-annotated demonstration data; see-also: discussed further in a later chapter)

## Provenance
- [[sources/ch02-supervised-finetuning]]
