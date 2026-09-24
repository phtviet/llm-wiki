---
type: concept
sources: [ch09-inference-performance-metrics]
---
# Latency (Inference)

Latency measures the time from when a user sends a query until they receive the complete response. From the user's perspective it is the central axis of inference performance, distinct from response quality, which is a property of the model itself rather than the inference service (AIE p.412). For autoregressive generation, especially in streaming mode, overall latency decomposes into time to first token (TTFT) and time per output token (TPOT): total latency equals TTFT + TPOT x (number of output tokens) (AIE p.412-413).

TTFT measures how quickly the first token is generated after a query is sent, corresponding to the duration of the prefill step and depending on input length; expectations vary by application (e.g. near-instantaneous for chatbots, more tolerant for document summarization) (AIE p.412). TPOT measures how quickly each subsequent output token is generated; in streaming mode it should be faster than human reading speed, but need not be much faster (AIE p.412). Related variations time between tokens (TBT, used by LinkedIn) and inter-token latency (ITL, used by NVIDIA) both measure time between output tokens (AIE p.412).

The TTFT and TPOT observed by users can differ from those observed internally by the model, especially for chain-of-thought or agentic queries where intermediate steps are generated but not shown to the user; some teams use 'time to publish' to name the user-visible first-token metric explicitly (AIE p.413). Reducing TTFT at the cost of higher TPOT is possible by shifting compute instances from decoding to prefilling, and vice versa (AIE p.413).

Because latency is a distribution, averages can be misleading -- a single outlier request can inflate the mean far above what most users experience. Latency is therefore better examined via percentiles (p50/median, p90, p95, p99), which also help surface outliers worth investigating (AIE p.413-414).

## Key figures
- A TPOT of about 120 ms/token matches a very fast human reader; roughly 120 ms/token (6-8 tokens/second) is sufficient for most use cases (AIE p.412)
- Example distribution: 10 TTFT values averaging 390 ms due to one 3,000 ms outlier, versus a typical value near 100 ms -- illustrating why averages mislead (AIE p.413-414)

## Examples
- None beyond the worked TTFT-distribution example above.

## Related
- [[throughput-and-goodput]]  (contrast: latency/throughput trade-off -- batching raises throughput but can raise TTFT and TPOT)
- [[model-robustness]]  (see-also: both concern variability of model behavior, though latency variability is a serving-side property, not a model-output property)
- [[quantization]]  (see-also: fewer bytes per parameter reduces memory bandwidth demand, indirectly affecting achievable latency)

## Provenance
- [[sources/ch09-inference-performance-metrics]]
