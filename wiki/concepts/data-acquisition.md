---
type: concept
sources: [ch08-data-acquisition-and-annotation]
---
# Data Acquisition

Data acquisition is the process of producing a sufficiently large dataset with the quality and diversity a project needs, while respecting user privacy and complying with regulations. It involves sourcing public data, purchasing proprietary data, annotating data, and synthesizing data, and there is a growing research niche on how to best acquire a dataset meeting specific requirements given a budget (AIE p.377).

The most valuable source is typically an application's own data, since it is perfectly relevant and matches the distribution of data the team cares about; a [[data-flywheel]] that leverages user-generated data to continually improve a product is a significant advantage. Before investing in creating new data, teams should check available datasets in data marketplaces, since a dataset can be developed from multiple sources via multiple acquisition channels. A worked example walks a dataset from 10,000 raw examples through quality filtering, manual response-writing, and synthetic-instruction generation up to 11,000 high-quality examples, illustrating how curation mixes filtering, manual annotation, and synthesis rather than following one clean step (AIE p.378).

## Key figures
None. The example's example figures (10,000 to 11,000 examples across curation steps) are illustrative of the process rather than load-bearing about the concept itself.

## Examples
- [[public-dataset-resources]] (repositories for sourcing publicly available data)

## Related
- [[data-annotation]] (part-of: annotation is one acquisition method alongside sourcing, purchasing, and synthesizing data)
- [[data-synthesis]] (part-of: synthesizing data is one acquisition method used when available data is insufficient)
- [[data-flywheel]] (example-of: user-generated application data as the ideal acquisition source)
- [[training-data-curation]] (see-also: acquisition feeds into the broader curation process for training data quality)

## Provenance
- [[sources/ch08-data-acquisition-and-annotation]]
