---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Language Model

A language model encodes statistical information about one or more languages: given a
context, it tells us how likely a word or token is to appear next (AIE p.2). The
statistical nature of language is not new — Sherlock Holmes's letter-frequency analysis
in "The Adventure of the Dancing Men" and Claude Shannon's 1951 "Prediction and Entropy
of Printed English" both exploit it, and concepts from Shannon's paper, such as
entropy, are still used in language modeling today (AIE p.3). Early language models
covered a single language; today a model can span multiple languages (AIE p.3).

The basic unit of a language model is the [[token]], and the set of all tokens a model
can use is its vocabulary (AIE p.3). A language model can be thought of as a completion
machine: given a prompt, it tries to complete the text, and this framing makes
translation, summarization, coding, and classification all expressible as completion
tasks (AIE p.5). Completions are probabilistic predictions, not guaranteed correct, and
completing text is not the same as engaging in conversation — a completion machine may
respond to a question with another question rather than an answer, a gap that
post-training addresses (AIE p.5).

A model that produces open-ended output from a fixed, finite vocabulary is called
generative, which is the origin of the term generative AI (AIE p.5). There are two main
types of language models, distinguished by what context they use to predict a token:
[[masked-language-model]] and [[autoregressive-language-model]] (AIE p.4). Unless
otherwise stated, the book uses "language model" to mean an autoregressive model
(AIE p.5).

## Key figures
None. Figures here are token/vocabulary-specific and live on [[token]].

## Examples
- [[masked-language-model]]  (predicts missing tokens using both preceding and following context)
- [[autoregressive-language-model]]  (predicts the next token using only preceding context)

## Related
- [[token]]  (prerequisite: tokens are the basic unit language models operate on)
- [[self-supervision]]  (prerequisite: self-supervision is the training approach that let language models scale to today's size)
- [[masked-language-model]]  (part-of: one of the two main types of language model)
- [[autoregressive-language-model]]  (part-of: one of the two main types of language model; the book's default sense of "language model")

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
