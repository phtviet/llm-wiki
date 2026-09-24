---
type: concept
sources: [ch10-monitoring-and-observability]
---
# Logs and Traces

Metrics are aggregated: they condense events over time into an at-a-glance summary but cannot answer questions like 'has this happened before?' Logs answer that: a log is an append-only record of events, contrasted with metrics' numerical measurements (AIE p.468-469). A typical production debugging process is: metrics flag that something went wrong at a point in time; logs from around that time are examined to find out what happened; the errors found in logs are correlated back to the metrics to confirm the right issue was identified (AIE p.468).

Because it is not known in advance which logs will be needed, the general rule is to log everything: all configurations (model API endpoint, model name, sampling settings such as temperature, top-p, top-k, and stopping condition, and the prompt template), the user query, the final prompt sent to the model, the output, intermediate outputs, tool calls and their outputs, and component start/end/crash events, each tagged with an ID identifying its origin in the system (AIE p.469). For fast detection metrics must compute quickly; for fast response, logs must be readily accessible -- a 15-minute log delay means a 5-minute-old issue cannot be resolved quickly (AIE p.468-469).

Because logging everything grows log volume quickly, many automated log analysis and anomaly detection tools are AI-powered, though manual daily inspection of production data remains useful: Shankar et al. (2024) found developers' sense of what counts as good or bad output changes as they see more data, letting them both improve prompts and improve the evaluation pipeline (AIE p.469).

A trace, unlike a series of disjointed log events, links related events into a complete timeline of a request's execution path through system components -- in an AI application, from the user's query through retrieved documents, tool actions, and the final prompt, to the returned response, including the time and cost of each step. Ideally, each query can be traced step-by-step so that if it fails, the exact failing step (incorrect processing, irrelevant retrieved context, or a wrong generated response) can be pinpointed (AIE p.469-470). LangSmith is shown in the book visualizing a request trace this way (AIE p.470).

## Key figures
None.

## Related
- [[monitoring]]  (contrast: metrics are aggregated summaries while logs and traces are granular event records)
- [[observability]]  (part-of: logs and traces are the detailed instrumentation observability relies on)

## Provenance
- [[sources/ch10-monitoring-and-observability]]
