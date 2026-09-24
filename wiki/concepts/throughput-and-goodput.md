---
type: concept
sources: [ch09-inference-performance-metrics]
---
# Throughput and Goodput

Throughput measures the number of output tokens per second an [[inference-service]] can generate across all users and requests, typically reported in tokens/s (TPS); tokens/s/user is used to evaluate how the system scales with more users (AIE p.414). Because prefilling (processing input tokens) and decoding (generating output tokens) have different computational bottlenecks and are often decoupled in modern inference servers, input and output throughput are usually counted separately, and 'throughput' without a modifier usually refers to output tokens (AIE p.414). Throughput can also be measured in completed requests per unit time -- requests per second (RPS) or, since a foundation-model request can take seconds, the coarser completed requests per minute (RPM) (AIE p.414).

Throughput is directly linked to compute cost: higher throughput generally means lower cost per token, and total cost per request is the sum of prefilling and decoding costs (AIE p.414-415). What counts as good throughput depends on the model, hardware, and workload -- smaller models and higher-end chips give higher throughput, and consistent-length workloads are easier to optimize than variable-length ones. Direct throughput comparisons across models are only approximate because token count depends on each model's tokenizer, so cost per request is a better cross-model comparison metric (AIE p.415).

AI applications face a latency/throughput trade-off: techniques like batching raise throughput but can increase TTFT and TPOT. Because optimizing purely for throughput and cost can produce a bad user experience, some teams instead track goodput, a metric adapted from networking: the number of requests per second that satisfy a defined service-level objective (SLO), e.g. a maximum TTFT and TPOT (AIE p.415).

## Key figures
- Example: $2/h compute at 100 tokens/s throughput costs about $5.556 per 1M output tokens; at 200 output tokens/request, decoding 1K requests costs about $1.11 (AIE p.414)
- Example: prefilling 100 requests/minute on the same $2/h hardware costs about $0.33 per 1K requests; combined with decoding, total cost for 1K requests is $1.11 + $0.33 = $1.44 (AIE p.414)
- LinkedIn reports it is not uncommon to double or triple throughput by sacrificing TTFT and TPOT (AIE p.415)
- Goodput example: 100 completed requests/minute of which only 30 satisfy the SLO gives a goodput of 30 requests/minute (AIE p.415)

## Examples
- None.

## Related
- [[inference-latency]]  (contrast: latency/throughput trade-off -- batching improves throughput but can worsen TTFT/TPOT)
- [[utilization-metrics]]  (see-also: throughput and MFU/MBU are linearly related, so throughput sometimes stands in for utilization)
- [[quantization]]  (see-also: reducing bytes per parameter lowers memory-bandwidth demand, raising achievable throughput)
- [[inference-service]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch09-inference-performance-metrics]]
