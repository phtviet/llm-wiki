---
type: concept
sources: [ch06-memory]
---
# Long-Term Memory

Long-term memory consists of external data sources a model can access via retrieval, such as in a RAG system. Unlike a model's internal knowledge, information in long-term memory can be deleted without updating the model, and unlike short-term memory it can persist across tasks (AIE p.301).

Long-term memory can absorb the overflow from short-term memory when the context window fills up. Because external memory storage is relatively cheap and easily extensible, deletion from long-term memory may not be necessary, unlike short-term memory which is hard-capped by context length (AIE p.302).

Memory retrieval -- pulling relevant information from long-term memory for a task -- is similar to RAG retrieval, since long-term memory is itself an external data source (AIE p.302).

## Key figures
None.

## Related
- [[memory]]  (part-of: one of the model's three memory mechanisms)
- [[short-term-memory]]  (contrast: persistent and cheaply extensible vs. fast but capacity-limited; boundary: receives overflow moved from short-term memory)
- [[memory-management]]  (prerequisite: memory management decides what is added to or deleted from long-term memory)

## Provenance
- [[sources/ch06-memory]]
