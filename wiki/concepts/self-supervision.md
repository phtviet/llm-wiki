---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Self-Supervision

Self-supervision is a training approach in which a model infers labels directly from
the input data instead of requiring explicit human-provided labels, overcoming the data
labeling bottleneck that limits supervised learning and letting models scale up on much
larger datasets (AIE p.6). Language modeling is self-supervised because each input
sequence supplies both the labels (the tokens to be predicted) and the context used to
predict them (AIE p.6-7). For example, the sentence "I love street food." yields six
training samples, each an input context paired with the next token as output, using
`<BOS>` and `<EOS>` markers to mark sequence boundaries -- the end-of-sequence marker in
particular helps a language model know when to stop generating (AIE p.7).

This contrasts with supervision, where labeled examples (e.g., transactions tagged
"fraud"/"not fraud") are used to train a model, and where labeling cost scales with
dataset size and category count -- AlexNet, which started the deep learning revolution,
was trained this way on ImageNet (Krizhevsky et al., 2012) (AIE p.6).

## Key figures
- Labeling 1 million images at 5 cents each would cost $50,000; scaling to 1 million categories would raise labeling cost to about $50 million (AIE p.6)
- AlexNet was trained to classify over 1 million images into 1,000 categories (AIE p.6)
- The sentence "I love street food." produces six training samples for self-supervised language modeling (AIE p.7)

## Related
- [[language-model]]  (prerequisite: self-supervision is what let language models scale to their current size)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
