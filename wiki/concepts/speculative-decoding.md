---
type: concept
sources: [ch09-model-optimization]
---
# Speculative Decoding

Speculative decoding (also called speculative sampling) uses a faster, less powerful 'draft' (or proposal) model to generate a sequence of K tokens, which the more powerful 'target' model then verifies in parallel. The target model accepts the longest left-to-right subsequence of draft tokens it agrees with, then generates one additional token itself; the loop repeats conditioned on the accepted tokens (AIE p.428). If no draft tokens are accepted, the loop yields only one token; if all K are accepted, it yields K+1 tokens (AIE p.428).

This works because verifying a sequence in parallel is faster than generating it sequentially, effectively turning decoding's computation profile into that of prefilling; some tokens are easier to predict than others, letting a weaker draft model get high acceptance rates; and decoding is memory bandwidth-bound, leaving idle FLOPs available for free verification (AIE p.429). Acceptance rates are domain-dependent, higher for structured text like code. Larger K reduces verification calls but lowers the draft acceptance rate. The draft model can be any architecture but ideally shares the target's vocabulary and tokenizer; it can be custom-trained or an existing weaker model (AIE p.429).

The technique has gained traction for being easy to implement (about 50 lines of PyTorch) without changing model quality, and has been incorporated into vLLM, TensorRT-LLM, and llama.cpp (AIE p.429).

## Key figures
- DeepMind's 4B-parameter draft model for Chinchilla-70B generates a token eight times faster (1.8 ms/token vs. 14.1 ms/token), reducing overall response latency by more than half without compromising quality (Chen et al., 2023) (AIE p.429)

## Examples
None.

## Related
- [[autoregressive-decoding-bottleneck]]  (prerequisite: speculative decoding is one solution to this bottleneck)
- [[inference-with-reference]]  (contrast: uses input tokens as drafts instead of a separate draft model)
- [[parallel-decoding]]  (contrast: breaks sequential dependency directly rather than verifying a separately-generated draft sequence)

## Provenance
- [[sources/ch09-model-optimization]]
