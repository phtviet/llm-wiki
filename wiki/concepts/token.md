---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Token

A token is the basic unit a language model works with: a character, a word, or part of
a word (like "-tion"), depending on the model (AIE p.3). Breaking text into tokens is
called tokenization. Tokens are preferred over characters or whole words for three
reasons: they let a model break words into meaningful components (e.g., "cooking" into
"cook" and "ing"), they keep the vocabulary smaller than a word-level vocabulary would
be (improving efficiency), and they help the model process unknown or made-up words by
splitting them into recognizable pieces (AIE p.3-4). The set of all tokens a model can
work with is called its vocabulary, and the tokenization method and vocabulary size are
decided by model developers (AIE p.3).

## Key figures
- GPT-4 breaks the phrase "I can't wait to build AI applications" into nine tokens, splitting "can't" into "can" and "'t" (AIE p.3)
- For GPT-4, an average token is about ¾ the length of a word, so 100 tokens ≈ 75 words (AIE p.3)
- Mixtral 8x7B has a vocabulary size of 32,000; GPT-4's vocabulary size is 100,256 (AIE p.3)

## Related
- [[language-model]]  (prerequisite: tokens are the basic unit language models are built from)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
