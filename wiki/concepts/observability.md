---
type: concept
sources: [ch10-monitoring-and-observability]
---
# Observability

Observability is the whole process of instrumenting, tracking, and debugging a system so that its internal state can be inferred from its external outputs. It makes a stronger assumption than [[monitoring]]: that when something goes wrong, the answer can be found by examining logs and metrics alone, without shipping new code (AIE p.466). Observability should be integral to a product's design rather than an afterthought, and matters more as a product grows more complex (AIE p.465).

The term rose to prominence in the industry since the mid-2010s as a replacement for 'monitoring.' In this book, 'monitoring' refers to the act of tracking a system's information, while 'observability' refers to the broader process of instrumenting, tracking, and debugging (AIE p.466).

Three DevOps-derived metrics evaluate the quality of a system's observability: MTTD (mean time to detection), MTTR (mean time to response), and CFR (change failure rate, the percentage of deployments requiring fixes or rollbacks) (AIE p.465). Evaluation and monitoring should work closely together: evaluation metrics should translate to monitoring metrics, and issues found in monitoring should feed back into the evaluation pipeline (AIE p.465).

## Key figures
None.

## Related
- [[monitoring]]  (part-of: observability encompasses the act of monitoring plus instrumenting and debugging)
- [[metrics-for-monitoring]]  (prerequisite: metrics are the raw signal observability tools track and analyze)
- [[logs-and-traces]]  (part-of: logs and traces are the detailed records observability uses to explain what metrics only flag)
- [[drift-detection]]  (example-of: a category of problem observability aims to surface)
- [[evaluation]]  (see-also: shares the same risk-mitigation goal and feeds signals to and from monitoring)

## Provenance
- [[sources/ch10-monitoring-and-observability]]
