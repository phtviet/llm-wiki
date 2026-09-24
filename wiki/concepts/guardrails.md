---
type: concept
sources: [ch10-step-2-put-in-guardrails]
---
# Guardrails

Guardrails are mechanisms placed around an AI system to mitigate risks and protect both the application and its users. They should be placed wherever the system is exposed to risk, and are broadly categorized into [[input-guardrails]] and [[output-guardrails]] (AIE p.451).

Guardrails come with trade-offs. The main one is reliability versus latency: guardrails such as retries and multi-layered checks reduce failure rates but add extra API calls and waiting time, and some teams choose to skip guardrails entirely because of the latency cost (AIE p.454). Guardrails can be implemented at multiple levels: by model providers (who must balance safety against flexibility/usability), and by application developers using off-the-shelf solutions or custom techniques (AIE p.455). Whether guardrails are needed also depends on deployment mode: third-party APIs typically bundle guardrails out of the box, reducing what a developer must add, while self-hosting removes the need for many input guardrails since data never leaves the organization but shifts the burden of output guardrails onto the developer (AIE p.454-455).

Output guardrails are also harder to apply cleanly under streaming completion, since partial responses are shown to users before the full response can be evaluated, risking unsafe content being streamed before it can be blocked (AIE p.454).

## Key figures
None.

## Examples
- [[input-guardrails]]
- [[output-guardrails]]

## Related
- [[input-guardrails]]  (part-of: one of the two guardrail categories, protecting against leaked private data and bad prompts)
- [[output-guardrails]]  (part-of: the other guardrail category, catching and handling failed model outputs)
- [[prompt-attacks]]  (prerequisite: understanding prompt-hacking techniques motivates why input guardrails are needed)
- [[violation-rate-and-false-refusal-rate]]  (see-also: security guardrails must be tracked against over-blocking legitimate requests, the same trade-off guardrails face generally)
- [[model-gateway]]  (part-of: some model gateways bundle guardrail functionality)

## Provenance
- [[sources/ch10-step-2-put-in-guardrails]]
