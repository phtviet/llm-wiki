---
type: concept
sources: [ch08-clean-and-filter-data]
---
# Data Cleaning and Filtering

Data cleaning and filtering makes training data performant and safe to use. It covers three main jobs: stripping extraneous formatting artifacts (e.g. HTML/Markdown tags left over from web-scraped datasets), removing data that violates policy (PII, sensitive data, copyrighted data, toxic content, and fields like zip code, name, or gender that aren't allowed to be used), and removing low-quality data using [[data-verification]] techniques (AIE p.401).

Manual inspection of data is called out as especially important at this step: staring at the data can surface patterns usable as heuristics for detecting low quality. Such heuristics can be non-obvious -- for example, annotations made in the second half of an annotation session tend to be lower quality, likely from annotator boredom or fatigue (Kern et al., 2024) (AIE p.401).

When there is more data than needed or affordable given a compute budget, teams can filter further using [[active-learning]] to select the most helpful examples for the model to learn from, or importance sampling to find the examples most important to the task. The efficiency of either approach depends on having a good way to evaluate the importance of each training example. Meta researchers, studying data pruning, concluded that good data-pruning metrics can significantly reduce the resource costs of modern deep learning (Sorscher et al., 2022) (AIE p.401).

## Key figures
- Removing extraneous Markdown and HTML tokens improved Databricks' model accuracy by 20% while reducing input token lengths by 60% (AIE p.401)

## Examples
- [[databricks-html-cleaning-example]]  (20% accuracy gain, 60% shorter inputs from stripping HTML/Markdown)

## Related
- [[data-verification]]  (prerequisite: cleaning relies on data-verification techniques to detect low-quality data)
- [[training-data-curation]]  (part-of: cleaning and filtering is one step within curating training data for quality)
- [[dataset-engineering]]  (part-of: data cleaning is part of the broader dataset-engineering discipline)

## Provenance
- [[sources/ch08-clean-and-filter-data]]
