---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Language Model

A language model encodes statistical information about one or more languages: intuitively, how likely a word or token is to appear in a given context (AIE p.2). The statistical nature of language was recognized long before modern computing -- Sherlock Holmes decoding stick figures in 'The Adventure of the Dancing Men' and Claude Shannon's 1951 paper 'Prediction and Entropy of Printed English' both exploit it (AIE p.2). Early language models covered a single language; today a language model can span multiple languages (AIE p.2).

The basic unit of a language model is the [[token]], and the process of splitting text into tokens is [[tokenization]]. There are two main types of language model, distinguished by what context they use to predict a token: the [[masked-language-model]], which predicts missing tokens using context from both directions, and the [[autoregressive-language-model]], which predicts the next token using only preceding tokens (AIE p.4). Unless stated otherwise, the book uses 'language model' to mean an autoregressive model (AIE p.5).

A language model's outputs are open-ended -- it uses a fixed, finite vocabulary to construct effectively infinite possible outputs, which is why such models are called generative (AIE p.5). It can be thought of as a completion machine: given a prompt, it predicts a completion, and that completion is a probabilistic guess, not a guaranteed-correct answer (AIE p.5). Many tasks -- translation, summarization, coding, math, spam classification -- can be framed as completion tasks (AIE p.5-6). Completion is distinct from holding a conversation: a completion machine asked a question may complete it with another question rather than answering (AIE p.6).

Language models became the center of the scaling approach behind the ChatGPT moment because they can be trained with [[self-supervision]], unlike many other ML models that require labeled supervision (AIE p.6). A model's scale is typically measured by its number of [[model-parameters]] (AIE p.7).

## Key figures
None. Figures in this section are entity- or example-specific (GPT-4's tokenization, GPT/GPT-2 parameter counts) and are recorded on those pages/concepts.

## Examples
- [[bert]]  (masked language model)
- [[gpt-4]]  (autoregressive model; tokenizes text into subword units)

## Related
- [[token]]  (part-of: tokens are the basic unit a language model operates on)
- [[tokenization]]  (prerequisite: text must be tokenized before a language model can process it)
- [[masked-language-model]]  (part-of: one of the two main types of language model)
- [[autoregressive-language-model]]  (part-of: the other main type, and the book's default sense of 'language model')
- [[self-supervision]]  (prerequisite: self-supervision is what let language models scale to become LLMs)
- [[model-parameters]]  (part-of: model size is measured by parameter count)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
