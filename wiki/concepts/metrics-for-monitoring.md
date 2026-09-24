---
type: concept
sources: [ch10-monitoring-and-observability]
---
# Metrics for Monitoring

Metrics for monitoring an AI application span format failures, open-ended generation quality, safety, [[user-feedback]], per-component quality, latency, and cost. Format failures (e.g. invalid JSON) are the easiest to track since they are easy to notice and verify, including whether an invalid output can be easily fixed (AIE p.467). For open-ended generations, relevant metrics include [[factual-consistency]], conciseness, creativity, and positivity, many computable using [[ai-as-a-judge|AI judges]] (AIE p.467).

For safety, teams can track toxicity-related metrics, detect private/sensitive information in inputs and outputs, and track how often [[guardrails]] trigger, the system refuses to answer, or abnormal queries appear (which may reveal edge cases or [[prompt-attacks]]) (AIE p.467).

Model quality can also be inferred from user natural-language feedback and conversational signals: how often users stop a generation halfway, average turns per conversation, average input/output token counts, and the model's output token distribution over time (AIE p.467-468). Length-related metrics also matter for latency and cost, since longer contexts and responses raise both (AIE p.468).

Per-component metrics apply to each part of a pipeline: a RAG application's retrieval quality is evaluated with context relevance and context precision, and a [[vector-database]] is evaluated by storage needed and query time (AIE p.468). Teams should measure how metrics correlate with each other and with business north-star metrics like DAU, session duration, or subscriptions, since strongly or weakly correlated metrics both suggest what to optimize (AIE p.468).

Latency metrics -- time to first token (TTFT), time per output token (TPOT), and total latency -- should be tracked per user to observe scaling behavior (AIE p.468). Cost metrics include number of queries, input/output token volume, tokens per second (TPS), and requests per second when an API enforces rate limits (AIE p.469).

## Key figures
None.

## Examples
- [[inference-latency]]  (TTFT and TPOT as shared latency vocabulary)

## Related
- [[monitoring]]  (part-of: metrics are monitoring's core signal)
- [[ai-as-a-judge]]  (prerequisite: many open-ended quality metrics are computed using AI judges)
- [[retrieval-quality-metrics]]  (example-of: context relevance and precision as component-level monitoring metrics for RAG)
- [[inference-latency]]  (see-also: shares TTFT/TPOT vocabulary between serving-time and monitoring-time measurement)
- [[natural-language-feedback]]  (see-also: user conversational signals double as monitoring metrics)
- [[factual-consistency]]  (see-also: mentioned in this page's text)
- [[vector-database]]  (see-also: mentioned in this page's text)
- [[prompt-attacks]]  (see-also: mentioned in this page's text)
- [[user-feedback]]  (see-also: mentioned in this page's text)
- [[guardrails]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch10-monitoring-and-observability]]
