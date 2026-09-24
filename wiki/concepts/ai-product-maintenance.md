---
type: concept
sources: [ch01-maintenance]
---
# AI Product Maintenance

Maintaining an AI product means planning for how it will change over time, an added challenge given AI's fast pace of change: building on foundation models today means committing to keep up with continuous shifts in the underlying technology (AIE p.34).

Some changes are beneficial but still cause friction: context lengths are getting longer, model outputs are getting better, and [[inference-optimization|inference]] is getting faster and cheaper, yet teams must constantly run a cost-benefit analysis of each technology investment, since the best option today can become the worst option tomorrow (AIE p.34). An in-house model that looks cheaper than a provider's API can become the expensive option months later if the provider cuts prices; a third-party solution built into your infrastructure can disappear if its provider goes out of business (AIE p.34).

Some changes are easier to adapt to: as model providers converge on similar APIs, swapping one model for another is getting simpler, though each model's quirks still require adjusting workflows, prompts, and data, which is painful without proper versioning and evaluation infrastructure (AIE p.34).

Other changes are harder to adapt to, especially regulatory ones. AI resources (compute, talent, data) are treated as national security concerns and are heavily regulated; compute availability can change overnight due to new export or sale restrictions (AIE p.35). Some changes can be fatal to a product: evolving intellectual-property regulation around AI-usage and training data leaves open the question of whether a product's IP will remain the developer's own, which makes IP-heavy companies such as game studios hesitant to adopt AI (AIE p.35).

## Key figures
- Europe's GDPR was estimated to cost businesses $9 billion to become compliant (AIE p.35)

## Related
- [[inference-optimization]]  (part-of: faster/cheaper inference is one of the 'good changes' maintenance must still manage)
- [[model-as-a-service]]  (boundary: relying on a model provider risks price shifts or provider shutdown, a maintenance risk)

## Provenance
- [[sources/ch01-maintenance]]
