---
type: concept
sources: [ch08-model-distillation, ch09-inference-overview]
---
# Inference Service

The inference service is the broader system responsible for receiving, routing, and possibly preprocessing requests before they reach the [[inference-server]], which hosts models and executes them (AIE p.406). Model APIs such as those from OpenAI and Google are themselves inference services; using one means the caller is not responsible for implementing inference-optimization techniques, whereas self-hosting a model makes the host responsible for building, optimizing, and maintaining its inference service (AIE p.406).

Providers commonly expose two API modes over an inference service: online APIs, which optimize for latency by processing requests as they arrive, and batch APIs, which optimize for cost by allowing higher-latency, more efficient processing such as request batching and cheaper hardware (AIE p.410). Customer-facing use cases like chatbots and code generation typically need online APIs, while use cases without strict latency needs -- synthetic data generation, periodic reporting, document onboarding, model migration reprocessing, personalized recommendations, and knowledge base reindexing -- suit batch APIs (AIE p.410-411). This differs from traditional ML batch inference, which precomputes predictions before requests arrive; [[foundation-model]] inputs are open-ended, making such precomputation impractical (AIE p.411-412).

Online APIs may still batch requests together as long as latency isn't significantly harmed. Many online APIs offer streaming mode, returning each token as it's generated to reduce the wait until the first token, at the cost of being unable to score a response before showing it to users (AIE p.411).

## Key figures
- Batch APIs from [[google-gemini]] and OpenAI offer a 50% cost reduction with turnaround in hours rather than seconds or minutes (AIE p.410)

## Examples
- [[inference-server]]  (the component within the service that executes models)

## Related
- [[inference-server]]  (part-of: the inference service routes and preprocesses requests before they reach the inference server)
- [[computational-bottlenecks]]  (see-also: bottleneck analysis shapes how an inference service is optimized)
- [[inference-optimization]]  (part-of: inference services are the target of inference-optimization techniques)
- [[foundation-model]]  (see-also: mentioned in this page's text)
- [[google-gemini]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch09-inference-overview]]
