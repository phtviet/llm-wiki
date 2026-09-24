---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Evaluation

Evaluation is about mitigating risks and uncovering opportunities, and is needed throughout the model adaptation process: to select models, benchmark progress, decide whether an application is ready for deployment, and detect issues and opportunities in production (AIE p.44). It has always mattered in ML engineering but matters even more with foundation models, chiefly because of their open-ended nature and expanded capabilities (AIE p.44).

In close-ended traditional ML tasks (e.g. fraud detection) there is usually an expected ground truth to compare a model's output against. Open-ended tasks like chatbot responses have so many possible valid outputs that curating an exhaustive set of ground truths to compare against is impossible (AIE p.44).

The existence of many adaptation techniques also complicates evaluation, since a system's apparent performance can shift dramatically with the technique used to evaluate it. See [[gemini-mmlu-prompting-comparison]] for the book's worked example of this using Gemini and ChatGPT on the MMLU benchmark (AIE p.44-45).

## Key figures
None.

## Related
- [[application-development]]  (part-of: one of its three responsibilities)
- [[prompt-engineering]]  (see-also: choice of prompting technique can swing evaluation results dramatically)
- [[gemini-mmlu-prompting-comparison]]  (example-of: the book's illustration of evaluation results shifting with prompting technique)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
