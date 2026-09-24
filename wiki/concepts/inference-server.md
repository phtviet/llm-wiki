---
type: concept
sources: [ch09-inference-overview]
---
# Inference Server

The inference server is the production component that runs model inference. It hosts the available models and has access to the necessary hardware; based on requests from applications (e.g., user prompts), it allocates resources to execute the appropriate models and returns responses (AIE p.406). It is one part of a broader [[inference-service]], which also handles receiving, routing, and preprocessing requests before they reach the server (AIE p.406).

## Key figures
None.

## Related
- [[inference-service]]  (part-of: the server is the execution component within the broader inference service)
- [[computational-bottlenecks]]  (prerequisite: an inference server must be designed around its workload's compute-bound or memory bandwidth-bound bottlenecks)

## Provenance
- [[sources/ch09-inference-overview]]
