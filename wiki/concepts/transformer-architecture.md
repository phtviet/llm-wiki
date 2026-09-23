---
type: concept
sources: [ch02-model-architecture]
---
# Transformer Architecture

The transformer is, as of this writing, the most dominant architecture for language-based foundation models, built on the [[attention-mechanism]] (Vaswani et al., 2017) (AIE p.58). It was developed to address two problems with the earlier [[seq2seq-architecture]]: the decoder's reliance on only a final hidden-state summary of the input, and the sequential, slow processing of RNN-based encoders/decoders (AIE p.59). Transformers dispense with RNNs entirely, letting input tokens be processed in parallel and letting the decoder attend to any prior token rather than only a compressed summary (AIE p.59).

Transformer-based autoregressive language models still face a sequential output bottleneck, so inference proceeds in two steps: **prefill**, where input tokens are processed in parallel to build the key/value intermediate state, and **decode**, where output tokens are generated one at a time (AIE p.60). These two phases motivate many inference optimization techniques discussed later in the book (AIE p.60).

A transformer model is composed of stacked **transformer blocks** (their count is called the model's number of layers), each generally containing an attention module and an [[mlp-module]], plus an embedding module before the blocks and an output layer (unembedding layer / model head) after them (AIE p.62-63). The embedding module converts tokens and positions into embedding vectors; naively, the number of position indices caps the model's maximum context length, though techniques exist to extend context length without increasing position indices (AIE p.63). A transformer model's overall size is set by its dimension, number of transformer blocks, feedforward-layer dimension, and vocabulary size (AIE p.63).

## Key figures
- Llama 2-7B has a hidden/model dimension of 4,096, so its key, value, and query matrices are each 4,096 x 4,096 (AIE p.61)
- Llama 2-7B has 32 attention heads, splitting each K/V/Q vector into 32 vectors of dimension 128 (4,096 / 32 = 128) (AIE p.61)

## Examples
- [[llama-2]]
- [[llama-3]]

## Related
- [[attention-mechanism]]  (part-of: the attention mechanism is the core computation inside each transformer block)
- [[seq2seq-architecture]]  (contrast: transformer replaces seq2seq's sequential RNN encoder/decoder with parallel attention-based processing)
- [[mlp-module]]  (part-of: each transformer block pairs an attention module with an MLP module)
- [[state-space-models]]  (contrast: alternative architecture family aiming to overcome transformer limitations, e.g. context-length scaling)
- [[inference-optimization]]  (prerequisite: prefill/decode split in transformer inference motivates optimization techniques covered elsewhere)

## Provenance
- [[sources/ch02-model-architecture]]
