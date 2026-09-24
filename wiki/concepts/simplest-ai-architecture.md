---
type: concept
sources: [ch10-ai-engineering-architecture]
---
# Simplest AI Architecture

The simplest architecture for a foundation model application is a direct pipeline: the application receives a query, sends it to the model, and the model generates a response returned to the user. There is no context augmentation, no guardrails, and no optimization at this stage (AIE p.449). The 'Model API' in this architecture refers to both third-party APIs (e.g., OpenAI, Google, Anthropic) and self-hosted models served via an inference server (AIE p.449).

This architecture is the starting point of a progressive build-out. From it, a team typically adds, in roughly this order: enhancing context input via external data sources and tools, adding guardrails, adding a model router and gateway for complex pipelines and security, optimizing latency and cost with caching, and adding complex logic and write actions. Monitoring/observability and orchestration are treated as cross-cutting concerns layered in afterward. The book notes this is the progression commonly seen in production, but that teams should order these additions to fit their own application's needs (AIE p.450).

## Key figures
None.

## Related
- [[rag-architecture]]  (prerequisite: context-augmentation step added to this simplest architecture builds toward retrieval-augmented designs)
- [[model-api]]  (part-of: the model API is the single component this architecture routes queries to)
- [[inference-server]]  (part-of: self-hosted models behind the Model API box run on an inference server)

## Provenance
- [[sources/ch10-ai-engineering-architecture]]
