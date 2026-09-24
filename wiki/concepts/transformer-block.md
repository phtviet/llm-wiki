---
type: concept
sources: [ch02-model-architecture]
---
# Transformer Block

A transformer architecture is composed of multiple transformer blocks; the number of blocks is often called the model's number of layers. Each block generally contains two modules: an attention module and an MLP (multi-layer perceptron) module. The attention module consists of four weight matrices: query, key, value, and output projection. The MLP module consists of linear (feedforward) layers separated by nonlinear activation functions, which let the model learn nonlinear patterns; common choices are ReLU and GELU, used respectively by GPT-2 and GPT-3. Simpler, faster activation functions have proven preferable to more sophisticated ones, which cost more training compute and memory (AIE p.61-62).

A transformer model also has a module before all transformer blocks -- an embedding module with an embedding matrix and a positional embedding matrix, converting tokens and positions into vectors -- and a module after them: an output layer (also called the unembedding layer or model head) that maps output vectors into token probabilities used for sampling. Naively, the number of position indices sets the model's maximum [[context-length]], though techniques exist to extend context length without increasing position indices (AIE p.62-63).

A transformer model's size is determined by: the model's dimension (sizing the key/query/value/output-projection matrices), the number of transformer blocks, the feedforward layer dimension, and the vocabulary size (AIE p.63).

## Key figures
None. Per-model dimension figures live on the relevant model entity page (e.g. [[llama-2]]).

## Related
- [[transformer-architecture]]  (part-of: transformer blocks are the repeated building unit of the architecture)
- [[attention-mechanism]]  (part-of: the attention module is one of the block's two components)
- [[context-length]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-model-architecture]]
