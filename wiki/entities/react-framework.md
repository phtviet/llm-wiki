---
type: entity
sources: [ch06-planning]
---
# ReAct

ReAct (Yao et al., 2022) is the framework that first proposed interleaving reasoning and action for agents, a pattern that became common. Yao et al. use 'reasoning' to cover both planning and reflection: at each step the agent explains its thinking (planning), takes an action, then analyzes the observation (reflection), continuing until the agent judges the task finished. The agent is typically prompted, using examples, to output in a Thought/Act/Observation format (AIE p.293). The book illustrates a ReAct agent answering a question from [[hotpotqa]], a benchmark for multi-hop question answering (AIE p.293).

## Key figures
None.

## Related
- [[reflection-and-error-correction]] (example-of: canonical interleaved reasoning-and-action framework)
- [[reflexion-framework]] (contrast: Reflexion separates evaluation and self-reflection into distinct modules, building on ReAct-style interleaving)

## Provenance
- [[sources/ch06-planning]]
