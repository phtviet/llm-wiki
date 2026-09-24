---
type: entity
sources: [ch02-training-data]
---
# Common Crawl

Common Crawl is a dataset created by a nonprofit organization that sporadically crawls
websites on the internet; in 2022 and 2023 it crawled approximately 2-3 billion web pages
each month (AIE p.50). Its data quality is questionable, containing clickbait,
misinformation, propaganda, conspiracy theories, and other low-trustworthiness content;
a Washington Post study found that the 1,000 most common websites in the dataset include
several outlets that rank low on NewsGuard's trustworthiness scale (AIE p.50). Despite
this, variations of Common Crawl are used in most foundation models that disclose their
training sources, including OpenAI's GPT-3 and Google's Gemini, and it is suspected to be
used in undisclosed models as well (AIE p.50).

Google provides a cleaned subset called the Colossal Clean Crawled Corpus (C4). Some
teams apply additional heuristics to filter low-quality data further; for example,
OpenAI trained GPT-2 only on Reddit links that had received at least three upvotes, a
heuristic that screens out unpopular links but does not guarantee propriety or quality,
since Reddit itself is not a byword for good taste (AIE p.50). Common Crawl is also
heavily skewed toward English (45.88%) over other languages (AIE p.50).

## Key figures
- Approximately 2-3 billion web pages crawled per month in 2022 and 2023 (AIE p.50)
- English makes up 45.88% of the dataset (AIE p.50)
- OpenAI used only Reddit links with at least three upvotes to train GPT-2 (AIE p.50)

## Related
- [[training-data-curation]]  (example-of: illustrates the 'use what we have, not what we want' problem in sourcing training data)
- [[low-resource-languages]]  (boundary: Common Crawl's skew toward English leaves low-resource languages underrepresented)
- [[gpt-4]]  (see-also: GPT-3 and other OpenAI models have used Common Crawl variants; contrast in generation and disclosure)

## Provenance
- [[sources/ch02-training-data]]
