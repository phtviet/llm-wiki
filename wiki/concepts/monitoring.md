---
type: concept
sources: [ch10-monitoring-and-observability]
---
# Monitoring

Monitoring is the act of tracking a system's external outputs to figure out when something goes wrong inside it. Unlike [[observability]], monitoring makes no assumption that the outputs will actually reveal what went wrong internally (AIE p.466). The goal of monitoring is the same as the goal of [[evaluation]]: to mitigate risks (application failures, security attacks, drifts) and discover opportunities for improvement and cost savings, while keeping a system accountable (AIE p.465).

Metrics themselves are not the goal; their purpose is to signal when something is wrong and to identify opportunities for improvement. Effective metric design starts from the failure modes to be caught -- for example, tracking whether output can be inferred from context to catch hallucination, or tracking token counts and cache hit rate to catch runaway API costs (AIE p.466). Because foundation models produce open-ended output, there are many ways things can go wrong, so which metrics to track is highly application-specific and requires analytical, statistical, and creative judgment (AIE p.466).

When computing metrics, teams can choose spot checks (sampling a subset of data) or exhaustive checks (evaluating every request), with a combination of both giving a balanced strategy. Metrics should be breakable down by axes such as users, releases, prompt/chain versions, prompt/chain types, and time (AIE p.468).

## Key figures
None.

## Related
- [[observability]]  (part-of: monitoring is the tracking act within the broader observability process)
- [[metrics-for-monitoring]]  (part-of: metrics are monitoring's primary output)
- [[evaluation]]  (see-also: shares monitoring's goal of risk mitigation and opportunity discovery; evaluation metrics should translate to monitoring metrics)
- [[logs-and-traces]]  (contrast: metrics are aggregated summaries while logs and traces record individual events)

## Provenance
- [[sources/ch10-monitoring-and-observability]]
