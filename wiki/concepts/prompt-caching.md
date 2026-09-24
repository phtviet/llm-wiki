---
type: concept
sources: [ch09-inference-service-optimization]
---
# Prompt Caching

Prompt caching (also called context caching or prefix caching) stores overlapping text segments that recur across prompts -- most commonly a system prompt -- so they need to be processed only once instead of with every query. It is useful for queries repeatedly referencing the same long document (a book or codebase) and for long conversations, where earlier messages can be cached and reused when predicting future messages (AIE p.443).

Prompt caching is not free: like the KV cache, the cache can be large and consume memory, and implementing it can require significant engineering effort unless a model API already provides it. Introduced by Gim et al. in November 2023, it has since been rapidly adopted by model API providers (AIE p.443-444).

## Key figures
- A 1,000-token system prompt reused across one million daily API calls saves roughly one billion repetitive input tokens processed per day (AIE p.443)
- Google Gemini gives cached input tokens a 75% discount versus regular input tokens, but charges separately for cache storage ($1.00 per million tokens per hour, as of writing) (AIE p.444)
- Anthropic's prompt caching promises up to 90% cost savings and up to 75% latency reduction (longer cached context yields higher savings) (AIE p.444)
- Chat with a 100,000-token cached book: time to first token drops from 11.5s to 2.4s (-79%), cost down 90% (AIE p.444)
- Many-shot prompting with a 10,000-token prompt: TTFT drops from 1.6s to 1.1s (-31%), cost down 86% (AIE p.444)
- Multi-turn 10-turn conversation with a long system prompt: TTFT drops from ~10s to ~2.5s (-75%), cost down 53% (AIE p.444)

## Examples
None.

## Related
- [[inference-latency]]  (see-also: prompt caching directly reduces time to first token)
- [[context-length]]  (prerequisite: caching is most valuable for prompts with long, reused context)
- [[cost-and-latency]]  (part-of: prompt caching is a concrete technique for improving both cost and latency)

## Provenance
- [[sources/ch09-inference-service-optimization]]
