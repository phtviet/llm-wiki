---
type: concept
sources: [ch02-model-architecture]
---
# Seq2seq Architecture

Seq2seq (sequence-to-sequence) is an earlier architecture that provided significant improvements on machine translation and summarization when introduced in 2014, and became the go-to architecture for text-sequence tasks after Google incorporated it into Google Translate in 2016, claiming the "largest improvements to date for machine translation quality" (AIE p.58). Seq2seq contains an encoder that processes input tokens and a decoder that generates output tokens, both using RNNs (recurrent neural networks) (AIE p.58). In its basic form, the encoder processes input tokens sequentially into a final hidden state, and the decoder generates output tokens sequentially, conditioned on that final hidden state and the previously generated token (AIE p.58).

Seq2seq has two key problems that the [[transformer-architecture]] was created to solve: the decoder generates outputs using only the final hidden state of the input (like summarizing a book from only its summary), and the RNN encoder/decoder process sequentially, making it slow for long sequences (AIE p.59). RNNs are also especially prone to vanishing and exploding gradients due to their recursive structure, which makes learning difficult over many steps (AIE p.59). Seq2seq was the dominant architecture for about four years (2014-2018) before being displaced (AIE p.65).

## Key figures
None.

## Related
- [[transformer-architecture]]  (contrast: transformer replaces seq2seq's sequential RNN processing with parallelizable attention)
- [[attention-mechanism]]  (prerequisite: attention was first paired with seq2seq's RNN architecture before being used standalone in the transformer)

## Provenance
- [[sources/ch02-model-architecture]]
