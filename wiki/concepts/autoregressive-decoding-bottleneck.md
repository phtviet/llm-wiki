---
type: concept
sources: [ch09-model-optimization]
---
# Autoregressive Decoding Bottleneck

Autoregressive language models generate one token after another, making generation slow and expensive: a 100-token response at 100ms/token takes 10 seconds (AIE p.428). Each token-generation step requires transferring the entire model's parameters from accelerator high-bandwidth memory to compute units, making the operation bandwidth-heavy; since only one token is produced at a time, only a small number of FLOP/s are consumed, resulting in computational inefficiency (AIE p.427-428). Across model API providers, an output token costs roughly two to four times an input token, and Anyscale found a single output token can affect latency as much as 100 input tokens (Kadous et al., 2023) (AIE p.428).

Techniques addressing this bottleneck include speculative decoding, inference with reference, and parallel decoding.

## Key figures
- 100ms/token generation implies a 10s latency for a 100-token response (AIE p.428)
- An output token costs approximately two to four times an input token; one output token can impact latency as much as 100 input tokens (AIE p.428)

## Examples
- [[speculative-decoding]]
- [[inference-with-reference]]
- [[parallel-decoding]]

## Related
- [[speculative-decoding]]  (example-of: technique overcoming this bottleneck)
- [[inference-with-reference]]  (example-of: technique overcoming this bottleneck)
- [[parallel-decoding]]  (example-of: technique overcoming this bottleneck)
- [[inference-latency]]  (part-of: autoregressive decoding drives TTFT/TPOT latency components)

## Provenance
- [[sources/ch09-model-optimization]]
