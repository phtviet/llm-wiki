---
type: concept
sources: [ch07-when-to-finetune]
---
# When to Finetune

Before adopting [[finetuning]], it is worth asking whether it is the right option at all. Compared to prompt-based methods, finetuning requires significantly more resources -- not just data and hardware, but also ML talent. Because of this cost, finetuning is generally attempted only after extensive experiments with prompt-based methods have been tried first (AIE p.311).

Finetuning and prompting are not mutually exclusive: real-world problems often require both approaches, used together rather than as a strict either/or choice (AIE p.311).

## Key figures
None.

## Related
- [[finetuning]]  (prerequisite: deciding when to finetune presupposes understanding what finetuning is and what it costs)
- [[prompt-engineering]]  (contrast: cheaper, weight-preserving alternative generally tried first, before resorting to finetuning)
- [[model-adaptation-workflow]]  (part-of: this decision point is a step in the book's staged prompting-to-RAG-to-finetuning process)

## Provenance
- [[sources/ch07-when-to-finetune]]
