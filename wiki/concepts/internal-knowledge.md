---
type: concept
sources: [ch06-memory]
---
# Internal Knowledge

Internal knowledge is a model's own retained knowledge from the data it was trained on. It is one of the three memory mechanisms described for AI models, alongside [[short-term-memory]] and [[long-term-memory]]. A model's internal knowledge doesn't change unless the model itself is updated, and it can be accessed in all queries (AIE p.301).

Information that is essential for all tasks should be incorporated into a model's internal knowledge via training or finetuning, as opposed to being kept in short- or long-term memory (AIE p.301).

## Key figures
None.

## Related
- [[memory]]  (part-of: one of the model's three memory mechanisms)
- [[short-term-memory]]  (contrast: persists indefinitely without retraining vs. limited to the current context/task)
- [[long-term-memory]]  (contrast: requires updating the model to change vs. can be deleted or updated without retraining)
- [[finetuning]]  (prerequisite: incorporating information into internal knowledge requires training or finetuning the model)

## Provenance
- [[sources/ch06-memory]]
