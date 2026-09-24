---
type: concept
sources: [ch08-data-processing]
---
# Data Processing Efficiency

Data processing steps (deduplication, cleaning, filtering, and similar) can each take
hours or days at scale, so the order in which they are applied matters for efficiency:
running the cheaper or more time-saving step first reduces total work. For example, if
cleaning each example is slower than deduplication, duplicates should be removed before
cleaning; if deduplication is slower than filtering out low-quality data, filtering
should come first (AIE p.397).

Other practical tips: always run processing scripts on a small trial subset to validate
they behave as expected before applying them to the full dataset, and avoid modifying
data in place. Keeping a copy of the original data lets a team reprocess it differently
for other applications, and protects against scripts with bugs corrupting the only copy
of the data (AIE p.397). Reading model papers that disclose dataset details is also
highlighted as a source of practical curation and processing tips (AIE p.396).

## Key figures
None.

## Related
- [[data-cleaning-and-filtering]]  (prerequisite: processing-order tips apply to cleaning and filtering steps like these)
- [[data-acquisition]]  (part-of: processing follows acquisition in the dataset engineering pipeline)

## Provenance
- [[sources/ch08-data-processing]]
