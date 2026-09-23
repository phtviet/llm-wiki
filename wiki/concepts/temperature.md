---
type: concept
sources: [ch02-sampling-strategies]
---
# Temperature

Temperature is a constant that adjusts a model's [[logits]] before the [[softmax]] transformation, by dividing each logit by the temperature value (AIE p.90). A higher temperature reduces the probabilities of common tokens and increases the probabilities of rarer ones, producing more creative but potentially less coherent outputs; a lower temperature makes outputs more consistent but potentially more boring (AIE p.91). Model providers typically limit temperature to between 0 and 2, though a model owner can use any non-negative value (AIE p.91). Technically temperature can never be exactly 0, since logits can't be divided by zero; in practice, setting temperature to 0 makes the model simply pick the highest-logit token directly, skipping logit adjustment and softmax (AIE p.92).

## Key figures
- With logits [1, 2] for outputs A and B: temperature 1 (default) gives probabilities [0.27, 0.73]; temperature 0.5 gives [0.12, 0.88] (AIE p.91)
- Model providers typically cap temperature between 0 and 2 (AIE p.91)
- A temperature of 0.7 is often recommended for creative use cases, balancing creativity and predictability (AIE p.91)

## Related
- [[logits]]  (prerequisite: temperature adjusts logits directly)
- [[softmax]]  (prerequisite: the adjusted logits are then passed through softmax)
- [[sampling]]  (part-of: temperature is one sampling strategy among several for shaping model output)
- [[top-k-sampling]]  (contrast: both shape output diversity, but temperature rescales probabilities while top-k restricts the candidate set)

## Provenance
- [[sources/ch02-sampling-strategies]]
