---
type: concept
sources: [ch05-give-the-model-time-to-think]
---
# Chain-of-Thought Prompting

Chain-of-thought (CoT) prompting explicitly asks a model to think step by step, nudging it toward a more systematic approach to problem solving. It was introduced in Wei et al., 2022, almost a year before ChatGPT came out, and is among the first prompting techniques that work well across models (AIE p.227). It improved the performance of models of different sizes -- LaMDA, GPT-3, and PaLM -- across benchmarks including MAWPS, SVAMP, and GSM-8K (AIE p.227). LinkedIn found that CoT also reduces models' hallucinations (AIE p.227).

The simplest form of CoT adds a phrase like 'think step by step' or 'explain your decision' to a prompt, letting the model work out its own steps. A prompt can instead specify the exact steps to follow, or include a worked example of the steps (one-shot CoT), rather than leaving step generation zero-shot (AIE p.227-228).

CoT, like [[prompt-decomposition]], can increase the latency a user perceives, since the model performs multiple intermediate steps before the first output token appears -- especially costly when the model is left to come up with its own steps (AIE p.229).

## Key figures
None.

## Examples
- Zero-shot CoT: appending 'Think step by step before arriving at an answer' to a query (AIE p.228)
- One-shot CoT: including a worked example (e.g. comparing shark and dolphin speeds) before the actual query (AIE p.228)

## Related
- [[self-critique-prompting]]  (see-also: both nudge a model to think more before finalizing an answer; often paired)
- [[prompt-decomposition]]  (contrast: decomposition splits a task into chained prompts, CoT elongates a single response; boundary: both raise perceived latency for the same reason -- multiple steps before the first visible token)
- [[hallucination]]  (boundary: LinkedIn found CoT reduces hallucination rates, though the section does not explain the mechanism)

## Provenance
- [[sources/ch05-give-the-model-time-to-think]]
