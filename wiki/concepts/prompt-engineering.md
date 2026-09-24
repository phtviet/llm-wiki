---
type: concept
sources: [ch05-prompt-engineering]
---
# Prompt Engineering

Prompt engineering is the process of crafting an instruction that gets a model to generate a desired outcome. It is the easiest and most common model adaptation technique: unlike [[finetuning]], it guides a model's behavior without changing the model's weights (AIE p.211). Because foundation models have strong base capabilities, many applications can be adapted using prompt engineering alone, and it is recommended to exhaust prompting before moving to more resource-intensive techniques like finetuning (AIE p.211).

Despite its apparent simplicity, prompt engineering is not merely 'fiddling with words' -- it involves substantive challenges and solutions, and can be thought of as a form of human-to-AI communication: writing a prompt is easy, but writing an effective one is not (AIE p.211). Prompt experiments warrant the same rigor as any ML experiment, with systematic experimentation and [[evaluation]]. Prompt engineering alone is not sufficient to build production-ready AI applications; it must be paired with statistics, engineering, and classic ML knowledge for experiment tracking, evaluation, and dataset curation (AIE p.212).

## Key figures
None.

## Examples
Omit -- covered by linked technique pages such as [[chain-of-thought-prompting]], [[in-context-learning]], and [[structured-outputs]].

## Related
- [[finetuning]]  (contrast: changes model weights vs. prompt engineering leaves them unchanged)
- [[model-adaptation]]  (part-of: prompt engineering is one of the two model-adaptation branches, alongside finetuning)
- [[evaluation]]  (prerequisite: rigorous prompt engineering requires systematic evaluation of results)

## Provenance
- [[sources/ch05-prompt-engineering]]
