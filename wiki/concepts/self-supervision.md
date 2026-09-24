---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Self-Supervision

Self-supervision is a training approach in which a model infers labels directly from the input data, instead of relying on explicit human-provided labels (AIE p.6). Language modeling is self-supervised because each input sequence supplies both the labels (the tokens to be predicted) and the context used to predict them: the sentence 'I love street food.' alone yields six training samples of (context, next-token) pairs (AIE p.7).

Self-supervision overcomes the data-labeling bottleneck of [[supervision]], since text sequences are abundant (books, blog posts, articles, comments) and require no manual labeling, letting language models scale up to become LLMs (AIE p.7). Self-supervision is distinct from unsupervised learning: in self-supervised learning labels are inferred from the input; in unsupervised learning no labels are used at all (AIE p.7).

Beginning- and end-of-sequence markers (<BOS>, <EOS>) are typically treated as special tokens so a model can work with multiple sequences and know when to stop generating (AIE p.7).

## Key figures
None.

## Examples
- [[gpt-4]]  (autoregressive model whose scale was enabled by self-supervised training)

## Related
- [[supervision]]  (contrast: requires labeled data vs. infers labels from the input itself)
- [[language-model]]  (prerequisite: self-supervision is what enabled language models to scale into LLMs)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
