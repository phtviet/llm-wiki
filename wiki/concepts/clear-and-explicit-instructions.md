---
type: concept
sources: [ch05-write-clear-and-explicit-instructions]
---
# Write Clear and Explicit Instructions

A core prompt engineering best practice: communicating with a model benefits from the same clarity that helps human communication. The technique breaks into several concrete tips (AIE p.220).

First, explain without ambiguity what the model should do -- for example, specifying the exact scoring scale for grading an essay (1-5 vs 1-10), whether to guess or say 'I don't know' when uncertain, and whether fractional outputs like 4.5 are allowed. Prompts are refined iteratively: observing an undesirable output (e.g. unwanted fractional scores) motivates an explicit instruction ruling it out (AIE p.220).

Second, asking the model to adopt a persona can shift the perspective it uses to generate a response. The book's example: an essay about liking chickens scores 2/5 from a model with no persona, but 4/5 when the model is told to respond as a first-grade teacher (AIE p.220).

Third, providing examples reduces ambiguity about the desired response, functioning as a form of [[few-shot-learning]]. The book's example: a children's chatbot asked 'Will Santa bring me presents on Christmas?' debunks Santa without examples, but affirms Santa's existence once given a prior example about the tooth fairy answered in-character (AIE p.221). Example formatting also has a cost dimension: a terser input-output arrow format ('chickpea --> edible') used 27 tokens versus 38 for a verbose input/output-labeled format for the same classification task on GPT-4, and the cheaper format should be preferred when performance is equal (AIE p.222).

Fourth, specifying the output format matters both for cost/latency (longer outputs cost more per token and increase latency) and for downstream parseability. This includes telling the model to skip preambles (e.g. 'Based on the content of this essay, I'd give it a score of...'), specifying JSON keys, and, for structured-output tasks like classification, using explicit end-of-prompt markers so the model knows where to begin its structured output rather than continuing to append to the input list it was given (AIE p.222-223).

## Key figures
- Terser few-shot example formatting used 27 tokens vs. 38 tokens for an equivalent classification prompt on GPT-4 (AIE p.222)

## Examples
- Essay-grading persona: first-grade-teacher persona raises a chicken essay's score from 2/5 to 4/5 (AIE p.220)
- Santa/tooth-fairy example prompt: a prior in-context example flips the model's answer from debunking to affirming Santa (AIE p.221)
- Classification without markers: a model continues appending items ('chicken tacos --> edible') instead of stopping, absent an explicit end-of-input marker (AIE p.222-223)

## Related
- [[prompt-engineering]]  (part-of: one set of best practices within the broader discipline of adapting model behavior via input alone)
- [[few-shot-learning]]  (example-of: providing examples in a prompt is an application of in-context learning via example shots)
- [[prompt-structure]]  (see-also: examples and task description are compositional parts of a prompt whose ordering and format affect performance)
- [[structured-outputs]]  (prerequisite: writing explicit format instructions and markers is one technique for getting a model to produce structured, machine-readable output)
- [[prompting-for-structure]]  (see-also: instructing a model to follow an output format is the same underlying technique described here in more general terms)

## Provenance
- [[sources/ch05-write-clear-and-explicit-instructions]]
