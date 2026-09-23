---
type: concept
sources: [ch02-model-architecture]
---
# Attention Mechanism

The attention mechanism allows a model to weigh the importance of different input tokens when generating each output token, rather than relying on only a single compressed summary of the input (AIE p.59-60). It was introduced three years before the transformer paper (Bahdanau et al.) and was first used with RNN-based [[seq2seq-architecture]] in Google's 2016 GNMT model; it wasn't until the transformer paper showed attention could work without RNNs that it took off (AIE p.60).

Under the hood, attention uses three vectors per token: the **query (Q)** vector, representing the decoder's current state and what information it seeks; the **key (K)** vector, representing a previous token (like a page number); and the **value (V)** vector, representing that token's learned content (like the page's content) (AIE p.60-61). Attention is computed as a dot product between a query vector and each key vector, producing a score for how much of that token's value vector to use when generating the next token; formally, Attention(Q, K, V) = softmax(QK^T / sqrt(d))V (AIE p.61). Given input x and key/value/query weight matrices W_K, W_V, W_Q, the vectors are computed as K = xW_K, V = xW_V, Q = xW_Q (AIE p.61).

The longer the sequence, the more key and value vectors must be computed and stored, which is one reason extending context length is difficult for transformer models (AIE p.61). Attention is almost always multi-headed: query, key, and value vectors are split into smaller vectors, one per attention head, allowing the model to attend to different groups of previous tokens simultaneously; head outputs are concatenated and passed through an output projection matrix sized to the model's hidden dimension (AIE p.61-62).

## Key figures
None. The general mechanism carries no intrinsic load-bearing figure of its own; the worked dimension numbers (4,096, 32 heads, 128 per head) are Llama 2-7B-specific and live on [[transformer-architecture]] and [[llama-2]].

## Examples
- [[transformer-architecture]]  (mechanism at the core of every transformer block)

## Related
- [[transformer-architecture]]  (part-of: attention is the core mechanism inside each transformer block)
- [[seq2seq-architecture]]  (contrast: attention lets the decoder reference any prior token instead of only the encoder's final hidden state)

## Provenance
- [[sources/ch02-model-architecture]]
