---
type: concept
sources: [ch10-step-2-put-in-guardrails]
---
# Output Guardrails

Output guardrails serve two functions: catching output failures, and specifying the policy for handling each failure mode (AIE p.452). The simplest failure to detect is an empty response where one is not expected (AIE p.453).

Failures fall into two categories. Quality failures include malformatted responses that don't follow the expected output format (e.g., invalid JSON), factually inconsistent (hallucinated) responses, and generally bad responses such as a poorly written essay. Security failures include toxic responses (racist or sexual content, or content describing illegal activity), responses containing private or sensitive information, responses that trigger remote tool or code execution, and brand-risk responses that mischaracterize the company or its competitors (AIE p.453). For security failures it is important to track not just the failure rate but also the false refusal rate, since an overly cautious system can block legitimate requests and frustrate users (AIE p.453); see [[violation-rate-and-false-refusal-rate]].

Many failures can be mitigated with retry logic: since model outputs are probabilistic, resending a failed query (e.g., one that came back empty or malformatted) can yield a valid response on a later attempt (AIE p.453). Sequential retries double user-perceived latency; an alternative is to send the same query to the model twice in parallel and pick the better of the two responses, trading redundant API calls for lower latency (AIE p.453-454).

For tricky requests, teams commonly fall back to human operators — for example, transferring a conversation to a human when a sentiment-analysis model detects anger, or after a set number of turns to prevent the user getting stuck in a loop (AIE p.453). See [[human-in-the-loop]].

Output guardrails are difficult to apply under streaming completion: because tokens are shown to the user as they are generated rather than after the full response is checked, unsafe content can reach the user before the guardrail has evaluated the complete response (AIE p.454).

## Key figures
None.

## Examples
None.

## Related
- [[guardrails]]  (part-of: output guardrails are one of the two guardrail categories)
- [[input-guardrails]]  (contrast: checks model output vs. guards data going into the model)
- [[violation-rate-and-false-refusal-rate]]  (see-also: security-failure tracking must be paired with false-refusal tracking to avoid over-blocking)
- [[human-in-the-loop]]  (example-of: escalating tricky or flagged conversations to human operators is a guardrail policy)
- [[hallucination]]  (example-of: factually inconsistent responses are one quality failure output guardrails must catch)

## Provenance
- [[sources/ch10-step-2-put-in-guardrails]]
