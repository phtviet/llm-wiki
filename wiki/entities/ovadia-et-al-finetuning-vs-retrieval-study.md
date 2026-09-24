---
type: entity
sources: [ch07-finetuning-and-rag]
---
# Ovadia et al. (2024), 'Fine-Tuning or Retrieval?'

A 2024 paper by Ovadia et al. comparing RAG and finetuning on tasks requiring up-to-date information, such as questions about current events. It is the book's primary empirical support for preferring RAG over finetuning for knowledge-based tasks (AIE p.316).

The study curated a question-answering task about current events and tested three base models -- Mistral-7B, [[llama-2]]-7B, and Orca 2-7B -- under six conditions: base model, base model + RAG, two finetuning approaches (FT-reg and FT-par), and each finetuning approach combined with RAG (AIE p.316). It also evaluated the same models on the [[mmlu]] benchmark (AIE p.317).

## Key figures

- Base model + RAG scores: Mistral-7B 0.875, Llama 2-7B 0.585, Orca 2-7B 0.876, all higher than either finetuning approach alone on the current-events QA task (AIE p.316)
- FT-reg and FT-par (finetuning-only) scores were lower than base model + RAG for all three models, e.g. Mistral-7B FT-reg 0.504 and FT-par 0.588 vs. base+RAG 0.875 (AIE p.316)
- Combining RAG with a finetuned model improved MMLU performance 43% of the time; it did not improve over RAG alone 57% of the time (AIE p.318)

## Related

- [[finetuning-versus-rag]]  (part-of: this study is the empirical evidence for the synthesis's central claim)
- [[mmlu]]  (example-of: benchmark used to test RAG-plus-finetuning combinations)
- [[rag]]  (see-also: study demonstrates RAG outperforming finetuning on knowledge tasks)
- [[llama-2]]  (see-also: mentioned in this page's text)

## Provenance

- [[sources/ch07-finetuning-and-rag]]
