---
type: concept
sources: [ch02-domain-specific-models]
---
# Domain-Specific Models

General-purpose foundation models like Gemini, GPTs, and Llamas perform well across many domains largely because those domains are present in their training data (AIE p.56). But they are unlikely to perform well on domain-specific tasks they never saw during training, especially ones involving data that is scarce or hard to obtain publicly -- such as drug discovery (protein, DNA, and RNA data, expensive to acquire) and cancer screening (X-ray and fMRI scans, restricted by privacy) (AIE p.57).

To perform well on such tasks, a model typically needs training on very specific curated datasets. Domain-specific models are especially common in biomedicine, but the same logic extends to other fields -- e.g. a model trained on architectural sketches or factory plans could outperform a generic model like Stable Diffusion or ChatGPT on those tasks (AIE p.57).

## Key figures
None. Figures in this section (dataset sizes, benchmark accuracies) are entity-specific and live on the relevant entity pages.

## Examples
- [[alphafold]]  (trained on protein sequences and 3D structures; DeepMind)
- [[bionemo]]  (NVIDIA model for biomolecular drug-discovery data)
- [[med-palm2]]  (Google LLM combined with medical data)

## Related
- [[foundation-model]]  (prerequisite: domain-specific performance is discussed as a limitation of general-purpose foundation models)
- [[clip]]  (example-of: benchmark performance used to infer a general-purpose model's domain coverage)
- [[model-distillation]]  (contrast: distillation compresses an existing model's knowledge, whereas domain-specific models are built from curated domain data)

## Provenance
- [[sources/ch02-domain-specific-models]]
