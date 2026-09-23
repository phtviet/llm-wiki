---
type: concept
sources: [ch02-multilingual-models]
---
# Multilingual Models

General-purpose foundation models are trained predominantly on English-dominated web data, and as a result perform worse on other languages, especially low-resource ones. English accounts for almost half (45.8786%) of the [[common-crawl]] dataset, making it roughly eight times more prevalent than the second-most common language, Russian (5.9692%) (Lai et al., 2023) (AIE p.51). Languages with limited representation in training data are called low-resource languages (AIE p.51).

Under-representation is a major but not the only cause of degraded performance: a language's structure and the culture it embodies can also make it intrinsically harder for a model to learn (AIE p.54). On the MMLU benchmark (14,000 multiple-choice problems spanning 57 subjects), GPT-4 performed much better in English than in under-represented languages like Telugu; the three worst-performing MMLU languages for GPT-4 -- Telugu, Marathi, and Punjabi -- are also among the most under-represented in Common Crawl (OpenAI, 2023) (AIE p.53-54). Testing on Project Euler math problems, GPT-4 solved English problems more than three times as often as Armenian or Farsi, and failed all six questions in Burmese and Amharic (AIE p.54).

Translating queries into English and back is a common but imperfect workaround: it requires a model that already understands the under-represented language well enough to translate, and translation can cause information loss -- for example, Vietnamese pronouns encoding speaker relationships collapse into generic "I" and "you" in English (AIE p.54). Models can also behave unexpectedly across languages: NewsGuard found ChatGPT-3.5 far more willing to produce misinformation in Chinese than in English (AIE p.54-55).

Non-English languages can also be slower and more expensive to serve, since inference cost and latency scale with token count and tokenization efficiency varies by language (AIE p.55). To address underperformance, some models are trained to focus on non-English languages, such as ChatGLM, YAYI, and Llama-Chinese for Chinese, CroissantLLM for French, PhoGPT for Vietnamese, and Jais for Arabic (AIE p.55).

## Key figures
- English is 45.8786% of Common Crawl vs. 5.9692% for Russian, the second-most common language (Lai et al., 2023) (AIE p.51)
- Median token length for the same content in the MASSIVE dataset: 7 for English, 32 for Hindi, 72 for Burmese -- about ten times longer than English (AIE p.55)
- GPT-4 solved Project Euler math problems in English more than 3x as often as in Armenian or Farsi, and failed all six questions in Burmese and Amharic (AIE p.54)
- NewsGuard: ChatGPT-3.5 declined to produce misinformation in English 6 of 7 times, but produced it in simplified and traditional Chinese all 7 times (AIE p.54-55)

## Examples
- [[common-crawl]]  (primary training-data source whose language skew drives the disparity)

## Related
- [[common-crawl]]  (prerequisite: Common Crawl's language distribution is the main driver of multilingual performance gaps)
- [[dataset-engineering]]  (part-of: curating language-specific data is a form of dataset curation for specific needs)
- [[domain-specific-models]]  (contrast: language specialization vs. domain specialization as two axes of curated, specialized foundation models)
- [[foundation-model]]  (boundary: general-purpose foundation models underperform on non-English languages despite broad training)

## Provenance
- [[sources/ch02-multilingual-models]]
