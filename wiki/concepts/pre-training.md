---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Pre-training

Pre-training refers to training a model from scratch, with weights randomly initialized (AIE p.41). For LLMs, pre-training often means training for text completion. It is by far the most resource-intensive training step: for the [[instructgpt]] model, pre-training takes up to 98% of the overall compute and data resources (AIE p.41).

Pre-training takes a long time, and a small mistake can cause significant financial loss and set a project back substantially. Because of this resource intensity, pre-training large models is a specialized art practiced by relatively few people, who are consequently heavily sought after (AIE p.41).

## Key figures
- Pre-training takes up to 98% of the overall compute and data resources for the InstructGPT model (AIE p.41)

## Related
- [[finetuning]]  (contrast: trains from randomly initialized weights vs. continues training from existing weights)
- [[post-training]]  (see-also: pre-training and post-training form a spectrum with similar processes and tooling)
- [[model-adaptation]]  (boundary: pre-training is training from scratch, outside the model-adaptation techniques this section focuses on)
- [[instructgpt]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
