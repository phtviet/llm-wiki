---
type: concept
sources: [ch06-planning]
---
# Foundation Model vs. Reinforcement Learning Planners

The agent is a core concept in reinforcement learning (RL) too, defined there as an intelligent agent taking actions in a dynamic environment to maximize cumulative reward. RL agents and foundation-model (FM) agents are similar in being characterized by their environment and possible actions; they differ chiefly in how their planners are built. In an RL agent, the planner is trained by an RL algorithm, which can require substantial time and resources. In an FM agent, the model itself is the planner, and it can be prompted or finetuned to improve planning, generally requiring less time and fewer resources (AIE p.285). Nothing prevents an FM agent from incorporating RL algorithms to improve performance, and the book suggests FM agents and RL agents may merge over time (AIE p.285).

## Key figures
None.

## Related
- [[planning]] (part-of: contrasts how the planner component is built across the two agent paradigms)
- [[agent]] (prerequisite: both RL agents and FM agents are defined by environment plus action set)

## Provenance
- [[sources/ch06-planning]]
