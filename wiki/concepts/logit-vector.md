---
type: concept
sources: [ch02-sampling-fundamentals]
---
# Logit Vector

Given an input, a neural network outputs a logit vector: one logit per possible value. For a [[language-model]], each logit corresponds to one token in the model's [[vocabulary]], so the logit vector's size equals the vocabulary size (AIE p.89). Larger logits correspond to higher probabilities, but logits are not themselves probabilities—they don't sum to one, and unlike probabilities they can be negative (AIE p.89-90). A [[softmax]] layer converts a logit vector into a probability distribution.

## Key figures
None.

## Related
- [[softmax]]  (prerequisite: softmax is the function used to convert logits into probabilities)
- [[vocabulary]]  (part-of: the logit vector has one entry per token in the vocabulary)
- [[sampling]]  (prerequisite: sampling draws from the probability distribution derived from the logit vector)
- [[language-model]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-sampling-fundamentals]]
