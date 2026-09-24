---
type: concept
sources: [ch07-finetuning-tactics]
---
# Learning Rate

The learning rate determines how fast a model's parameters change with each learning step -- the step size toward a training goal. Too small a step size can make training take too long; too large a step size can cause the model to overstep the goal and never converge. No universal optimal learning rate exists; it must be found experimentally, typically in the range 1e-7 to 1e-3. A common practice is to take the learning rate at the end of pre-training and multiply it by a constant between 0.1 and 1 (AIE p.359).

The loss curve diagnoses a poorly chosen learning rate: heavy fluctuation suggests the rate is too large, while a stable curve that decreases too slowly suggests it is too small -- the rate should be increased as high as the loss curve remains stable. Learning rates can also vary across training, typically larger early and smaller later; algorithms that schedule this variation are called learning rate schedules (AIE p.359).

## Key figures
- Typical experimental range: 1e-7 to 1e-3 (AIE p.359)
- Common practice: pre-training's final learning rate multiplied by a constant between 0.1 and 1 (AIE p.359)

## Related
- [[finetuning-hyperparameters]]  (part-of: one of the frequently tuned finetuning hyperparameters)
- [[batch-size]]  (see-also: both are core training hyperparameters diagnosed via the loss curve)
- [[backpropagation]]  (prerequisite: learning rate scales the parameter update computed in the backward pass)

## Provenance
- [[sources/ch07-finetuning-tactics]]
