---
type: concept
sources: [ch02-model-architecture]
---
# Seq2seq

Seq2seq (sequence-to-sequence) is an architecture introduced in 2014 that provided significant improvements on machine translation and summarization. It contains an encoder that processes input tokens and a decoder that generates output tokens, both as sequences of tokens. Seq2seq uses RNNs (recurrent neural networks) as its encoder and decoder: in its basic form, the encoder processes input tokens sequentially into a final hidden state, and the decoder generates output tokens sequentially, conditioned on that hidden state and the previously generated token (AIE p.58).

In 2016 Google incorporated seq2seq into Google Translate, an update it claimed gave the 'largest improvements to date for machine translation quality,' making seq2seq the go-to architecture for text-sequence tasks (AIE p.58). Seq2seq has two key limitations: the decoder relies only on the input's final hidden state (limiting output quality), and its RNN structure forces sequential processing, which is slow for long sequences. RNNs are also especially prone to vanishing and exploding gradients due to their recursive structure (AIE p.58-59). These limitations motivated the [[transformer-architecture]], and seq2seq's popularity lasted roughly 2014-2018 (AIE p.65).

## Key figures
None.

## Related
- [[transformer-architecture]]  (contrast: transformer replaces seq2seq's sequential RNNs with parallelizable attention; prerequisite: transformer was designed to fix seq2seq's problems)
- [[attention-mechanism]]  (boundary: attention was first used to augment seq2seq, e.g. Google's GNMT, three years before the transformer paper showed it could replace RNNs entirely)

## Provenance
- [[sources/ch02-model-architecture]]
