---
type: concept
sources: [ch05-defenses-against-prompt-attacks]
---
# Violation Rate and False Refusal Rate

Two metrics evaluate a system's robustness against prompt attacks. The violation rate measures the percentage of successful attacks out of all attack attempts. The false refusal rate measures how often a model refuses a query when it could have answered it safely. Both metrics are necessary together: a system that refuses all requests could achieve a violation rate of zero while being useless to users, so security must be balanced against over-caution (AIE p.248).

## Key figures
None.

## Related
- [[prompt-attacks]]  (part-of: the pair of metrics used to evaluate a system's robustness against prompt attacks)
- [[evaluation]]  (example-of: a domain-specific pair of evaluation metrics, applied to security rather than general quality)

## Provenance
- [[sources/ch05-defenses-against-prompt-attacks]]
