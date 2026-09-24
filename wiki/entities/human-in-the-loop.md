---
type: concept
sources: [ch10-step-2-put-in-guardrails]
---
# Human-in-the-Loop

Involving humans in AI decision-making rather than relying on the model alone, including Microsoft's Crawl-Walk-Run automation framework for gradually increasing AI autonomy.

In production applications, human-in-the-loop is also used as a guardrail escalation policy: tricky or risky requests are transferred from the model to human operators. Teams have implemented this by transferring a conversation when a specialized sentiment-analysis model detects anger in a user's messages, or after a conversation reaches a certain number of turns, to prevent the user from being stuck in an unproductive loop (AIE p.453).

## Key figures
None.

## Examples
None.

## Related
- [[output-guardrails]]  (example-of: human escalation is a policy for handling failure modes that output guardrails specify)
- [[guardrails]]  (part-of: human fallback is one mitigation strategy within the guardrails layer)

## Provenance
- [[sources/ch10-step-2-put-in-guardrails]]
