---
type: concept
sources: [ch03-bits-per-character-and-bits-per-byte]
---
# Bits-per-Byte (BPB)

Bits-per-byte is a more standardized metric than [[bits-per-character]] for measuring
how many bits a language model needs to represent one byte of the original training
data, correcting for the fact that BPC varies with character encoding scheme. Given a
BPC of 3 and a character encoded in 7 bits (7/8 of a byte), the BPB is 3 / (7/8) = 3.43
(AIE p.121).

Cross entropy, and therefore BPB, indicates how efficiently a language model can
compress text. A BPB of 3.43 means the model can represent each original byte (8 bits)
using only 3.43 bits, i.e. it can compress the original training text to less than half
its original size (AIE p.121).

## Key figures
- Example: BPC of 3 with 7-bit characters gives a BPB of 3 / (7/8) = 3.43 (AIE p.121)
- A BPB of 3.43 compresses text to less than half its original size (AIE p.121)

## Examples
None.

## Related
- [[bits-per-character]]  (prerequisite: BPB is derived from BPC, adjusted for the bits-per-character encoding scheme)
- [[language-model]]  (part-of: BPB measures a language model's data-compression efficiency)

## Provenance
- [[sources/ch03-bits-per-character-and-bits-per-byte]]
