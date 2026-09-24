---
type: concept
sources: [ch04-cost-and-latency]
---
# Cost and Latency

Cost and latency are two of the practical axes, alongside quality, that a model must be balanced against: a model that generates high-quality outputs but is too slow and expensive to run will not be useful. Many companies opt for lower-quality models in exchange for better cost and latency (AIE p.177). Optimizing for multiple objectives at once (quality, cost, latency) is an active field of study called Pareto optimization; when doing so, it is important to be explicit about which objectives can and cannot be compromised. If an objective such as latency is non-negotiable, one approach is to first set latency expectations for candidate models, filter out models that fail to meet them, and then pick the best remaining model (AIE p.177).

There are multiple metrics for latency, including but not limited to time to first token, time per token, time between tokens, and time per query; which metrics matter depends on the application. Latency depends not only on the underlying model but also on the specific prompt and sampling variables, since autoregressive language models generate output token by token -- more tokens to generate means higher total latency. Total observed latency can be controlled through careful prompting (e.g. instructing the model to be concise), setting a [[stopping-condition]], or other optimization techniques. When evaluating latency, it is important to distinguish must-haves from nice-to-haves: users will always say they want lower latency if asked, but high latency is often an annoyance rather than a deal breaker (AIE p.177).

Cost differs by deployment mode. Model APIs typically charge by token, so the more input and output tokens used, the more expensive the call; many applications try to reduce token counts to manage cost. Self-hosting shifts cost (beyond engineering cost) to compute -- to make the most of available machines, many teams choose the largest model that fits their hardware, which is part of why many popular models cluster around sizes like 7 billion or 65 billion parameters, matching common GPU memory sizes of 16, 24, 48, and 80 GB. With model APIs, cost per token usually does not change much with scale; with self-hosting, cost per token can get much cheaper at scale, since a cluster built to serve up to a fixed number of tokens per day costs the same whether it serves far fewer. This means companies need to periodically reevaluate whether an API or self-hosting makes more sense at their current scale (AIE p.178).

## Key figures
None. The figures in this section (GPU memory sizes, example cost/latency thresholds) are illustrative of a worked example rather than general claims about the concept; the example's numbers live in the linked criteria table context.

## Examples
- [[model-selection-criteria-table]]  (fictional application's worked cost/latency/quality criteria)

## Related
- [[evaluation]]  (part-of: cost and latency are evaluation criteria alongside model quality)
- [[inference-optimization]]  (prerequisite: cost/latency optimization techniques are covered in depth in the book's inference-optimization chapter)
- [[stopping-condition]]  (see-also: one lever for controlling total generation latency)
- [[model-selection-criteria-table]]  (part-of: cost and latency are two of the criteria rows in the example selection table)

## Provenance
- [[sources/ch04-cost-and-latency]]
