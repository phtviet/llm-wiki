---
type: concept
sources: [ch01-use-case-evaluation]
---
# AI Product Defensibility

Because foundation models lower the barrier to building AI applications, anything easy for a company to build is also easy for competitors, making defensibility a central question for standalone AI products (AIE p.31). Building on top of foundation models means providing a layer on top of those models; if the underlying models expand in capability, that layer risks being subsumed and the application rendered obsolete (AIE p.31). A PDF-parsing app built on the assumption that a base model can't parse PDFs at scale loses its edge if that assumption stops holding — though such an app can still make sense if built on open source models for users who want to self-host (AIE p.31).

The book identifies three general types of competitive advantage: technology, data, and distribution (the ability to get a product in front of users). With foundation models, core technology tends to converge across companies, so the distribution advantage tends to favor big, established companies. The data advantage is more nuanced: big companies typically hold more existing data, but a startup that reaches market first and accumulates usage data can turn that data into a moat, even when user data cannot directly train models, since usage patterns still guide data collection and product decisions (AIE p.31-32).

## Key figures
None.

## Examples
- [[chegg]]  (illustrates how AI-driven disruption threatens an existing product's defensibility)

## Related
- [[model-as-a-service]]  (boundary: low entry barrier from readily available foundation models is the same force that erodes defensibility)
- [[ai-engineering]]  (prerequisite: defensibility concerns arise directly from the low barrier to entry that defines AI engineering)

## Provenance
- [[sources/ch01-use-case-evaluation]]
