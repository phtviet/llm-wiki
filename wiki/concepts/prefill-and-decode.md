---
type: concept
sources: [ch09-inference-overview]
---
# Prefill and Decode

Inference for a transformer-based [[language-model]] consists of two steps (AIE p.409):

- **Prefill**: the model processes input tokens in parallel, effectively populating the initial [[kv-cache]]. How many tokens can be processed at once is limited by the number of operations the hardware can execute in a given time, making prefilling compute-bound (AIE p.409).
- **Decode**: the model generates one output token at a time, which at a high level involves loading large matrices (e.g., model weights) into GPUs -- a step limited by how quickly hardware can load data into memory, making decoding memory bandwidth-bound (AIE p.409).

Because prefill and decode have different computational profiles, they are often decoupled in production onto separate machines (AIE p.409).

## Key figures
None.

## Related
- [[computational-bottlenecks]]  (example-of: prefill and decode instantiate the compute-bound/memory bandwidth-bound distinction within transformer inference)
- [[transformer-architecture]]  (prerequisite: prefill and decode describe how transformer-based language models perform inference)
- [[inference-server]]  (see-also: an inference server's design accounts for the differing prefill/decode profiles)
- [[language-model]]  (see-also: mentioned in this page's text)
- [[kv-cache]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch09-inference-overview]]
