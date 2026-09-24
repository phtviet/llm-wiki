---
type: concept
sources: [ch02-multilingual-models]
---
# Common Crawl

Common Crawl is a popular dataset used for training LLMs, compiled by crawling the internet. It is heavily skewed toward English: English accounts for almost half of the data (45.88%), making it roughly eight times more prevalent than the second-most common language, Russian (5.97%) (Lai et al., 2023) (AIE p.51). A language's share of Common Crawl relative to its share of world population indicates how under- or over-represented it is: a ratio near 1 would mean proportional representation, but languages like Punjabi, Swahili, and Urdu have ratios above 100, meaning they are drastically under-represented, while English's ratio is 0.40, indicating over-representation (AIE p.52).

Languages with limited availability as training data -- typically languages falling outside the most-common list -- are considered [[low-resource-languages]] (AIE p.51).

## Key figures
- English: 45.8786% of Common Crawl, 1,452M speakers (18.15% of world population) (AIE p.51-52)
- Russian: 5.9692% of Common Crawl, the second most common language (AIE p.51)
- Punjabi: 113M speakers, 1.41% of world population, only 0.0061% of Common Crawl, world:CC ratio 231.56 (AIE p.52)
- Swahili: world:CC ratio 115.26; Urdu: 105.38; Kannada: 65.57; Telugu: 64.89; Gujarati: 61.51; Marathi: 58.10; Bengali: 36.56 (AIE p.52)
- English world:CC ratio: 0.40, for comparison against under-represented languages (AIE p.52)

## Examples
- [[low-resource-languages]]  (languages under-represented in Common Crawl)

## Related
- [[low-resource-languages]]  (prerequisite: Common Crawl's skew toward English is the basis for defining which languages count as low-resource)
- [[multilingual-performance-gap]]  (prerequisite: under-representation in Common Crawl is cited as a major cause of the performance gap)
- [[tokenization]]  (see-also: tokenization efficiency compounds the disadvantage already created by data under-representation)

## Provenance
- [[sources/ch02-multilingual-models]]
