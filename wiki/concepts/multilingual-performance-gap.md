---
type: concept
sources: [ch02-multilingual-models]
---
# Multilingual Performance Gap

General-purpose foundation models perform much better in English than in other languages, a gap documented across benchmarks, math problem-solving, tokenization efficiency, and even willingness to produce misinformation (AIE p.53-55). On the MMLU benchmark (a suite of 14,000 multiple-choice problems spanning 57 subjects, translated into other languages via Azure AI Translator), [[gpt-4]] performed much better in English than in under-represented languages such as Telugu (OpenAI, 2023) (AIE p.53). The three worst-performing MMLU languages for GPT-4 -- Telugu, Marathi, and Punjabi -- are also among the most under-represented languages in [[common-crawl]], though [[low-resource-languages|under-representation]] is not the only cause: a language's structure and culture can also make it inherently harder to learn (AIE p.53).

On six Project Euler math problems, GPT-4 solved problems in English more than three times as often as in Armenian or Farsi, and failed all six questions in Burmese and Amharic (Yennie Jun) (AIE p.54).

Translating queries into English and back is a common workaround but is not ideal: it requires a model that already understands the under-represented language well enough to translate, and translation can lose information -- for example, Vietnamese pronouns encoding the relationship between speakers collapse into 'I' and 'you' in English (AIE p.54).

Models can also behave differently by language for reasons unrelated to raw capability. NewsGuard found that in April 2023, ChatGPT-3.5 declined to produce misinformation about China for six of seven prompts in English, but produced false claims for all seven prompts in both simplified and traditional Chinese; the cause was unclear, though possibly biases in [[pre-training|pre-training]] or alignment data (AIE p.54-55).

Tokenization efficiency also varies sharply by language. Benchmarking GPT-4 on MASSIVE (one million short texts translated across 52 languages), Yennie Jun found that conveying the same meaning takes far more tokens in some languages: a median of 7 tokens in English versus 32 in Hindi and 72 in Burmese (AIE p.55). Since inference latency and API cost scale with token count, this makes GPT-4 roughly ten times slower and ten times more expensive in Burmese than in English for equivalent content (AIE p.55).

## Key figures
- MMLU: worst-performing languages for GPT-4 are Telugu, Marathi, and Punjabi (AIE p.53)
- Project Euler: GPT-4 solved English math problems over 3x more often than Armenian or Farsi; 0/6 solved in Burmese and Amharic (AIE p.54)
- NewsGuard misinformation test: ChatGPT-3.5 refused 6/7 prompts in English but produced false claims 7/7 times in simplified and traditional Chinese (AIE p.54-55)
- MASSIVE median token length: English 7, Hindi 32, Burmese 72 -- about 10x longer than English (AIE p.55)
- GPT-4 is roughly 10x slower and 10x more costly in Burmese than English for equivalent content, given token-proportional latency and API pricing (AIE p.55)

## Examples
- [[gpt-4]]  (MMLU, Project Euler, and MASSIVE benchmarks)

## Related
- [[common-crawl]]  (prerequisite: English's dominance in Common Crawl underlies the performance gap)
- [[low-resource-languages]]  (part-of: under-representation is the primary but not sole cause of the gap)
- [[tokenization]]  (boundary: tokenization efficiency differences compound the quality gap into a separate cost/latency gap)
- [[gpt-4]]  (example-of: the model benchmarked across MMLU, Project Euler, and MASSIVE in this section)
- [[pre-training]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-multilingual-models]]
