---
type: concept
sources: [ch04-step-1-evaluate-all-components-in-a-system]
---
# Turn-Based vs. Task-Based Evaluation

Generative AI applications, especially chatbot-like ones, allow back-and-forth between user and application across a conversation to accomplish a task. A turn can consist of multiple steps and messages, but it is still considered a single turn even if a system takes multiple steps to generate an output (AIE p.200-201).

Turn-based evaluation evaluates the quality of each individual output. Task-based evaluation evaluates whether a system completes a task overall -- for example, whether an AI model helped a user fix a bug in their Python code, and how many turns it took. Since what users ultimately care about is whether a model helps them accomplish their task, task-based evaluation is considered more important. It makes a large practical difference whether a system solves a problem in two turns versus twenty (AIE p.201).

A key challenge of task-based evaluation is determining task boundaries: in a multi-question conversation, it can be ambiguous whether a new query is a follow-up to an existing task or the start of a new one (AIE p.201).

## Key figures
None.

## Examples
- [[twenty-questions-benchmark]]  (task-based evaluation scored by whether and how quickly a concept is guessed)

## Related
- [[component-level-evaluation]]  (see-also: both slice evaluation of multi-step or multi-turn AI applications)
- [[twenty-questions-benchmark]]  (example-of: a concrete task-based evaluation benchmark)
- [[evaluation]]  (part-of: turn-based and task-based evaluation are approaches within the broader practice of evaluating AI systems)

## Provenance
- [[sources/ch04-step-1-evaluate-all-components-in-a-system]]
