---
type: concept
sources: [ch06-planning]
---
# Reflection and Error Correction

Reflection and error correction are two mechanisms that go hand in hand: reflection generates insights that help uncover errors, which are then corrected. Even the best plans need constant evaluation and adjustment to maximize success, and while reflection isn't strictly necessary for an agent to operate, it is necessary for an agent to succeed (AIE p.292). Reflection can occur at several points: after receiving a user query (is the request feasible?), after initial [[plan-generation]] (does the plan make sense?), after each execution step (is it on the right track?), and after the whole plan executes (was the task accomplished?) (AIE p.292).

Reflection can be performed by the same agent via self-critique prompts, or by a separate component such as a specialized scorer model that outputs a concrete score for each outcome (AIE p.293). [[react-framework]] (Yao et al., 2022) interleaves reasoning and action: at each step the agent explains its thinking (planning), takes an action, then analyzes the observation (reflection), in a Thought/Act/Observation loop, until it decides the task is finished (AIE p.293). Reflection can also be run in a multi-agent setup, with one agent planning/acting and another evaluating outcomes. [[reflexion-framework]] (Shinn et al., 2023) separates reflection into an evaluator module (scores the outcome) and a self-reflection module (analyzes what went wrong), after which the agent proposes a new 'trajectory' (plan) (AIE p.294).

Compared to plan generation, reflection is relatively easy to implement and can bring surprisingly good performance gains, but at a cost: thoughts, observations, and sometimes actions consume many tokens, increasing cost and user-perceived latency, especially for tasks with many intermediate steps, and heavy example-laden prompts (used by both ReAct and Reflexion to enforce format) further increase input-token cost and reduce available context (AIE p.294).

## Key figures
None.

## Examples
- [[react-framework]] (Thought/Act/Observation loop; HotpotQA example)
- [[reflexion-framework]] (evaluator + self-reflection modules, proposes new trajectories)

## Related
- [[planning]] (part-of: the second and fourth of planning's four processes)
- [[self-critique-prompting]] (example-of: reflection performed by the same agent via self-critique prompts)
- [[agent]] (prerequisite: reflection is a capability layered onto an agent's plan/execution loop)
- [[plan-generation]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch06-planning]]
