---
type: concept
sources: [ch02-structured-outputs]
---
# Prompting for Structured Outputs

Prompting is the first line of action for getting a model to produce structured outputs: instructing the model to generate in a given format. Whether the model complies depends on its [[instruction-following-capability|instruction-following capability]] and the clarity of the instruction, and there is no guarantee it will always follow the instruction (AIE p.101).

To raise the rate of valid outputs, some teams add a second model query that validates and/or corrects the first output — an application of the AI-as-judge approach. This adds at least one extra model query per output, and the added [[cost-and-latency]] can make the approach too expensive for some applications (AIE p.101).

## Key figures
None.

## Related
- [[structured-outputs]]  (part-of: one of the layers at which structured generation can be guided)
- [[ai-as-judge]]  (example-of: using a model to validate/correct another model's output)
- [[post-processing]]  (contrast: fixes output after generation vs. shaping the instruction before generation)
- [[instruction-following-capability]]  (see-also: mentioned in this page's text)
- [[cost-and-latency]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-structured-outputs]]
