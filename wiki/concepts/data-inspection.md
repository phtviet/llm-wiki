---
type: concept
sources: [ch08-inspect-data]
---
# Data Inspection

Data inspection is the practice of manually examining a raw dataset to assess its quality before using it for training. It starts with basic provenance questions: where the data comes from, how it has been processed, and what else it has been used for (AIE p.397).

Practical inspection techniques include plotting distributions of token frequency, input length, response length, special-token usage, and topic/language coverage, then asking how relevant those topics and languages are to the task at hand. These distributions can be broken down by data source, time, or annotator to surface patterns, such as which question types tend to get longer or shorter responses or higher or lower scores, and to spot outliers worth investigating (AIE p.397-398). When examples carry more than one annotation, computing inter-annotator disagreement and manually resolving conflicting annotations is part of the same process (AIE p.398).

Beyond automated statistics, the section stresses that manual inspection is irreplaceable: staring at data directly surfaces insights that tooling misses. Recommended manual checks include re-annotating a sample of examples to check whether personal annotations match the given ones (a trustworthiness check on the annotation process), fact-checking responses, and searching for duplicate or near-duplicate examples -- the same query with different responses, or the same response with different queries (AIE p.398-399).

## Key figures
None.

## Examples
- [[gpt-instruction-tuning-comparison-study]]  (Microsoft researchers' verb-noun-pair and response-length analysis comparing GPT-3 and [[gpt-4|GPT-4]] outputs)

## Related
- [[data-quality]]  (prerequisite: inspecting data is how quality issues are identified before curation decisions are made)
- [[data-cleaning-and-filtering]]  (prerequisite: inspection findings inform what gets removed or filtered)
- [[data-annotation]]  (see-also: inter-annotator disagreement checks apply inspection to annotated data)
- [[evaluation]]  (see-also: the same distributional analysis used to inspect training data can be used to evaluate model outputs)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch08-inspect-data]]
