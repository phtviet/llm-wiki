---
type: concept
sources: [ch08-data-quality]
---
# Data Quality

Data quality, for finetuning, means data that helps a model learn efficiently and reliably. Broader data-quality frameworks name up to seven or more dimensions (completeness, uniqueness, validity, timeliness, accuracy, consistency, fitness for purpose, plus Wikipedia's accessibility, comparability, credibility, flexibility, and plausibility), but the book narrows the question to finetuning and gives six characteristics: relevant, aligned with task requirements, consistent, correctly formatted, sufficiently unique, and compliant (AIE p.368).

A small amount of high-quality data can outperform a large amount of noisy data. Relevance means training examples match the task's domain and era -- a 19th-century legal dataset is irrelevant to a modern legal-question task but highly relevant to a task about 19th-century law. Alignment with task requirements means annotations match what the task actually demands (factual correctness for factual tasks, creativity for creative tasks, concise answers when conciseness is required, or a score plus justification when both are required) -- the book uses "aligned" rather than "accurate" or "correct" since the right response depends on the task. Consistency means annotations shouldn't vary too much across examples or annotators, since inconsistency confuses a model during learning; a good annotation guideline supports both alignment and consistency. Correct formatting means examples follow the format the model expects, with redundant formatting tokens (e.g. scraped HTML tags), trailing whitespace, inconsistent casing, and inconsistent numerical formats removed, since they can interfere with learning. Sufficient uniqueness refers to avoiding excessive duplication, which can introduce bias and cause data contamination, though tolerance for duplication varies by use case. Compliance means the data conforms to internal and external policies, laws, and regulations -- for example, excluding PII where its use is prohibited (AIE p.368-369).

## Key figures
None. The characteristics are qualitative; load-bearing figures from specific studies illustrating this concept live on their own pages.

## Examples
- [[lima-study]]  (1,000 curated prompts and responses outperform data volume)
- [[yi-model-family]]  (10K curated instructions outperform hundreds of thousands of noisy ones)

## Related
- [[llama-3]]  (example-of: Llama 3 team found human-generated data more error-prone for nuanced safety policies and built AI-assisted annotation tools to raise data quality)
- [[data-annotation]]  (prerequisite: a good annotation guideline is essential for consistent, aligned annotations)
- [[data-cleaning-and-filtering]]  (see-also: removing formatting tokens and low-quality data overlaps with the correctly-formatted and relevant characteristics)
- [[data-curation-criteria]]  (part-of: data quality's characteristics inform the broader quality/coverage/quantity curation criteria)

## Provenance
- [[sources/ch08-data-quality]]
