---
type: concept
sources: [ch08-data-curation]
---
# Data Curation Criteria

Data curation is not just about creating new data to teach a model new behaviors, but also about removing existing data to help a model unlearn bad behaviors. For example, if a chatbot responds to fact-checking requests with unsolicited, arrogant rewrites, investigation may trace the behavior to training examples containing unsolicited suggestions -- the fix is to remove those examples and acquire replacement examples that demonstrate the desired behavior instead (AIE p.367).

At a high level, data curation follows three criteria: [[data-quality]], data coverage, and [[data-quantity]]. By analogy to cooking, data quality is the quality of the ingredients (spoiled ingredients cannot make good food), data coverage is having the right mix of ingredients in the right proportions, and data quantity is how much of each ingredient to use (AIE p.367).

## Key figures
None.

## Examples
- Chatbot trained on annotations containing unsolicited rewrites learns an arrogant, unsolicited-rewriting habit, fixed by removing those examples (AIE p.367)

## Related
- [[data-coverage]]  (part-of: one of the three data curation criteria)
- [[training-data-curation]]  (see-also: this section's three-criteria framework elaborates on curating training data for quality and alignment)
- [[data-cleaning-and-filtering]]  (see-also: removing bad examples from training data parallels cleaning/filtering out low-quality data)
- [[data-quantity]]  (see-also: mentioned in this page's text)
- [[data-quality]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch08-data-curation]]
