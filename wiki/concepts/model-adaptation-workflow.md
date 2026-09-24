---
type: concept
sources: [ch07-finetuning-and-rag]
---
# Model Adaptation Workflow

The book's suggested staged process for adapting a model to a task, moving from cheapest/simplest techniques to more complex ones as failure modes demand. Before any adaptation step, the book stresses defining evaluation criteria and an evaluation pipeline, since evaluation should run through every subsequent step, not just at the start (AIE p.318).

The stages: (1) attempt the task with prompting alone, using prompt-engineering best practices and versioning prompts; (2) add more examples to the prompt, typically between 1 and 50 depending on use case; (3) if failures are information-based, connect the model to external data via RAG, starting with basic term-based retrieval; (4) branch depending on remaining failure mode -- persistent information-based failures call for more advanced RAG such as embedding-based retrieval, while persistent behavioral issues (irrelevant, malformatted, or unsafe output) call for finetuning; (5) combine RAG and finetuning together for a further performance boost (AIE p.318-319).

The book notes embedding-based retrieval increases inference-time complexity by adding pipeline components, while finetuning increases model-development complexity but leaves inference unchanged (AIE p.318). There is no single universal workflow; the actual path an application takes depends on its own failure modes (AIE p.318).

## Key figures

- Prompt examples added at stage 2 typically range from 1 to 50, depending on use case (AIE p.318)

## Related

- [[finetuning-versus-rag]]  (part-of: this workflow operationalizes the finetuning-vs-RAG decision into ordered steps)
- [[prompt-engineering]]  (prerequisite: workflow starts with prompting before considering retrieval or finetuning)
- [[rag]]  (example-of: term-based then embedding-based retrieval are the workflow's RAG stages)
- [[finetuning]]  (example-of: finetuning is the workflow's step for unresolved behavioral issues)
- [[embedding-based-retrieval]]  (example-of: advanced RAG option tried when basic term-based retrieval doesn't resolve information-based failures)
- [[bm25]]  (example-of: term-based method recommended as the workflow's initial RAG step)

## Provenance

- [[sources/ch07-finetuning-and-rag]]
