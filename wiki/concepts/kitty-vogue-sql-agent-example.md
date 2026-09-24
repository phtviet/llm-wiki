---
type: concept
sources: [ch06-agent-overview]
---
# Kitty Vogue SQL Agent Example

The book's running RAG-with-tabular-data example (Kitty Vogue) illustrates agentic behavior with three actions: response generation, SQL query generation, and SQL query execution (AIE p.277).

Given the query 'Project the sales revenue for Fruity Fedora over the next three months,' the agent performs a sequence of actions: it reasons about what it needs (e.g. sales numbers from the last five years), invokes SQL query generation and execution to get them, reasons that the data is insufficient and it also needs past marketing-campaign information, invokes SQL generation and execution again, then reasons that it now has enough information to generate a sales projection, and finally reasons that the task is complete (AIE p.277).

## Key figures
None.

## Related
- [[agent]]  (example-of: illustrates an agent's plan-act-reason loop across multiple tool invocations)

## Provenance
- [[sources/ch06-agent-overview]]
