---
type: entity
sources: [ch02-multilingual-models]
---
# Common Crawl

Common Crawl is a large, publicly available web-scrape dataset used, in some variation, by most foundation models that disclose their training data sources, including OpenAI's GPT-3 and Google's Gemini; the author suspects it is also used by models that do not disclose sources (AIE p.51). Its raw, unfiltered nature illustrates a "use what we have, not what we want" approach to data collection, which can produce models that perform well on tasks represented in the data but not necessarily on the tasks a practitioner cares about (AIE p.51). Some teams apply heuristics to filter it -- for example, OpenAI trained GPT-2 only on Reddit links with at least three upvotes (AIE p.51).

Common Crawl's language composition is heavily skewed toward English, which is the main documented driver of foundation models' weaker performance in other, especially low-resource, languages; see [[multilingual-models]] (AIE p.51-54).

## Key figures
- English is 45.8786% of Common Crawl, Russian (second place) is 5.9692% (Lai et al., 2023) (AIE p.51)
- Under-represented language examples (world population % vs. % in Common Crawl): Punjabi 1.41% vs. 0.0061%, Urdu 2.89% vs. 0.0274%, Bengali 3.40% vs. 0.0930% (Lai et al., 2023) (AIE p.52)

## Related
- [[multilingual-models]]  (prerequisite: its skewed language distribution underlies documented cross-language performance gaps)
- [[dataset-engineering]]  (example-of: a raw, uncurated data source contrasted with deliberate curation for specific needs)

## Provenance
- [[sources/ch02-multilingual-models]]
