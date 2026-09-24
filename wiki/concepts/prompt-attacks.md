---
type: concept
sources: [ch05-defensive-prompt-engineering]
---
# Prompt Attacks

Once an AI application is made available, it can be exploited by malicious attackers as well as used by intended users. There are three main types of prompt attacks application developers must defend against: [[prompt-extraction]], [[jailbreaking-and-prompt-injection]], and [[information-extraction]] (AIE p.235).

Prompt attacks pose multiple risks, some more devastating than others, including remote code or tool execution, data leaks, social harms, misinformation, service interruption and subversion, and brand risk; see [[prompt-attack-risks]] for detail (AIE p.235-236). Defenses are mounted at model, prompt, and system levels.

## Key figures
None.

## Examples
- [[prompt-extraction]]
- [[jailbreaking-and-prompt-injection]]
- [[information-extraction]]

## Related
- [[prompt-attack-risks]]  (part-of: risks motivating the defenses)
- [[violation-rate-and-false-refusal-rate]]  (evaluates: paired metrics measuring successful attacks vs. over-cautious refusals)
- [[instruction-hierarchy]]  (prerequisite: instruction hierarchy is a model-level defense against prompt injection specifically)
- [[prompt-engineering]]  (part-of: defensive prompt engineering is a protective application of prompt engineering)

## Provenance
- [[sources/ch05-defensive-prompt-engineering]]
