---
type: concept
sources: [ch05-defensive-prompt-engineering]
---
# Prompt Attack Risks

Prominent risks that prompt attacks pose to applications, ranging from technical compromise to reputational damage (AIE p.235-236):

- Remote code or tool execution -- for applications with access to powerful tools, bad actors can invoke unauthorized code or tool execution, e.g. an attacker getting a model to generate malicious code that compromises the system running it (AIE p.235).
- Data leaks -- extraction of private information about the system or its users (AIE p.235).
- Social harms -- AI models helping attackers gain knowledge or tutorials for dangerous or criminal activities such as making weapons, evading taxes, or exfiltrating personal information (AIE p.236).
- Misinformation -- attackers manipulating models to output misinformation supporting their agenda (AIE p.236).
- Service interruption and subversion -- e.g. granting access to an unauthorized user, giving high scores to bad submissions, wrongly rejecting a loan application, or a malicious instruction causing the model to refuse to answer all questions (AIE p.236).
- Brand risk -- offensive or politically incorrect model outputs next to a company's logo causing a PR crisis, as when Google AI search urged users to eat rocks (2024) and Microsoft's Tay chatbot produced racist comments (2016) (AIE p.236).

## Key figures
None.

## Related
- [[prompt-attacks]]  (part-of: these risks motivate defending against the three prompt-attack types)

## Provenance
- [[sources/ch05-defensive-prompt-engineering]]
