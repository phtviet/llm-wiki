---
type: entity
sources: [ch10-step-3-add-model-router-and-gateway]
---
# Model Gateway

A model gateway is an intermediate layer that lets an organization interface with different models -- self-hosted or behind commercial APIs -- in a unified and secure manner. In its simplest form it is a unified wrapper: applications send a model type, model name, and input to the gateway, and the gateway dispatches the call to the right underlying API (e.g. OpenAI or Gemini), returning a standardized response (AIE p.458).

A model gateway simplifies maintenance: if an underlying model API changes, only the gateway needs updating rather than every application that depends on it. It also enables access control and cost management: instead of distributing organizational API tokens (which can be leaked) to everyone, an organization grants access only to the gateway, which can enforce fine-grained, per-user or per-application access controls and monitor and limit API usage to prevent abuse and manage cost (AIE p.458-459).

A gateway can implement fallback policies to work around rate limits or API failures: when a primary API is unavailable, the gateway can route requests to alternative models, retry after a short wait, or otherwise fail gracefully, keeping the application running smoothly. Because requests and responses already flow through it, the gateway is also a natural place to add load balancing, logging, analytics, caching, and guardrails (AIE p.459).

Off-the-shelf gateways exist since gateways are relatively straightforward to build, including Portkey's AI Gateway, MLflow AI Gateway, Wealthsimple's LLM Gateway, TrueFoundry, Kong, and Cloudflare. In the book's evolving AI architecture, the gateway replaces the plain model API box once introduced (AIE p.459-460).

## Key figures
None.

## Related
- [[router]]  (part-of: both sit inside the model API layer of the architecture; boundary: gateway provides unified access to models, router decides which model or solution a query goes to)
- [[model-api]]  (part-of: the gateway sits in front of and unifies multiple model APIs)
- [[inference-service]]  (see-also: the gateway is a layer for accessing inference services in a unified way)
- [[guardrails]]  (part-of: some gateways implement guardrails alongside caching, logging, and analytics)
- [[ai-pipeline-orchestration]]  (contrast: gateway unifies access to models specifically, orchestrator chains an AI system's components generally)

## Provenance
- [[sources/ch10-step-3-add-model-router-and-gateway]]
