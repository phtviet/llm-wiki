---
type: concept
sources: [ch03-cross-entropy]
---
# Cross Entropy

Cross entropy measures how difficult it is for a language model to predict what comes next in a dataset. When training on a dataset, the goal is to get the model to learn the true distribution of that data; cross entropy quantifies how far the model's learned distribution is from succeeding at this (AIE p.120).

A model's cross entropy on training data depends on two things: the training data's own predictability, measured by its entropy H(P), and how far the model's learned distribution Q diverges from the true distribution P, measured by the Kullback-Leibler (KL) divergence D_KL(P||Q). The model's cross entropy is H(P, Q) = H(P) + D_KL(P||Q). Cross entropy is not symmetric: H(P, Q) differs from H(Q, P) (AIE p.120).

A language model is trained to minimize its cross entropy with respect to the training data. If it learns the training data's distribution perfectly, its cross entropy equals the training data's entropy, and the KL divergence term becomes 0. Cross entropy can therefore be thought of as the model's approximation of the entropy of its training data (AIE p.121).

## Key figures
None. This is a mathematical/definitional concept with no load-bearing numeric figure in this section.

## Examples
None in this section.

## Related
- [[bits-per-character]]  (prerequisite: BPC is a per-character normalization of a language model's cross entropy)
- [[bits-per-byte]]  (prerequisite: bits-per-byte is derived from BPC, which is itself derived from cross entropy)
- [[language-model]]  (part-of: cross entropy is the quantity a language model is trained to minimize with respect to its training data)

## Provenance
- [[sources/ch03-cross-entropy]]
