---
type: concept
sources: [ch01-three-layers-of-the-ai-stack]
---
# Three Layers of the AI Stack

Any AI application stack has three layers: [[application-development]], [[model-development]], and [[infrastructure]]. When building an AI application, developers typically start at the application-development layer and move down into the lower layers only as needed (AIE p.37).

Application development sits at the top: it involves giving a model good prompts and context, and requires rigorous evaluation and good interfaces. Model development provides tooling for modeling, training, finetuning, and [[inference-optimization]], and because data is central to it, also includes [[dataset-engineering]]; it too requires rigorous evaluation. Infrastructure, at the bottom, covers model serving, managing data and compute, and monitoring (AIE p.37).

A March 2024 analysis of GitHub repositories with at least 500 stars (used as a proxy for ecosystem activity) found that application development and applications saw the highest growth in 2023, following the introduction of Stable Diffusion and ChatGPT, while infrastructure grew much less since core infrastructural needs -- resource management, serving, monitoring -- remain the same regardless of which models or applications are built (AIE p.38).

Despite the excitement around foundation models, many principles of building AI applications persist: applications still need to solve business problems and map business metrics to ML metrics, systematic experimentation is still required (though now over models, prompts, retrieval algorithms, and sampling variables rather than just hyperparameters), and feedback loops for iterative improvement from production data remain essential (AIE p.39).

## Key figures
- 920 total AI-related GitHub repositories with at least 500 stars, found in a March 2024 search (AIE p.38)

## Examples
- [[application-development]]  (top layer)
- [[model-development]]  (middle layer)
- [[infrastructure]]  (bottom layer)

## Related
- [[application-development]]  (part-of: top layer of the AI stack)
- [[model-development]]  (part-of: middle layer of the AI stack)
- [[infrastructure]]  (part-of: bottom layer of the AI stack)
- [[ai-engineering-workflow]]  (see-also: describes the product-first iteration that moves through these layers)
- [[inference-optimization]]  (see-also: mentioned in this page's text)
- [[dataset-engineering]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch01-three-layers-of-the-ai-stack]]
