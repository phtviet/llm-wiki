---
type: concept
sources: [ch02-model-architecture]
---
# Transformer Architecture

The transformer architecture (Vaswani et al., 2017) is, as of this writing, the most dominant architecture for language-based foundation models. It is based on the [[attention-mechanism]] and was popularized on the heels of [[seq2seq]]'s success on machine translation and summarization (AIE p.58).

Seq2seq had two problems the transformer addresses. First, its decoder generated outputs using only the final hidden state of the input, limiting output quality -- like generating answers about a book using only its summary. Second, seq2seq's RNN encoder and decoder processed tokens sequentially, making it slow for long sequences. The transformer's attention mechanism lets the model weigh the importance of any input token when generating each output token -- like referencing any page of the book rather than just its summary -- and dispenses with RNNs entirely, so input tokens can be processed in parallel (AIE p.59).

While the transformer removes the sequential input bottleneck, transformer-based autoregressive models still have a sequential output bottleneck. Inference therefore has two steps: prefill, where the model processes input tokens in parallel to build the intermediate key/value state; and decode, where the model generates one output token at a time (AIE p.60).

A transformer model is composed of multiple [[transformer-block]]s, plus an embedding module before them and an output layer after them. [[model-size]] is determined by the model's dimension, the number of transformer blocks, the feedforward dimension, and the vocabulary size (AIE p.62-63). The transformer has proven unusually durable: it has dominated since 2017, longer than seq2seq (2014-2018) or GANs (2014-2019), because a replacement architecture must perform at the scale and on the hardware people already care about (AIE p.65).

## Key figures
None. Model-specific dimension figures (e.g. Llama 2/3 sizes) live on the Llama entity page; general architectural claims here carry no single load-bearing number of their own.

## Examples
- [[llama-2]]  (dimension values illustrating transformer scaling)

## Related
- [[seq2seq]]  (prerequisite: transformer was created to address seq2seq's limitations; contrast: parallel attention vs. sequential RNN processing)
- [[attention-mechanism]]  (part-of: attention is the core mechanism inside each transformer block)
- [[transformer-block]]  (part-of: transformer blocks are the repeated building unit of the architecture)
- [[state-space-models]]  (contrast: alternative architecture family aiming to address transformer limitations, e.g. context scaling)
- [[model-size]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-model-architecture]]
