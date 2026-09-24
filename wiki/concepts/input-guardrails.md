---
type: concept
sources: [ch10-step-2-put-in-guardrails]
---
# Input Guardrails

Input guardrails protect against two risks: leaking private information to external APIs, and executing bad prompts that compromise the system (AIE p.451). Prompt-hacking risks and their defenses are covered separately under [[prompt-attacks]]; this page covers the data-leakage side.

Leaking private information is a risk specific to using external model APIs, since it requires sending data outside the organization. It can happen when an employee pastes a company secret or a user's private information into a prompt sent to a third-party API, when a developer embeds internal policies or data into a system prompt, or when a tool retrieves private information from an internal database and adds it to context (AIE p.451-452). One documented case: a Samsung employee leaked proprietary company information by pasting it into ChatGPT (AIE p.451).

There is no airtight way to eliminate such leaks when using third-party APIs, but they can be mitigated. Tools can automatically detect sensitive data classes defined by the developer, commonly personal information (ID numbers, phone numbers, bank accounts), human faces, and company-specific confidential keywords or phrases; many such tools are themselves AI-based (e.g., recognizing that a string resembles a valid home address) (AIE p.452). When sensitive information is found in a query, the system can either block the query entirely or mask the sensitive portion with a placeholder (e.g., replacing a phone number with '[PHONE NUMBER]'). If the generated response echoes the placeholder, a PII reverse dictionary maps it back to the original value so it can be unmasked before being shown to the user, without ever having sent the real value to the external API (AIE p.452).

## Key figures
None.

## Examples
None.

## Related
- [[guardrails]]  (part-of: input guardrails are one of the two guardrail categories)
- [[output-guardrails]]  (contrast: guards data going into the model vs. checking what comes out)
- [[prompt-attacks]]  (see-also: the other major input risk, bad/malicious prompts, defended against separately)
- [[model-api]]  (boundary: the private-data leakage risk applies specifically to sending data to external model APIs, not to self-hosted models)

## Provenance
- [[sources/ch10-step-2-put-in-guardrails]]
