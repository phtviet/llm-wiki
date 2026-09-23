---
type: concept
sources: [ch02-sampling-strategies]
---
# Stopping Condition

A stopping condition determines when an autoregressive language model halts token-by-token generation, which matters because longer output sequences take more time, cost more compute, and can annoy users (AIE p.95). One method fixes a maximum number of tokens, which risks cutting output off mid-sentence; another uses stop tokens or stop words, such as stopping when the model generates an end-of-sequence token (AIE p.95). Stopping conditions help keep latency and cost down, but early stopping can cause malformatted output — for example, generated JSON missing closing brackets, making it hard to parse (AIE p.95).

## Key figures
None.

## Related
- [[sampling]]  (part-of: stopping conditions govern when autoregressive sampling ends)
- [[autoregressive-language-model]]  (prerequisite: stopping conditions apply to the token-by-token generation process autoregressive models use)

## Provenance
- [[sources/ch02-sampling-strategies]]
