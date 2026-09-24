---
type: concept
sources: [ch02-model-architecture]
---
# Attention Mechanism

The attention mechanism allows a model to weigh the importance of different input tokens when generating each output token -- like generating answers by referencing any page of a book rather than just its summary. It was introduced three years before the transformer paper (Bahdanau et al.) and was first used to augment seq2seq (Google's GNMT model, 2016), but it wasn't until the transformer paper showed attention could work without RNNs that it took off (AIE p.59-60).

The mechanism uses query (Q), key (K), and value (V) vectors. The query vector represents the decoder's current state -- the person looking for information. Each key vector represents a previous token, like a page number; each value vector represents that token's learned content, like the page's content. Attention is computed as a dot product between the query vector and each key vector: a high score means more of that token's value vector is used when generating output (AIE p.60-61).

Given input x and key/value/query weight matrices W_K, W_V, W_Q, the vectors are computed as K = xW_K, V = xW_V, Q = xW_Q, and attention is Attention(Q,K,V) = softmax(QK^T / sqrt(d))V. These matrices have dimensions matching the model's hidden dimension -- for Llama 2-7B, 4096x4096, producing K, V, Q vectors of dimension 4096 (AIE p.61).

Attention is almost always multi-headed: multiple heads let the model attend to different groups of previous tokens simultaneously, splitting Q, K, V into smaller per-head vectors. Llama 2-7B has 32 attention heads, so each vector splits into 32 vectors of dimension 128 (4096 / 32 = 128). Head outputs are concatenated and passed through an output projection matrix sized to the model's hidden dimension (AIE p.61-62). Because every previous token needs a stored key and value vector, longer sequences require more key/value storage and compute, which is a core reason context length is hard to extend for transformer models (AIE p.60).

## Key figures
- Llama 2-7B: query/key/value matrices are 4096x4096; 32 attention heads, each of dimension 128 (AIE p.61)

## Related
- [[transformer-architecture]]  (part-of: attention is the core mechanism inside the transformer's attention module)
- [[seq2seq]]  (boundary: attention predates the transformer and was first applied to augment seq2seq's RNNs)
- [[transformer-block]]  (part-of: the attention module is one of two modules in a transformer block)

## Provenance
- [[sources/ch02-model-architecture]]
