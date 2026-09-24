---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Token

A token is the basic unit a language model works with: it can be a character, a word, or part of a word (like '-tion'), depending on the model (AIE p.3). GPT-4 breaks the phrase 'I can't wait to build AI applications' into nine tokens, splitting 'can't' into 'can' and ''t' (AIE p.3). For GPT-4, an average token is approximately three-quarters the length of a word, so 100 tokens are roughly 75 words (AIE p.3).

The set of all tokens a model can work with is its [[vocabulary]]; tokenization method and vocabulary size are decided by model developers (AIE p.3). Models use tokens rather than words or characters for three reasons: tokens let a model break words into meaningful components (e.g. 'cooking' into 'cook' and 'ing'); fewer unique tokens than unique words reduces vocabulary size and improves efficiency; and tokens help a model handle unknown or made-up words by splitting them into recognizable pieces (AIE p.4).

## Key figures
- GPT-4 splits a nine-word example phrase into 9 tokens (AIE p.3)
- An average GPT-4 token is about ¾ the length of a word; 100 tokens ≈ 75 words (AIE p.3)

## Examples
- [[gpt-4]]  (tokenizes 'I can't wait to build AI applications' into nine tokens)

## Related
- [[tokenization]]  (prerequisite: tokenization is the process that produces tokens from raw text)
- [[vocabulary]]  (part-of: the vocabulary is the set of all tokens a model can use)
- [[language-model]]  (part-of: tokens are the basic unit a language model operates on)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
