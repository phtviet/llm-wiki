---
type: concept
sources: [ch03-bits-per-character-and-bits-per-byte]
---
# Bits-per-Character (BPC)

Bits-per-character is a unit derived from a language model's [[cross-entropy]] that
normalizes for differing [[tokenization]] schemes. Because models tokenize text
differently (e.g. one using words as tokens, another using characters), the number of
bits needed per token is not directly comparable across models. BPC instead measures
the number of bits needed per character: if a model's cross entropy is 6 bits per
token and each token averages 2 characters, its BPC is 6/2 = 3 (AIE p.121).

BPC has a complication: it depends on the character encoding scheme used, since
different schemes use different numbers of bits per character. For example, ASCII
encodes each character with 7 bits, while UTF-8 uses anywhere from 8 to 32 bits per
character, making BPC values encoding-dependent and not fully standardized (AIE p.121).

## Key figures
- Example: cross entropy of 6 bits/token with 2 characters/token gives a BPC of 3 (AIE p.121)
- ASCII encodes each character using 7 bits (AIE p.121)

## Examples
None.

## Related
- [[bits-per-byte]]  (prerequisite: BPC is converted into BPB to correct for encoding-scheme dependence)
- [[language-model]]  (part-of: BPC measures a language model's per-character compression efficiency)
- [[cross-entropy]]  (see-also: mentioned in this page's text)
- [[tokenization]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch03-bits-per-character-and-bits-per-byte]]
