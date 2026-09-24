---
type: concept
sources: [ch10-ai-pipeline-orchestration]
---
# AI Pipeline Orchestration

An AI application can consist of multiple models, retrieval from many databases, and access to a wide range of tools. An orchestrator specifies how these components work together to form an end-to-end pipeline, ensuring data flows seamlessly between them (AIE p.472).

At a high level, an orchestrator operates in two steps. **Components definition** tells the orchestrator what components the system uses -- models, external data sources for retrieval, tools, and any evaluation/monitoring tooling. A [[model-gateway]] can make it easier to add a model. **Chaining** is function composition: combining components together by specifying the steps the system takes from receiving a user query to completing the task. An example chain: process the raw query, retrieve relevant data, combine query and retrieved data into a prompt, generate a response, evaluate the response, and either return it or route to a human operator (AIE p.472-473).

The orchestrator is responsible for passing data between components, and should provide tooling that ensures a step's output matches the next step's expected format, ideally notifying the developer when the data flow is disrupted by component failures or data mismatches (AIE p.473).

An AI pipeline orchestrator is distinct from a general workflow orchestrator like Airflow or Metaflow (AIE p.473). For applications with strict latency requirements, independent steps -- such as a routing component and a PII removal component -- should run in parallel rather than sequentially (AIE p.473).

Many tools exist for AI orchestration, including LangChain, LlamaIndex, Flowise, Langflow, and Haystack; because retrieval and tool use are common patterns, many RAG and agent frameworks double as orchestration tools. Adopting an orchestration tool early is tempting but adds complexity: an orchestrator can abstract away critical details of how a system works, making it harder to understand and debug, so it can be worth building an application without one first (AIE p.473).

## Key figures
None.

## Examples
- LangChain, LlamaIndex, Flowise, Langflow, Haystack -- general-purpose AI orchestration tools

## Related
- [[rag-architecture]]  (prerequisite: orchestration chains together a RAG pipeline's retriever and generator steps)
- [[agent]]  (see-also: agent tool use is often built and chained via an orchestrator)
- [[model-gateway]]  (part-of: a model gateway simplifies the components-definition step of orchestration)
- [[context-construction]]  (part-of: retrieval and prompt-assembly steps chained by an orchestrator implement context construction)

## Provenance
- [[sources/ch10-ai-pipeline-orchestration]]
