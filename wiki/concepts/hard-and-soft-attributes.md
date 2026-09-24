---
type: concept
sources: [ch04-model-selection-workflow]
---
# Hard and Soft Attributes

When evaluating models, it is useful to differentiate hard attributes (what is
impossible or impractical to change) from soft attributes (what can be improved upon).
Hard attributes often result from decisions made by model providers (licenses,
training data, model size) or from a team's own policies (privacy, control); for some
use cases they can significantly reduce the pool of viable models. Soft attributes are
things like accuracy, toxicity, or factual consistency, which can potentially be
improved (AIE p.179).

What counts as hard versus soft depends on both the model and the use case. Latency,
for example, is soft if you have access to the model to optimize it, but hard if you
use a model hosted by someone else. Estimating how much a soft attribute can be
improved is tricky: one task's accuracy jumped from around 20% to 70% after being
decomposed into two steps, while another model remained unusable for weeks of
tweaking before being abandoned (AIE p.179-180).

## Key figures
- Example task accuracy rose from ~20% to 70% after decomposing the task into two steps (AIE p.179-180)

## Examples
- [[model-build-versus-buy]]  (commercial-API-vs-self-hosting decisions often hinge on hard attributes like licensing and control)

## Related
- [[model-selection-workflow]]  (prerequisite: classifying attributes as hard or soft is the first step in the model selection workflow)
- [[model-build-versus-buy]]  (see-also: both concern narrowing model choices based on constraints)

## Provenance
- [[sources/ch04-model-selection-workflow]]
