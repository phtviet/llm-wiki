---
type: concept
sources: [ch02-sampling-strategies]
---
# Temperature

Temperature is a constant used to adjust logits before the softmax transformation, applied during [[sampling]]. For a given temperature T, each logit is divided by T before softmax is computed, so the adjusted logit for token i is x_i / T (AIE p.90).

A higher temperature reduces the probabilities of common tokens and increases the probabilities of rarer ones, making the model's output more creative but potentially less coherent. A lower temperature makes the model more likely to pick the highest-logit value, making output more consistent but potentially more boring (AIE p.91). Technically temperature can never be exactly 0, since logits can't be divided by 0; in practice, setting temperature to 0 makes the model just pick the token with the largest logit directly, skipping logit adjustment and softmax (AIE p.92).

## Key figures
- With logits [1, 2] for outputs A and B: at temperature 1 (no adjustment), softmax probabilities are [0.27, 0.73], so B is picked 73% of the time; at temperature 0.5, probabilities become [0.12, 0.88], so B is picked 88% of the time (AIE p.91)
- Model providers typically limit temperature to between 0 and 2; a temperature of 0.7 is often recommended for creative use cases as a balance of creativity and predictability (AIE p.91)

## Related
- [[sampling]]  (part-of: temperature is one strategy for controlling how a token is sampled from a probability distribution)
- [[softmax]]  (prerequisite: temperature adjusts logits before softmax is applied to them)
- [[logit-vector]]  (prerequisite: temperature divides raw logits by T before any probability is computed)
- [[top-k-sampling]]  (contrast: adjusts which tokens are considered rather than reshaping the whole distribution)
- [[top-p-sampling]]  (contrast: dynamically bounds the candidate set by cumulative probability rather than rescaling logits)

## Provenance
- [[sources/ch02-sampling-strategies]]
