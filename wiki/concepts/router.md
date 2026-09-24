---
type: concept
sources: [ch10-step-3-add-model-router-and-gateway]
---
# Router

A router directs different queries to different solutions instead of using one model for all queries. This lets an application use specialized models that outperform a general-purpose model on specific query types, and lets it save cost by sending simpler queries to cheaper models (AIE p.456).

A router typically consists of an intent classifier that predicts what the user is trying to do, then routes the query to the appropriate solution: an FAQ page, a human operator, a specialized chatbot, and so on. An intent classifier can also keep a system out of out-of-scope conversations (responding with a stock decline instead of wasting an API call), and can detect ambiguous queries and ask for clarification (AIE p.456-457).

Routers generalize beyond intent classification for chat: for an agent capable of multiple actions, a router can act as a next-action predictor deciding which tool or action to use next; for a model with a memory system, a router can predict which part of the memory hierarchy to pull information from (AIE p.457).

Many teams adapt smaller foundation models (GPT-2, BERT, Llama 7B) as intent classifiers, while others train even smaller classifiers from scratch. Because routers should be fast and cheap enough to use multiples of them without adding significant latency or cost, they are typically smaller than the models used for generation (AIE p.457).

Routing also has to handle context-limit mismatches: if a query is routed to a model with a smaller context limit than the context an action later retrieves (e.g., a 1,000-token query routed to a 4K-context model, followed by an action that returns 8,000 tokens of context), the system must either truncate the context or route to a model with a larger context limit (AIE p.457).

Routing typically happens before retrieval (e.g., deciding if a query is in-scope and needs retrieval at all), though it can also happen after retrieval, such as deciding whether to hand a query to a human operator. The common AI application pattern is routing, then retrieval, then generation, then scoring (AIE p.457).

## Key figures
- Example context-limit mismatch: a 1,000-token query intended for a 4K-context model, followed by a retrieved context of 8,000 tokens (AIE p.457)

## Examples
- [[customer-support-chatbot]]  (routes password-reset, billing, and troubleshooting queries to different solutions)

## Related
- [[model-gateway]]  (part-of: both sit inside the model API layer of the AI architecture; boundary: router selects which model/solution to use, gateway provides unified access to whichever model is chosen)
- [[agent]]  (example-of: a next-action predictor is a router used to choose an agent's next tool or action)
- [[memory]]  (see-also: a router can predict which part of a memory hierarchy to pull information from)
- [[bert]]  (example-of: smaller foundation model teams adapt as an intent classifier)
- [[rag-architecture]]  (prerequisite: routing commonly decides whether a query needs retrieval before the retrieve-generate-score pipeline runs)

## Provenance
- [[sources/ch10-step-3-add-model-router-and-gateway]]
