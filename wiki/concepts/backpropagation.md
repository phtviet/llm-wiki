---
type: concept
sources: [ch07-backpropagation-and-trainable-parameters]
---
# Backpropagation

Backpropagation is the mechanism most neural networks are trained with (AIE p.320). Each training step has two phases: a forward pass, which computes the output from the input, and a backward pass, which updates the model's weights using signals aggregated from the forward pass. During inference, only the forward pass runs; during training, both run (AIE p.320).

The backward pass works in three steps. First, the computed output is compared against the expected output (ground truth); the difference is the loss. Second, the gradient -- how much each trainable parameter contributes to the loss -- is computed as the derivative of the loss with respect to that parameter, giving one gradient value per trainable parameter. A parameter with a high gradient contributes significantly to the loss and should be adjusted more. Third, parameter values are adjusted according to their gradients, with the adjustment size determined by an [[optimizer]] (AIE p.321).

During the backward pass, each trainable parameter carries additional stored values -- its gradient and its optimizer states -- so more trainable parameters require more memory to train (AIE p.321).

## Key figures
None.

## Examples
- [[adam-optimizer]]  (dominant optimizer for transformer-based models)

## Related
- [[trainable-parameters]]  (prerequisite: backpropagation is the mechanism that updates trainable parameters)
- [[optimizer]]  (part-of: the optimizer determines the size of the backward-pass parameter adjustment)
- [[model-parameters]]  (part-of: trainable parameters are a subset of a model's total parameters)

## Provenance
- [[sources/ch07-backpropagation-and-trainable-parameters]]
