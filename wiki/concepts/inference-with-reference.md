---
type: concept
sources: [ch09-model-optimization]
---
# Inference with Reference

Inference with reference speeds up generation in cases where a response needs to repeat text from the input, such as answering a question about an attached document or fixing bugs in code. Instead of generating these repeated tokens, the technique copies candidate draft tokens directly from the input context (AIE p.430). It is similar to speculative decoding, but instead of using a model to generate draft tokens, it selects them from the input; the key challenge is identifying the most relevant text span from the context at each decoding step, with the simplest approach being to match a span against the current tokens (AIE p.430).

Unlike speculative decoding, this technique needs no extra model, but is useful only where there is significant overlap between context and output, such as retrieval systems, coding, or multi-turn conversations (AIE p.430).

## Key figures
- Achieves roughly a two-times generation speedup in overlap-heavy use cases (Yang et al., 2023) (AIE p.430)

## Examples
None.

## Related
- [[speculative-decoding]]  (contrast: copies draft tokens from the input rather than generating them with a separate model)
- [[autoregressive-decoding-bottleneck]]  (prerequisite: one solution to this bottleneck)

## Provenance
- [[sources/ch09-model-optimization]]
