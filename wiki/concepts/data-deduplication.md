---
type: concept
sources: [ch08-deduplicate-data]
---
# Data Deduplication

Data deduplication is the removal of duplicated examples from a training dataset.
Duplicated data can skew a dataset's distribution, introduce biases (e.g. leading a
model to wrongly associate a color with a price because the duplicated example
dominates), and cause test set contamination when a duplicate of a training example
ends up in the test set (AIE p.399).

What counts as a duplicate depends on definitional choices: the granularity
(document, paragraph, sentence, or token level), whether a match must be exact or
only partially overlapping (e.g. 80%), and whether reordered lists of the same items
count as duplicates. Duplication itself takes several forms: whole-document
duplication (the same document appears more than once), intra-document duplication
(the same paragraph repeats within one document), and cross-document duplication
(the same quote appears across multiple documents) (AIE p.399-400).

Deduplication reuses the same similarity-measurement techniques used for general
similarity comparison, and the same task underlies identity resolution (e.g.
determining whether two social media profiles are the same identity). Three concrete
approaches are used in practice: pairwise comparison of every example against every
other example (via [[exact-match]], n-gram match, fuzzy match, or semantic similarity),
which can be expensive at scale; hashing examples into buckets (e.g. via MinHash or
Bloom filter) and comparing only within a bucket; and dimensionality reduction
applied before pairwise comparison, reusing techniques from vector search (AIE p.400).

## Key figures
- Repeating 0.1% of training data 100 times degraded an 800M-parameter model's
  performance to that of a 400M-parameter model, even though the other 90% of
  training tokens remained unique (Hernandez et al., 2022) (AIE p.399)

## Examples
- [[minhash]]  (hashing-based deduplication technique)
- [[bloom-filter]]  (hashing-based deduplication technique)

## Related
- [[data-cleaning-and-filtering]]  (part-of: deduplication is one data-processing step alongside cleaning and filtering of training data)
- [[data-contamination]]  (boundary: deduplication addresses train/test duplication, a specific cause of the contamination that inflates evaluation scores)
- [[semantic-similarity]]  (prerequisite: pairwise deduplication reuses similarity-measurement techniques such as embedding-based semantic similarity)
- [[vector-database]]  (see-also: dimensionality-reduction deduplication reuses techniques from vector search)
- [[exact-match]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch08-deduplicate-data]]
