---
type: concept
sources: [ch03-limitations-of-ai-as-a-judge]
---
# Increased Costs and Latency of AI Judges

Using a powerful model as an AI judge adds real cost and latency to an application. If the same model both generates and evaluates responses (e.g. GPT-4 for both), API costs roughly double; evaluating three separate criteria (e.g. overall quality, factual consistency, toxicity) with three prompts roughly quadruples the number of calls (AIE p.144).

Costs can be reduced by using weaker models as judges, or by spot-checking -- evaluating only a subset of responses rather than all of them. Spot-checking trades confidence for cost: evaluating a larger fraction of samples gives higher confidence but costs more, and finding the right balance takes trial and error. Even so, AI judges remain much cheaper than human evaluators (AIE p.144).

Running an AI judge before returning a response to users adds latency, forcing a trade-off between reduced risk and slower responses -- a trade-off that can be a nonstarter for applications with strict latency requirements (AIE p.144).

## Key figures
- Using the same model to both generate and judge responses roughly doubles API costs; three evaluation criteria roughly quadruples call volume (AIE p.144)

## Related
- [[ai-as-a-judge]]  (boundary: cost and latency are practical limitations on deploying AI judges, especially in production)

## Provenance
- [[sources/ch03-limitations-of-ai-as-a-judge]]
