---
type: concept
sources: [ch02-model-architecture]
---
# MLP Module

The MLP (multi-layer perceptron) module is one of the two components of a typical [[transformer-architecture]] block, alongside the attention module (AIE p.62). It consists of linear layers (also called feedforward layers) separated by nonlinear activation functions: a linear layer is a weight matrix used for linear transformations, while the activation function lets the layers learn nonlinear patterns by breaking the linearity that would otherwise result from stacking only linear layers (AIE p.62).

Common nonlinear activation functions include ReLU (Rectified Linear Unit), used in earlier models, and GELU, used by GPT-2 and GPT-3 respectively (AIE p.62). ReLU is simple: ReLU(x) = max(0, x) (AIE p.62). Research found that simpler, faster-to-compute activation functions work as well as more sophisticated ones, since a model mainly needs some nonlinearity, and fancier functions cost more compute and memory without improving performance (AIE p.62).

## Key figures
None.

## Related
- [[transformer-architecture]]  (part-of: paired with the attention module inside each transformer block)

## Provenance
- [[sources/ch02-model-architecture]]
