---
type: concept
sources: [ch06-agent-failure-modes-and-evaluation]
---
# Agent Failure Modes

Evaluating an agent means identifying its failure modes and measuring how often each occurs. The more complex a task an agent performs, the more possible failure points there are. Beyond the failure modes common to all AI applications, agents have unique failures caused by planning, tool execution, and efficiency (AIE p.298).

The book illustrates these failure modes with a simple benchmark on its GitHub repository, alongside external agent benchmarks and leaderboards such as the Berkeley Function Calling Leaderboard, the AgentOps evaluation harness, and the TravelPlanner benchmark (AIE p.298). The three categories are developed as distinct concepts: [[planning-failures]], [[tool-failures]], and [[agent-efficiency]].

## Key figures
None.

## Examples
- [[planning-failures]]  (invalid tool, invalid parameters, goal failure, reflection errors)
- [[tool-failures]]  (wrong tool output, translation errors, missing tools)
- [[agent-efficiency]]  (steps, cost, and time per task)

## Related
- [[evaluation]]  (part-of: agent failure-mode analysis is a specialized form of evaluation applied to agentic systems)
- [[planning-failures]]  (part-of: one of the three failure-mode categories)
- [[tool-failures]]  (part-of: one of the three failure-mode categories)
- [[agent-efficiency]]  (part-of: one of the three failure-mode categories)

## Provenance
- [[sources/ch06-agent-failure-modes-and-evaluation]]
