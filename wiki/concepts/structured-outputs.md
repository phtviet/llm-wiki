---
type: concept
sources: [ch02-structured-outputs]
---
# Structured Outputs

Structured outputs are model outputs that follow a specified format. They are crucial in two scenarios: (1) tasks that inherently require structured outputs, such as semantic parsing -- converting natural language into a structured, machine-readable format, e.g. text-to-SQL, which lets users query APIs or databases in natural language -- and classification, where outputs must be valid classes; and (2) tasks whose outputs feed downstream applications that need a parsable format, such as an AI-written email delivered as a JSON document with specific keys, which matters especially for agentic workflows where a model's outputs become inputs to tools (AIE p.99-100).

Frameworks supporting structured outputs include guidance, outlines, instructor, and llama.cpp; OpenAI was the first model provider to introduce a JSON mode in its API, though such modes typically guarantee only valid JSON syntax, not correct content, and generation can still be truncated and unparsable if it stops too soon (AIE p.100).

Structured outputs can be enforced at several layers of the AI stack: prompting, post-processing, test time compute, constrained sampling, and finetuning. The first three act as bandages, useful when a model is already fairly good at the format and just needs a nudge; constrained sampling and finetuning are the intensive treatments (AIE p.101).

## Key figures
- Correctly generated JSON percentage observed ranging from 0% to the high 90s%, depending on application and model (AIE p.101)

## Examples
- text-to-SQL and text-to-regex (semantic parsing use cases)
- AI-written email formatted as JSON for a downstream application

## Related
- [[prompting-for-structure]]  (part-of: one of the five layers used to enforce structured outputs)
- [[post-processing]]  (part-of: another of the five layers, correcting common formatting mistakes cheaply)
- [[constrained-sampling]]  (part-of: filters logits to enforce format constraints during sampling)
- [[finetuning]]  (part-of: most effective and general layer, training the model directly on examples in the desired format)
- [[test-time-compute]]  (part-of: regenerating outputs until one fits the expected format)
- [[logits]]  (prerequisite: constrained sampling operates by filtering the logit vector before sampling)

## Provenance
- [[sources/ch02-structured-outputs]]
