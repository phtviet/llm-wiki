---
type: concept
sources: [ch06-memory]
---
# Memory

Memory refers to mechanisms that allow a model to retain and utilize information. It is especially useful for knowledge-rich applications like RAG and multi-step applications like agents: a RAG system relies on memory for its augmented context, which can grow over multiple turns, while an agentic system needs memory to store instructions, examples, context, tool inventories, plans, tool outputs, and reflections (AIE p.300).

An AI model typically has three memory mechanisms: [[internal-knowledge]], [[short-term-memory]], and [[long-term-memory]]. Which mechanism to use depends on frequency of use: information essential for all tasks belongs in internal knowledge (via training or finetuning), rarely-needed information belongs in long-term memory, and immediate task-specific information belongs in short-term memory (AIE p.301).

Augmenting a model with a memory system has several benefits: managing information overflow within a session (storing an agent's excess context in long-term memory), persisting information between sessions (personalizing an AI coach or assistant across conversations), boosting a model's consistency (referencing previous answers to calibrate future ones), and maintaining data structural integrity (storing structured data like a leads spreadsheet or an action queue outside unstructured text context) (AIE p.301-302).

A memory system typically consists of two functions: memory management (deciding what to store in short-term vs. long-term memory) and memory retrieval (retrieving information relevant to the task from long-term memory, similar to RAG retrieval) (AIE p.302). See [[memory-management]] for how the add/delete operations work.

## Key figures
None.

## Examples
- [[memory-management]]

## Related
- [[internal-knowledge]]  (part-of: one of the three memory mechanisms; retained model knowledge that only changes via retraining)
- [[short-term-memory]]  (part-of: one of the three memory mechanisms; the model's context window)
- [[long-term-memory]]  (part-of: one of the three memory mechanisms; external retrievable data)
- [[memory-management]]  (part-of: memory systems consist of memory management and memory retrieval)

## Provenance
- [[sources/ch06-memory]]
