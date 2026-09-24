---
type: concept
sources: [ch03-perplexity, ch03-language-modeling-metrics]
---
# Perplexity

Perplexity (often shortened to PPL) is the exponential of entropy or cross entropy.
Given a dataset with true distribution P, its perplexity is PPL(P) = 2^H(P); for a
language model with learned distribution Q, PPL(P, Q) = 2^H(P,Q) (AIE p.121). If cross
entropy measures how difficult it is for a model to predict the next token, perplexity
measures the model's uncertainty when predicting the next token: higher uncertainty
means more possible options for the next token (AIE p.121).

The base of the exponent depends on the unit used for entropy. Bit (base 2) is the
conventional unit, giving PPL(P, Q) = 2^H(P,Q). Popular frameworks such as TensorFlow
and PyTorch instead use nat (natural log, base e) as the unit for entropy and cross
entropy, giving PPL(P, Q) = e^H(P,Q). Because of the resulting confusion between bit
and nat, many practitioners report perplexity rather than cross entropy when reporting
a language model's performance (AIE p.122).

A worked example: a language model trained to perfectly encode 4 position tokens has a
cross entropy of 2 bits. Predicting a position means choosing among 2^2 = 4 possible
options, so this model has a perplexity of 4 (AIE p.122).

## Key figures
- Perplexity is defined as PPL(P, Q) = 2^H(P,Q) using bit units, or e^H(P,Q) using nat units (AIE p.121-122)
- Example: cross entropy of 2 bits corresponds to a perplexity of 4 (AIE p.122)

## Related
- [[cross-entropy]]  (prerequisite: perplexity is the exponential of cross entropy)
- [[entropy]]  (prerequisite: perplexity is the exponential of entropy, and its unit, bit vs. nat, determines the exponent base)
- [[bits-per-character]]  (see-also: another cross-entropy-derived metric, each interconvertible with perplexity)
- [[bits-per-byte]]  (see-also: another cross-entropy-derived metric, each interconvertible with perplexity)

## Provenance
- [[sources/ch03-perplexity]]
