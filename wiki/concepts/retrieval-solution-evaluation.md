---
type: concept
sources: [ch06-retrieval-optimization]
---
# Retrieval Solution Evaluation

Evaluating a retrieval solution (as distinct from evaluating retrieval quality metrics like precision and recall) means weighing a set of practical, operational factors when choosing or building a retrieval system (AIE p.272). Key factors include which retrieval mechanisms it supports and whether it supports hybrid search; if it is a vector database, which embedding models and vector search algorithms it supports; its scalability in data storage and query traffic for a given traffic pattern; how long it takes to index data and how much data it can bulk add/delete at once; its query latency across different retrieval algorithms; and, for a managed solution, its pricing structure (based on document/vector volume versus query volume). This list excludes enterprise functionality such as access control, compliance, and data-plane/control-plane separation (AIE p.272).

## Key figures
None.

## Examples
None.

## Related
- [[hybrid-search]]  (see-also: whether a retrieval solution supports hybrid search is one evaluation factor)
- [[vector-database]]  (part-of: vector databases are one kind of retrieval solution evaluated by these factors)
- [[retrieval-quality-metrics]]  (boundary: this evaluates the retrieval system/solution operationally, distinct from precision/recall quality metrics)

## Provenance
- [[sources/ch06-retrieval-optimization]]
