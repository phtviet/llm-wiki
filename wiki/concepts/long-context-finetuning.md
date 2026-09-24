---
type: concept
sources: [ch07-finetuning-overview]
---
# Long-Context Finetuning

Long-context finetuning extends a model's [[context-length]]. It typically requires modifying the model's architecture, such as adjusting positional embeddings, since a longer sequence means more possible token positions that positional embeddings must handle (AIE p.310). Compared to other finetuning techniques, long-context finetuning is harder to do, and the resulting model might degrade on shorter sequences (AIE p.310). [[code-llama]] used long-context finetuning to increase its maximum context length from 4,096 to 16,384 tokens to accommodate longer code files (AIE p.310).

## Key figures
None. The concept's load-bearing figure (4,096 to 16,384 tokens) is entity-specific and lives on the [[code-llama]] page.

## Related
- [[finetuning]]  (part-of: one specialized finetuning technique among several)
- [[context-length]]  (part-of: long-context finetuning is the technique used to extend context length)
- [[code-llama]]  (example-of: Code Llama used long-context finetuning to reach a 16,384-token context)

## Provenance
- [[sources/ch07-finetuning-overview]]
