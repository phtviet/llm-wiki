---
type: concept
sources: [ch02-test-time-compute]
---
# Self-Consistency

Self-consistency is a test-time-compute selection method that picks the most common output among a set of sampled outputs as the final answer, rather than using logprob or a reward model (Wang et al., 2023) (AIE p.99). It is especially useful for tasks expecting an exact answer: given a math problem, a model can solve it multiple times and pick the most frequent answer, or for a multiple-choice question, pick the most frequent selected option (AIE p.99). Google used this approach when evaluating Gemini on the MMLU benchmark, sampling 32 outputs per question, which let the model score higher than it would with a single output (AIE p.99).

## Key figures
None. The Gemini MMLU figure (32 samples) is entity/example-specific and lives on [[gemini-mmlu-prompting-comparison]].

## Related
- [[test-time-compute]]  (part-of: one selection method for choosing among multiple sampled outputs)
- [[gemini-mmlu-prompting-comparison]]  (example-of: Google's Gemini MMLU evaluation applied self-consistency by sampling 32 outputs per question)
- [[reward-model]]  (contrast: picks the most frequent output rather than scoring outputs with a learned model)

## Provenance
- [[sources/ch02-test-time-compute]]
