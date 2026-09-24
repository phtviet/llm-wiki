---
type: concept
sources: [ch03-entropy]
---
# Entropy

Entropy measures how much information, on average, a token carries. The higher a
language's entropy, the more information each token carries, and the more bits are
needed to represent a token. Claude Shannon introduced entropy in 1951 using
characters as tokens, describing it as the average number of binary digits needed per
letter of a language when translated into binary in the most efficient way (AIE p.119).

Entropy also measures how difficult it is to predict what comes next in a language: the
lower a language's entropy, the more predictable it is, since a token then carries less
information. A language with only two tokens (upper/lower) needs just one bit per
token and has entropy 1; a language with four tokens (upper-left, upper-right,
lower-left, lower-right) needs two bits per token and has entropy 2 -- higher entropy
since each token carries more information but requires more bits to represent (AIE
p.119-120).

A [[language-model]] encodes statistical information about how likely a token is to
appear in a given context; the better it learns this distribution, the better it
predicts what comes next in the training data, and the lower its training
[[cross-entropy]] (AIE p.119). Entropy underlies [[cross-entropy]], [[perplexity]],
[[bits-per-character]], and [[bits-per-byte]] -- all four metrics are closely related,
and knowing one lets you compute the other three given the necessary information
(AIE p.119).

## Key figures
- Two-token language (upper/lower): 1 bit per token, entropy 1 (AIE p.119)
- Four-token language (upper-left/upper-right/lower-left/lower-right): 2 bits per token, entropy 2 (AIE p.120)

## Related
- [[cross-entropy]]  (prerequisite: entropy is the base concept cross-entropy builds on)
- [[language-model]]  (see-also: a language model's quality is measured by how well it minimizes entropy/cross-entropy on data)
- [[bits-per-character]]  (prerequisite: BPC is a per-character normalization derived from entropy-related cross-entropy)
- [[bits-per-byte]]  (prerequisite: BPB is a standardized derivative of the same entropy-related metrics)

## Provenance
- [[sources/ch03-entropy]]
