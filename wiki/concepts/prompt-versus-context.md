---
type: concept
sources: [ch05-in-context-learning-zero-shot-and-few-shot]
---
# Prompt Versus Context (Terminology)

'Prompt' and 'context' are sometimes used interchangeably, but the book distinguishes them. In the GPT-3 paper (Brown et al., 2020), context referred to the entire input into a model, making it synonymous with prompt. Others argue context is only part of the prompt: the information a model needs to perform what the prompt asks, i.e. contextual information. Google's PaLM 2 documentation defines context differently still, as the description shaping how a model responds throughout a conversation -- for example specifying words the model can or cannot use, topics to focus on or avoid, or response format or style -- making context equivalent to a task description (AIE p.214).

The book adopts its own convention: prompt refers to the whole input into the model, and context refers specifically to the information provided so the model can perform a given task (AIE p.214).

## Key figures
None.

## Examples
(none)

## Related
- [[in-context-learning]]  (prerequisite: understanding in-context learning requires knowing what 'context' means in this book's usage)
- [[prompt-engineering]]  (part-of: prompt/context terminology underlies how prompt engineering is discussed)

## Provenance
- [[sources/ch05-in-context-learning-zero-shot-and-few-shot]]
