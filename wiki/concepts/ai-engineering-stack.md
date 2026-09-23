---
type: concept
sources: [ch01-three-layers-of-the-ai-stack]
---
# Three Layers of the AI Stack

Any AI application stack has three layers: application development, model development,
and infrastructure. When developing an AI application, work typically starts at the top
layer and moves down as needed (AIE p.37).

[[application-development]] involves providing a model with good prompts and necessary
context, and requires rigorous evaluation and good interfaces. [[model-development]]
provides tooling for modeling, training, finetuning, and inference optimization, and
since data is central to it, also contains dataset engineering; it likewise requires
rigorous evaluation. [[infrastructure]] sits at the bottom, covering model serving,
managing data and compute, and monitoring (AIE p.37).

To gauge how the landscape has evolved with foundation models, a March 2024 search of
GitHub for AI-related repositories with at least 500 stars (used as a proxy for
understanding the ecosystem) found a total of 920 repositories, including application
and model repositories as products of the top two layers, tracked cumulatively by
category over time (AIE p.38).

## Key figures
- 920 total GitHub repositories (AI-related, ≥500 stars) found in a March 2024 search used as an ecosystem proxy (AIE p.38)

## Related
- [[application-development]]  (part-of: top layer of the stack, covering evaluation, prompt engineering, and AI interface)
- [[model-development]]  (part-of: middle layer of the stack, covering modeling/training, dataset engineering, and inference optimization)
- [[infrastructure]]  (part-of: bottom layer of the stack, covering serving, data/compute management, and monitoring)
- [[ai-engineering]]  (see-also: the stack is the structural breakdown of the AI engineering discipline)

## Provenance
- [[sources/ch01-three-layers-of-the-ai-stack]]
