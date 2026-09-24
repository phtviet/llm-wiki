---
type: concept
sources: [ch05-in-context-learning-zero-shot-and-few-shot]
---
# In-Context Learning

In-context learning is teaching a model what to do via prompts alone, without updating weights. The term was introduced by Brown et al. (2020) in the GPT-3 paper, 'Language Models Are Few-shot Learners.' Traditionally a model learns desired behavior during training -- [[pre-training|pre-training]], [[post-training|post-training]], or finetuning -- all of which update weights. The GPT-3 paper showed a model could instead learn a desired behavior, even one different from what it was trained to do, purely from examples given in the prompt: GPT-3 was trained for next-token prediction but could learn from context to do translation, reading comprehension, simple math, and answer SAT questions (AIE p.213).

Because new information can simply be added to the prompt, in-context learning lets a model incorporate information it never trained on, without retraining -- for example, giving a model documentation for a newer software version than it was trained on so it can answer questions beyond its training cutoff. This makes in-context learning a form of continual learning (AIE p.213).

Each example given in the prompt is called a shot. [[few-shot-learning]] teaches a model from examples in the prompt (five examples is 5-shot); [[zero-shot-learning]] provides none. How many examples are needed depends on the model and application, and is bounded by the model's maximum [[context-length]], since more examples lengthen the prompt and raise inference cost (AIE p.213).

Before GPT-3, models could do only what they were explicitly trained to do, so in-context learning was considered surprising. Francois Chollet, creator of the Keras ML framework, compared a [[foundation-model]] to a library of many different programs -- one that writes haikus, another that writes limericks -- each activated by a certain prompt; on this view, prompt engineering is finding the prompt that activates the program you want (AIE p.215).

## Key figures
None.

## Examples
- [[few-shot-learning]]  (in-context learning with examples in the prompt)
- [[zero-shot-learning]]  (in-context learning with no examples)

## Related
- [[prompt-engineering]]  (part-of: in-context learning is the mechanism prompt engineering exploits to shape model behavior)
- [[finetuning]]  (contrast: updates model weights to teach behavior vs. in-context learning teaches via prompt alone, no weight update)
- [[context-length]]  (boundary: the number of in-context examples usable is capped by the model's maximum context length)
- [[few-shot-learning]]  (part-of: shots are the examples that constitute few-shot in-context learning)
- [[foundation-model]]  (see-also: mentioned in this page's text)
- [[post-training]]  (see-also: mentioned in this page's text)
- [[pre-training]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch05-in-context-learning-zero-shot-and-few-shot]]
