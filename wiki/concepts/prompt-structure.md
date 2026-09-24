---
type: concept
sources: [ch05-introduction-to-prompting]
---
# Prompt Structure

A prompt generally consists of one or more of three parts: a task description (what the model should do, including any role and output format), example(s) of how to do the task, and the concrete task itself (the specific question or item to process). For instance, a named-entity-recognition prompt might state the task description, then present the text to analyze (AIE p.212).

How much prompting is needed to get good behavior depends on the model: prompting effectiveness assumes the model can follow instructions in the first place, and a model that can't follow instructions well will not respond correctly no matter how the prompt is structured. Model developers have found that prompt structure interacts with model idiosyncrasy: most models, including [[gpt-4]], empirically perform better when the task description comes at the beginning of the prompt, while others, including Llama 3, seem to perform better when it comes at the end (AIE p.213).

## Key figures
None.

## Examples
- named-entity-recognition prompt (task description followed by the text to tag)

## Related
- [[prompt-engineering]]  (part-of: prompt structure is the compositional basis prompt engineering manipulates)
- [[instruction-following-capability]]  (prerequisite: a model must be able to follow instructions for prompt structure choices to matter)
- [[model-robustness]]  (see-also: how sensitive a model's output is to small changes in prompt structure/wording)
- [[gpt-4]]  (example-of: performs better with task description placed at the start of the prompt)

## Provenance
- [[sources/ch05-introduction-to-prompting]]
