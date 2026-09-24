---
type: concept
sources: [ch06-rag-beyond-texts]
---
# RAG with Tabular Data

Many applications need to answer queries using information stored in data tables, not
just unstructured text or images. The workflow for augmenting context with tabular data
differs significantly from the classic RAG workflow, since the relevant information must
be computed by querying a table rather than retrieved as a chunk of text (AIE p.273-274).

Assuming the table can be queried with SQL, the workflow has three steps: (1)
text-to-SQL — based on the user query and the provided table schemas, determine what SQL
query is needed; text-to-SQL is an example of semantic parsing; (2) SQL execution —
execute the generated SQL query; (3) generation — generate a response based on the SQL
result and the original user query (AIE p.274). If there are many available tables whose
schemas cannot all fit into the model's context, an intermediate step may be needed to
predict which tables are relevant to a given query. The text-to-SQL step can be performed
by the same generator that produces the final response, or by a specialized text-to-SQL
model (AIE p.274).

## Key figures
None.

## Examples
- [[kitty-vogue-sql-agent-example]]  (worked example: Kitty Vogue Sales table and Fruity Fedora query)

## Related
- [[rag-architecture]]  (part-of: applies the retriever/generator pattern to structured data, replacing text retrieval with query execution)
- [[multimodal-rag]]  (contrast: augments context with structured table data instead of unstructured multimodal data)
- [[kitty-vogue-sql-agent-example]]  (example-of: worked text-to-SQL, execution, and generation walkthrough)
- [[function-calling]]  (see-also: SQL execution is one kind of tool a model-driven system can invoke)

## Provenance
- [[sources/ch06-rag-beyond-texts]]
