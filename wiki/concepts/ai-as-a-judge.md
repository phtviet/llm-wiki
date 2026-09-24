---
type: concept
sources: [ch08-model-distillation, ch03-why-ai-as-a-judge]
---
# AI as a Judge

AI as a judge means using an AI model to evaluate other AI models' outputs, a practice that has been practical since GPT-3 became available in 2020. AI judges are fast, easy to use, and relatively cheap compared to human evaluators, and they can work without reference data, making them usable in production settings where no reference exists. A judge can be asked to score an output against essentially any criterion -- correctness, repetitiveness, toxicity, wholesomeness, hallucination, and more -- much as a person could be asked for an opinion on the same criteria (AIE p.137).

AI judgments are not infallible, but because each AI model aggregates patterns from a mass of training data, its judgments can be representative of mass opinion; with the right prompt and model, this yields reasonably good judgments across a wide range of topics. Studies have found certain AI judges strongly correlated with human evaluators. AI judges can also explain their decisions in addition to producing a score, which is useful for auditing evaluation results. Even where AI judgments fall short of human judgments, they can still be good enough to guide an application's development and give a project enough confidence to get off the ground (AIE p.137-138).

## Key figures
- Zheng et al. (2023) found [[gpt-4|GPT-4]]-to-human agreement of 85% on the MT-Bench benchmark, exceeding the 81% agreement measured among humans themselves (AIE p.137)
- Dubois et al. (2023) found AlpacaEval's AI judges correlate with LMSYS's human-evaluated Chat Arena leaderboard at 0.98 (AIE p.137)

## Examples
- [[specialized-ai-judges]]  (reward models, reference-based judges, and preference models as trained-for-purpose AI judges)

## Related
- [[lmsys-chatbot-arena]]  (see-also: AlpacaEval's AI judges were validated against this human-evaluated leaderboard)
- [[comparative-evaluation]]  (see-also: AI judges are one mechanism for producing pairwise or ranked comparisons)
- [[criteria-ambiguity]]  (boundary: flexibility of judge criteria comes at the cost of inconsistent standardization across tools)
- [[ai-judge-bias]]  (boundary: correlation with humans does not eliminate systematic biases in AI judgments)
- [[ai-judge-cost-and-latency]]  (contrast: AI judges are cheaper and faster than human evaluators, but not free of their own cost/latency trade-offs)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch08-model-distillation]]
- [[sources/ch03-why-ai-as-a-judge]]
