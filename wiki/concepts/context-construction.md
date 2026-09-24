---
type: concept
sources: [ch06-rag-and-agents, ch10-step-1-enhance-context]
---
# Context Construction

Context construction is the process of gathering the task-relevant information a model needs to answer a query, via retrieval (text, image, or tabular data) or tool use such as web search. It is analogous to feature engineering for foundation models: it gives the model the information necessary to produce a good output (AIE p.450).

Because of its central role in output quality, context construction is almost universally supported by model API providers: OpenAI, Claude, and Gemini all let users upload files and let their models call tools. Providers differ, however, in how much context construction they support -- limits on document types and counts, retrieval algorithm and chunk-size configuration, and which tool types and execution modes (e.g. parallel function execution, long-running jobs) they allow. A specialized RAG solution may accept as many documents as its vector database can hold, while a generic model API may cap uploads much lower (AIE p.450-451).

In an evolving AI platform architecture, adding context construction is typically the first step taken beyond the simplest query-to-model pipeline (AIE p.450).

## Key figures
None.

## Related
- [[rag-architecture]]  (part-of: text retrieval is one context-construction mechanism)
- [[multimodal-rag]]  (part-of: image retrieval as a context-construction mechanism)
- [[rag-with-tabular-data]]  (part-of: tabular data retrieval as a context-construction mechanism)
- [[tool-inventory]]  (part-of: tool use, e.g. web search/news/weather APIs, augments context alongside retrieval)
- [[chunking-strategy]]  (see-also: chunk-size configuration is one axis on which context-construction solutions differ)
- [[ai-pipeline-orchestration]]  (prerequisite: context construction is added to the simplest pipeline as an early architectural extension)

## Provenance
- [[sources/ch06-rag-and-agents]]
- [[sources/ch10-step-1-enhance-context]]
