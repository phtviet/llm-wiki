---
type: entity
sources: [ch02-supervised-finetuning]
---
# InstructGPT

InstructGPT is OpenAI's model used in the book as the running example of supervised
finetuning: it was finetuned on demonstration data spanning task types like question
answering, summarization, and translation, though the training distribution did not
include multimodal tasks since InstructGPT is text-only (AIE p.81). Its demonstration
data was produced by labelers, most highly educated, writing (prompt, response) pairs
such as sentence-completion, reading-comprehension, and explanatory-answer examples
(AIE p.81).

## Key figures
- Finetuned on 13,000 (prompt, response) demonstration pairs (AIE p.82)
- ~90% of its demonstration-data labelers had at least a college degree, and more than one-third had a master's degree (AIE p.82)

## Related
- [[supervised-finetuning]]  (example-of: InstructGPT is the book's worked example of SFT on demonstration data)

## Provenance
- [[sources/ch02-supervised-finetuning]]
