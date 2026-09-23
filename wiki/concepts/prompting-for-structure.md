---
type: concept
sources: [ch02-structured-outputs]
---
# Prompting for Structured Outputs

Prompting is the first line of action for getting structured outputs: a model can be instructed to generate output in any format, but whether it complies depends on the model's instruction-following capability and the clarity of the instruction. Models are improving at this, but there is no guarantee of always following format instructions, and even a small percentage of invalid outputs can be unacceptable for some applications (AIE p.102).

To raise the rate of valid outputs, some use a second AI query to validate and/or correct the first output -- an instance of the AI-as-a-judge approach. This adds at least one extra model query per output, which improves validity but adds cost and latency that can make the approach too expensive for some use cases (AIE p.102).

## Key figures
None.

## Related
- [[structured-outputs]]  (part-of: prompting is the first, lightest-weight layer for enforcing structured outputs)
- [[prompt-engineering]]  (example-of: prompting for structure is a specific application of prompt engineering)

## Provenance
- [[sources/ch02-structured-outputs]]
