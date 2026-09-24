---
type: concept
sources: [ch02-training-data]
---
# Training Data Curation

A model is only as good as the data it was trained on: if a language is absent from
training data, the model cannot handle it, and if a training set only shows one class of
images, the model will not generalize beyond it (AIE p.50). Model developers often face
a 'use what we have, not what we want' constraint, since collecting sufficient data for a
large model is difficult and expensive, so they fall back on broadly available sources
like [[common-crawl]] even when that data does not exactly meet their needs. This
approach can produce models that perform well only on tasks already represented in the
training data, which is why curating datasets aligned to specific languages and domains
matters for applications with narrower needs (AIE p.50).

Training on all available data, general and specialized alike, is common but not
necessarily optimal: more data usually demands more compute and does not always improve
performance. A model trained on a smaller amount of high-quality data can outperform one
trained on a larger amount of low-quality data, making [[data-quality]], not just quantity,
a central curation concern (AIE p.51).

## Key figures
- Using 7B tokens of high-quality coding data, Gunasekar et al. (2023) trained a
  1.3B-parameter model that outperforms much larger models on several coding benchmarks
  (AIE p.51)

## Examples
- [[common-crawl]]  (broad, low-curation web-crawl dataset used despite quality concerns)

## Related
- [[common-crawl]]  (example-of: a widely used but low-curation training data source that illustrates the 'use what we have' problem)
- [[low-resource-languages]]  (boundary: curation for underrepresented languages is one motivation for moving beyond general-purpose crawled data)
- [[dataset-engineering]]  (part-of: curating training data is one aspect of the broader dataset-engineering practice)
- [[domain-specific-models]]  (see-also: domain- and language-specific curation supports models tailored to narrower needs)
- [[data-quality]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-training-data]]
