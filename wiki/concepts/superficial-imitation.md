---
type: concept
sources: [ch08-ai-powered-data-synthesis]
---
# Superficial Imitation

Superficial imitation is the risk that a student model trained to mimic a teacher's outputs learns only the teacher's style, not its underlying capability. 'The False Promise of Imitating Proprietary LLMs' (Gudibande et al., 2023) shows imitation models are good at mimicking teacher style but struggle with factual accuracy and generalization outside the training data (AIE p.393).

Worse, imitation can force a student to hallucinate: if a teacher can solve complex math problems and its responses look like solutions, training a student on those responses teaches it to produce answers that look like solutions even when the student cannot actually solve the underlying problems. Gudibande et al. (2023) argue that improving reasoning capability instead requires improving the base model's quality (AIE p.393).

## Key figures
None.

## Related
- [[data-synthesis]] (boundary: a limitation of training students on AI-generated outputs)
- [[model-distillation]] (boundary: distillation risks superficial imitation if the student only mimics teacher style)

## Provenance
- [[sources/ch08-ai-powered-data-synthesis]]
