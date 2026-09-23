---
type: synthesis
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# AI Engineering Versus ML Engineering

The book argues that many enduring principles of ML engineering still apply to AI engineering built on foundation models: mapping business metrics to ML metrics, systematic experimentation, making models faster and cheaper, and setting up feedback loops from production data all persist. What differs, at a high level, in three major ways (AIE p.39-40):

1. Without foundation models, teams must train their own models; with foundation models, AI engineering uses a model someone else already trained, shifting focus from modeling and training toward [[model-adaptation]] (AIE p.39).
2. Foundation models are bigger, more compute-hungry, and higher-latency, increasing pressure for efficient training and [[inference-optimization]], and increasing the need for engineers who can work with GPUs and large compute clusters (AIE p.39).
3. Foundation models produce open-ended outputs, which are more flexible but much harder to evaluate, making [[evaluation]] a much bigger problem in AI engineering (AIE p.39-40).

In short: AI engineering is less about model development from scratch and more about adapting and evaluating models (AIE p.40). This reshapes both major layers of the AI engineering stack: [[model-development]] (modeling/training, [[dataset-engineering]], inference optimization) shifts emphasis away from from-scratch ML knowledge, while [[application-development]] ([[evaluation]], [[prompt-engineering]], [[ai-interface]]) grows in importance because differentiation among applications built on the same shared foundation models must now come from the application layer rather than proprietary model quality (AIE p.40-44).

## Related
- [[model-adaptation]]  (part-of: the central shift this synthesis identifies)
- [[model-development]]  (part-of: one reshaped layer of the stack)
- [[application-development]]  (part-of: the other reshaped layer of the stack, now the main site of differentiation)
- [[inference-optimization]]  (example-of: a model-development responsibility whose importance grows with foundation models)
- [[evaluation]]  (example-of: an application-development responsibility whose importance grows with foundation models)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
