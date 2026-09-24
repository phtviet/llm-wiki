---
type: concept
sources: [ch05-defenses-against-prompt-attacks]
---
# Instruction Hierarchy

The instruction hierarchy is a model-level defense against prompt attacks, proposed by OpenAI in 'The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions' (Wallace et al., 2024). Many prompt attacks succeed because a model cannot differentiate system instructions from malicious instructions once they are concatenated into a single input blob; training a model to better follow system prompts closes this gap (AIE p.248).

The hierarchy defines four priority levels, highest first: system prompt, user prompt, model outputs, tool outputs. When instructions conflict, the higher-priority instruction wins; because tool outputs sit at the lowest priority, this neutralizes many indirect prompt injection attacks (AIE p.248). OpenAI trained the hierarchy into a model by synthesizing a dataset of aligned and misaligned instructions and finetuning the model to produce outputs appropriate to the hierarchy (AIE p.248).

Model-level safety finetuning must also address borderline requests -- prompts that could invoke either a safe or an unsafe response, such as asking for the easiest way to break into a locked room. An overly cautious system refuses such requests outright; a better system recognizes the ambiguity and offers a safe answer, such as suggesting a locksmith, balancing safety with helpfulness (AIE p.249).

## Key figures
- Increases robustness by up to 63% while imposing minimal degradation on standard capabilities (AIE p.248)

## Related
- [[prompt-attacks]]  (part-of: a model-level defense within the broader set of prompt-attack defenses)
- [[supervised-finetuning]]  (prerequisite: implemented by finetuning the model on a synthesized dataset of aligned/misaligned instructions)

## Provenance
- [[sources/ch05-defenses-against-prompt-attacks]]
