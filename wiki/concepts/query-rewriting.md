---
type: concept
sources: [ch06-retrieval-optimization]
---
# Query Rewriting

Query rewriting (also called query reformulation, query normalization, or sometimes query expansion) rewrites a user's query so it makes sense on its own before it is used for retrieval (AIE p.270). For example, in a conversation where a user asks "When was the last time John Doe bought something from us?" and follows up with "How about Emily Doe?", the follow-up is ambiguous out of context and would return irrelevant results if used verbatim; it must be rewritten to "When was the last time Emily Doe bought something from us?"

Query rewriting is not unique to RAG: traditional search engines often rewrite queries using heuristics, while AI applications can use a generative model prompted with instructions such as "Given the following conversation, rewrite the last user input to reflect what the user is actually asking." Rewriting can require identity resolution or external knowledge — e.g. a query like "How about his wife?" requires first looking up who the wife is. If that information isn't available, the rewriting model should acknowledge the query is unsolvable rather than hallucinate an answer, which would lead to a wrong result (AIE p.270).

## Key figures
None.

## Examples
None.

## Related
- [[hallucination]]  (boundary: a rewriting model should admit it lacks needed information rather than hallucinate a resolution)
- [[rag]]  (part-of: query rewriting is one of the retrieval-optimization tactics used within RAG systems, though not unique to RAG)
- [[context-construction]]  (part-of: rewriting the query is a step in constructing task-relevant context for retrieval)

## Provenance
- [[sources/ch06-retrieval-optimization]]
