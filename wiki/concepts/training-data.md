---
type: concept
sources: [ch02-training-data]
---
# Training Data

An AI model is only as good as the data it was trained on: gaps in the training data become gaps in the model's capability, for example a model with no Vietnamese in its training data cannot translate into Vietnamese, or an image classifier trained only on animals will not perform well on photos of plants (AIE p.50). Improving a model on a given task generally means including more data for that task, but collecting sufficient training data at scale is difficult and expensive, so model developers often must rely on whatever data is available even when it does not exactly meet their needs (AIE p.50).

A common source of training data is [[common-crawl]], a large public web-scrape whose quality is questionable — it includes clickbait, misinformation, propaganda, conspiracy theories, racism, and misogyny alongside legitimate content (AIE p.50).

## Key figures
None. See [[common-crawl]] for its own crawl-volume figures.

## Related
- [[common-crawl]]  (example-of: a widely used but low-quality source of training data)
- [[multilingual-models]]  (boundary: training-data gaps in a language directly limit a model's capability in that language)
- [[dataset-engineering]]  (part-of: curating training data is a component of the broader dataset-engineering effort)

## Provenance
- [[sources/ch02-training-data]]
