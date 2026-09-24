---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Model Development

Model development is the layer of the [[ai-engineering]] stack most commonly associated with traditional ML engineering. It has three main responsibilities: modeling and training, [[dataset-engineering]], and [[inference-optimization]] (AIE p.40). Evaluation is also required at this layer, but is more commonly encountered first at the application-development layer (AIE p.40).

Modeling and training covers coming up with a model architecture, training it, and finetuning it, using tools such as TensorFlow, Hugging Face Transformers, and PyTorch. It traditionally requires specialized ML knowledge — algorithm types (clustering, logistic regression, decision trees, collaborative filtering), neural network architectures (feedforward, recurrent, convolutional, transformer), and concepts like gradient descent, loss functions, and regularization. With foundation models, this knowledge is no longer a must-have for building AI applications, though it remains valuable for expanding the tools available and for troubleshooting (AIE p.41).

## Key figures
None.

## Examples
- [[dataset-engineering]]
- [[inference-optimization]]

## Related
- [[application-development]]  (contrast: the other main layer of the AI engineering stack, focused on differentiation via the application rather than the model)
- [[dataset-engineering]]  (part-of: one of its three responsibilities)
- [[inference-optimization]]  (part-of: one of its three responsibilities)
- [[ai-engineering-versus-full-stack-engineering]]  (see-also: model development is the layer where AI engineering diverges least, and most, from ML engineering, depending on the responsibility)
- [[ai-engineering]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
