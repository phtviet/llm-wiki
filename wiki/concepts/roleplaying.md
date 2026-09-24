---
type: concept
sources: [ch04-instruction-following-capability]
---
# Roleplaying

Roleplaying asks a model to assume a fictional character or persona. It serves two purposes: roleplaying a character for users to interact with (entertainment, gaming, interactive storytelling), and roleplaying as a [[prompt-engineering]] technique to improve output quality (AIE p.175). LMSYS's analysis of one million conversations from Chatbot Arena and the Vicuna demo (Zheng et al., 2023) found roleplaying to be the eighth most common use case, and it is especially important for AI-powered game NPCs, AI companions, and writing assistants (AIE p.175).

Roleplaying capability is hard to evaluate automatically. Benchmarks include RoleLLM (Wang et al., 2023), which scores emulation of a persona using both similarity scores against expected outputs and AI judges, and CharacterEval (Tu et al., 2024), which uses human annotators and a trained [[reward-model]] to score roleplaying aspects on a five-point scale (AIE p.176). Evaluation should cover both style (does the output match the persona's distinctive speaking style) and knowledge (is the output consistent with what the persona would know -- including 'negative knowledge', i.e. not revealing things the persona wouldn't know, which matters for avoiding NPC spoilers) (AIE p.176). Where a role has a distinctive trait (e.g. speaking sparingly), simple heuristics can supplement AI-judge evaluation; otherwise AI-as-a-judge is the most common automatic approach, with judge prompts written per-role (AIE p.176).

## Key figures
- Eighth most common use case among LMSYS's one million analyzed conversations (AIE p.175)

## Examples
- None (RoleLLM and CharacterEval are cited as benchmarks, not developed as standalone entities in this section).

## Related
- [[instruction-following-capability]] (example-of: roleplaying is one of the most common real-world instruction types)
- [[ai-as-a-judge]] (example-of: the most common automatic evaluation approach for roleplaying, with per-role judge prompts)
- [[lmsys-chatbot-arena]] (see-also: source of the one-million-conversation analysis showing roleplaying's prevalence)
- [[prompt-engineering]]  (see-also: mentioned in this page's text)
- [[reward-model]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch04-instruction-following-capability]]
