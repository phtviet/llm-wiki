---
type: concept
sources: [ch04-cost-and-latency]
---
# Model Selection Criteria Table

The book presents a worked example (Table 4-3) of criteria used to select a model for a fictional application, pairing each criterion with a metric, a benchmark source, a hard requirement, and an ideal target. The criteria are: cost per output token, scale (tokens per minute, TPM), latency (time to first token and time per total query, both at P90), overall model quality (Elo score from [[lmsys-chatbot-arena]]), code generation capability ([[pass-at-k]] on [[humaneval]]), and factual consistency (an internal GPT metric on an internal hallucination dataset). The scale row is called out as especially important when evaluating model APIs, since the chosen API service must be able to support the application's required throughput (AIE p.177-178).

## Key figures
- Cost per output token: hard requirement < $30.00 / 1M tokens, ideal < $15.00 / 1M tokens (AIE p.178)
- Scale: hard requirement and ideal both > 1M TPM (AIE p.178)
- Time to first token (P90): hard requirement < 200ms, ideal < 100ms (AIE p.178)
- Time per total query (P90): hard requirement < 1 minute, ideal < 30s (AIE p.178)
- Overall model quality (Elo score, Chatbot Arena ranking): hard requirement > 1200, ideal > 1250 (AIE p.178)
- Code generation capability (pass@1, HumanEval): hard requirement > 90%, ideal > 95% (AIE p.179)
- Factual consistency (internal GPT metric, internal hallucination dataset): hard requirement > 0.8, ideal > 0.9 (AIE p.179)

## Examples
- [[cost-and-latency]]  (cost and latency rows of the table)

## Related
- [[cost-and-latency]]  (part-of: cost and latency are two of the criteria in this table)
- [[lmsys-chatbot-arena]]  (example-of: source of the Elo-score quality benchmark used in the table)
- [[humaneval]]  (example-of: benchmark used for the code generation capability criterion)
- [[pass-at-k]]  (example-of: metric used for the code generation capability criterion)

## Provenance
- [[sources/ch04-cost-and-latency]]
