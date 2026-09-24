---
type: entity
sources: [ch08-clean-and-filter-data]
---
# Databricks HTML/Markdown Cleaning Result

Databricks found that removing extraneous Markdown and HTML tokens -- formatting artifacts common in datasets scraped from the internet -- from their training data improved their model's accuracy while also shortening input token lengths (AIE p.401). It is cited in the book as a concrete illustration of the payoff from the formatting-token-removal step of [[data-cleaning-and-filtering]].

## Key figures
- Removing extraneous Markdown/HTML tokens improved model accuracy by 20% (AIE p.401)
- Reduced input token lengths by 60% (AIE p.401)

## Related
- [[data-cleaning-and-filtering]]  (example-of: illustrates the payoff of stripping formatting tokens during data cleaning)

## Provenance
- [[sources/ch08-clean-and-filter-data]]
