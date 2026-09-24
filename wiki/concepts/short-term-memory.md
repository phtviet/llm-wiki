---
type: concept
sources: [ch06-memory]
---
# Short-Term Memory

Short-term memory is a model's context: previous messages in a conversation can be added to the model's context so it can leverage them to generate future responses. It doesn't persist across tasks (queries), so it is fast to access but limited in capacity, and is best used to store information most important to the current task (AIE p.301).

A model's short-term capacity is determined by how much of the context window is reserved for information retrieved from [[long-term-memory]]. For example, if 30% of the context is reserved for retrieved long-term memory, the model can use at most 70% of the context limit for short-term memory; once that threshold is reached, overflow can be moved to long-term memory (AIE p.302).

Because short-term memory is limited by the model's maximum [[context-length]], it requires a strategy for what to add and delete. The simplest such strategy is FIFO (first in, first out): the earliest-added information is the first moved to external storage. API providers such as OpenAI may remove the beginning of a conversation as it grows, and frameworks such as LangChain may retain only the N last messages or N last tokens. This assumes early messages are less relevant, an assumption that can be fatally wrong when early messages state the conversation's purpose (AIE p.302-303).

## Key figures
- Example allocation: if 30% of context is reserved for long-term memory retrieval, short-term memory can use at most 70% of the context limit (AIE p.302)

## Related
- [[memory]]  (part-of: one of the model's three memory mechanisms)
- [[long-term-memory]]  (contrast: fast, limited, task-specific vs. persistent, cheaply extensible external storage; boundary: short-term overflow can be moved into long-term memory)
- [[memory-management]]  (prerequisite: memory management strategies like FIFO decide what stays in or is dropped from short-term memory)
- [[context-length]]  (boundary: short-term memory capacity is capped by the model's maximum context length)

## Provenance
- [[sources/ch06-memory]]
