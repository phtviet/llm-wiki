---
type: concept
sources: [ch03-limitations-of-ai-as-a-judge]
---
# Inconsistency

Model producing very different responses for the same or slightly different prompts, and mitigations for it. Because AI judges are themselves probabilistic AI applications, they inherit this problem directly: the same judge, on the same input, can output different scores if prompted differently, and can even output different scores on repeated runs with the identical prompt. This inconsistency makes AI-judge evaluation results hard to reproduce or trust (AIE p.141).

Including evaluation examples in the judge's prompt is one mitigation: Zheng et al. (2023) found this raised GPT-4's consistency from 65% to 77.5%. However, high consistency does not imply high accuracy -- a judge can consistently make the same mistake -- and longer prompts from added examples increase inference cost; in Zheng et al.'s experiment, adding more examples quadrupled GPT-4 spending (AIE p.141).

## Key figures
- Including evaluation examples in the prompt raised GPT-4 judge consistency from 65% to 77.5% (Zheng et al., 2023) (AIE p.141)
- Adding more examples to the judge prompt quadrupled GPT-4 API spending in the same experiment (AIE p.141)

## Related
- [[ai-as-a-judge]]  (boundary: AI judges inherit the general inconsistency problem of probabilistic AI, making their results hard to trust without mitigation)
- [[probabilistic-nature-of-ai]]  (prerequisite: inconsistency is a direct consequence of AI's probabilistic sampling behavior)
- [[ai-judge-bias]]  (see-also: another limitation of AI as a judge, alongside inconsistency)

## Provenance
- [[sources/ch03-limitations-of-ai-as-a-judge]]
