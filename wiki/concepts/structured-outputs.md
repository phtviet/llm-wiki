---
type: concept
sources: [ch02-structured-outputs]
---
# Structured Outputs

Structured outputs are model outputs that follow a specific, machine-readable format. They matter in two scenarios: tasks that inherently require structured outputs, such as semantic parsing (e.g. text-to-SQL, text-to-regex, classification into valid classes), and tasks whose outputs feed downstream applications that need to parse them, such as agentic workflows where a model's output becomes a tool's input (AIE p.99-100).

Frameworks supporting structured outputs include guidance, outlines, instructor, and llama.cpp. OpenAI was the first model provider to introduce a JSON mode in its text generation API; an API's JSON mode typically guarantees only that output is valid JSON, not that its content is correct, and outputs can still be truncated and unparsable if generation stops too soon (AIE p.100).

Structured outputs can be guided at different layers of the AI stack: [[prompting-for-structure]], [[post-processing]], test-time compute (repeated generation until the format fits), [[constrained-sampling]], and [[finetuning-for-structure]]. The first three work best as light nudges when a model is already fairly good at the format; constrained sampling and finetuning are the more intensive treatments (AIE p.101).

## Key figures
- Correctly generated JSON object rates observed ranging from 0% up to the high 90s% depending on application and model (AIE p.101)

## Examples
- [[prompting-for-structure]]
- [[post-processing]]
- [[constrained-sampling]]
- [[finetuning-for-structure]]

## Related
- [[logit-vector]]  (prerequisite: constrained sampling filters the logit vector to keep only tokens meeting the constraints)
- [[sampling]]  (part-of: structured-output techniques act on or around the sampling step)
- [[ai-as-judge]]  (example-of: using a second model query to validate/correct structured output is an application of AI-as-judge)

## Provenance
- [[sources/ch02-structured-outputs]]
