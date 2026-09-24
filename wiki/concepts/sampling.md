---
type: concept
sources: [ch02-sampling-strategies]
---
# Sampling

Sampling is the process of choosing an outcome from a model's computed probability distribution, such as picking the next token for a [[language-model]]. The choice of sampling strategy shapes an application's outputs: one strategy can make generations more creative, another more predictable (AIE p.90). Building a custom sampling strategy typically requires access to the model's logits (AIE p.90).

Common strategies include [[temperature]] (rescales logits before softmax to trade off creativity against coherence), [[greedy-sampling]] (always picks the highest-probability outcome), [[top-k-sampling]] (restricts sampling to the k highest-logit tokens), and [[top-p-sampling]] (dynamically bounds the candidate set by cumulative probability). A [[stopping-condition]] determines when an autoregressive generation process ends. Model providers commonly expose sampled-token probabilities as [[logprobs]] (AIE p.90-95).

## Key figures
None. Strategy-specific figures live on each strategy's own page.

## Examples
- [[temperature]]  (adjusts logits before softmax)
- [[top-k-sampling]]  (restricts candidates to k highest logits)
- [[top-p-sampling]]  (nucleus sampling, dynamic cumulative-probability cutoff)
- [[greedy-sampling]]  (always picks highest-probability outcome)

## Related
- [[logit-vector]]  (prerequisite: sampling strategies operate on the logit vector a model outputs)
- [[softmax]]  (prerequisite: many sampling strategies operate on the probability distribution softmax produces)
- [[greedy-sampling]]  (example-of: a degenerate sampling strategy that always takes the highest-probability outcome)
- [[logprobs]]  (part-of: exposed sampled probabilities are typically surfaced to users as logprobs)
- [[autoregressive-language-model]]  (prerequisite: sampling is how this model type selects each generated token)
- [[language-model]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-sampling-strategies]]
