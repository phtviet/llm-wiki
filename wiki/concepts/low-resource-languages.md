---
type: concept
sources: [ch02-multilingual-models]
---
# Low-Resource Languages

Low-resource languages are languages with limited availability as training data, typically languages that fall outside the list of most-common languages in a dataset like [[common-crawl]] (AIE p.51). Many languages with large numbers of speakers today are nonetheless severely under-represented in web-scraped training corpora; the disparity is measured by the ratio between a language's share of world population and its share of a dataset like Common Crawl, where a higher ratio indicates greater under-representation (AIE p.52).

Under-representation is a major driver of worse model performance in these languages, though a language's structure and the culture it embodies can also make it inherently harder for a model to learn, independent of data volume (AIE p.53).

## Key figures
None. The Common Crawl percentages and world:Common-Crawl ratios that quantify under-representation are dataset-specific figures and live on [[common-crawl]].

## Related
- [[common-crawl]]  (prerequisite: Common Crawl composition is the dataset used to measure a language's under-representation)
- [[multilingual-performance-gap]]  (part-of: under-representation is cited as the primary cause of the multilingual performance gap)

## Provenance
- [[sources/ch02-multilingual-models]]
