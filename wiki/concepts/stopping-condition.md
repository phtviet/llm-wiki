---
type: concept
sources: [ch02-sampling-strategies]
---
# Stopping Condition

A stopping condition tells an [[autoregressive-language-model]] when to stop generating further tokens. Because a long output sequence takes more time, costs more compute, and can annoy users, applications often set a condition to end generation early (AIE p.95). One method is to stop after a fixed number of tokens, though this risks cutting the output off mid-sentence. Another is to use stop tokens or stop words, such as stopping when the model generates an end-of-sequence token (AIE p.95).

Stopping conditions help keep latency and cost down, but early stopping can cause outputs in a structured format (e.g., JSON) to be malformatted, such as missing closing brackets, making the generated output hard to parse (AIE p.95).

## Key figures
None.

## Related
- [[sampling]]  (part-of: governs when an autoregressive generation process produced by sampling ends)
- [[autoregressive-language-model]]  (prerequisite: stopping conditions apply to the token-by-token generation process this model type performs)

## Provenance
- [[sources/ch02-sampling-strategies]]
