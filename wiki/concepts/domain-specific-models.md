---
type: concept
sources: [ch02-domain-specific-models]
---
# Domain-Specific Models

Domain-specific models are trained or curated to perform well on tasks that general-purpose foundation models handle poorly, especially tasks never seen during training. General-purpose models like Gemini, GPTs, and Llamas perform well across many domains largely because those domains are present in their training data, but they are unlikely to perform well on domain-specific tasks such as drug discovery or cancer screening, where the relevant data (protein/DNA/RNA sequences, X-ray and fMRI scans) is expensive, specialized, and rarely found in publicly available internet data due to cost or privacy constraints (AIE p.57). To train a model for such tasks, developers typically need to curate very specific datasets (AIE p.57).

Domain-specific models are especially common in biomedicine, but the book notes other fields could benefit similarly -- for example, a model trained on architectural sketches or on factory plans could outperform a generic model like Stable Diffusion or ChatGPT in those narrow domains (AIE p.57).

## Key figures
None. Figures cited in this section (e.g. protein counts, benchmark accuracies) are entity-specific and live on the relevant entity pages.

## Examples
- [[alphafold]]  (trained on protein sequences and structures; canonical biomedical domain-specific model)
- [[clip]]  (general-purpose image-language model, contrasted against domain performance)

## Related
- [[clip]]  (contrast: general-purpose embedding model whose benchmark performance is used to illustrate domain coverage gaps)
- [[foundation-model]]  (boundary: domain-specific models are curated for narrow tasks where general-purpose foundation models underperform)

## Provenance
- [[sources/ch02-domain-specific-models]]
