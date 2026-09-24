---
type: concept
sources: [ch06-memory]
---
# Memory Management

Memory management is one of the two functions of a memory system (the other being memory retrieval). It typically consists of two operations: add and delete memory, governing what information is stored in short-term versus long-term memory (AIE p.302).

The simplest deletion strategy is FIFO (first in, first out): the earliest information added to short-term memory is the first moved to external storage. This is straightforward but assumes early messages are less relevant, which can be wrong when early messages state the conversation's purpose (AIE p.302-303).

More sophisticated strategies remove redundancy, for example by summarizing the conversation (using the same or another model) and tracking named entities. Bae et al. (2022) built a classifier that, for each sentence in the memory and each sentence in the summary, determines whether only one, both, or neither should be added to a new merged memory. Liu et al. (2023) used a reflection approach: after each action, the agent reflects on the newly generated information and determines whether it should be inserted into memory, merged with existing memory, or replace outdated or contradicting information (AIE p.303-304).

When information contradicts, some practitioners keep the newer information, while others ask an AI model to judge which to keep; the right approach depends on the use case, since contradictions can confuse an agent but can also let it draw on different perspectives (AIE p.304).

## Key figures
None.

## Examples
- [[memory]]

## Related
- [[memory]]  (part-of: memory management is one of the two functions of a memory system, alongside memory retrieval)
- [[short-term-memory]]  (prerequisite: memory management strategies determine what is added to or dropped from short-term memory)
- [[long-term-memory]]  (prerequisite: memory management determines what overflow moves into long-term memory)

## Provenance
- [[sources/ch06-memory]]
