---
type: concept
sources: [ch06-planning]
---
# Planning

Planning is the process by which a [[foundation-model]] agent decomposes a task -- defined by its goal and constraints -- into a plan: a roadmap of steps needed to accomplish it (AIE p.281). Given a task, many decompositions are possible, but not all succeed, and among correct ones some are more efficient than others; an intelligent agent should prefer the more efficient decomposition (AIE p.282).

Planning can be coupled with execution in a single prompt (e.g. a chain-of-thought prompt that both plans and executes), but this risks an agent running a long, useless plan for hours before the failure is noticed. To avoid fruitless execution, planning should be decoupled from execution: a plan is generated, then validated (via heuristics such as rejecting invalid actions or overly long plans, or via an AI judge), and only a validated plan is executed. Plans can also be generated in parallel and the most promising one selected, trading extra cost for lower latency (AIE p.282).

Solving a task typically involves four processes: plan generation (task decomposition), reflection and error correction on the plan, execution (often via function calling), and a further round of reflection and error correction on the outcome. Reflection is not mandatory but significantly boosts performance (AIE p.283-284). Planning also requires understanding the intent behind a task, often via an [[intent-classification]] step that can also flag out-of-scope queries as IRRELEVANT so the agent doesn't waste compute on impossible requests (AIE p.283). Humans can be inserted at any stage -- providing a high-level plan, validating a plan, or executing risky steps such as database updates -- so the level of automation per action should be explicitly defined (AIE p.284).

Whether foundation models -- particularly autoregressive ones -- can truly plan is disputed. Yann LeCun states autoregressive LLMs can't plan; Kambhampati (2023) argues LLMs extract general planning knowledge but don't produce reliably executable plans (AIE p.284). Planning is fundamentally a search problem: searching among paths to a goal, predicting each path's outcome, and picking the most promising, often requiring backtracking. Some argue autoregressive models can't backtrack, but a model can still revise or restart a path after determining it's unpromising, effectively backtracking (AIE p.285). Hao et al. (2023) argue an LLM can predict the outcome of each action, given its world knowledge, and use that prediction to generate coherent plans -- addressing the concern that a model needs to know an action's outcome state, not just the action sequence, to plan well (AIE p.285).

## Key figures
None.

## Examples
- [[kitty-vogue-sql-agent-example]] (plan-generation prompt over five actions)

## Related
- [[plan-generation]] (part-of: the first stage of planning, producing the roadmap itself)
- [[reflection-and-error-correction]] (part-of: the evaluative stage that follows plan generation and execution)
- [[agent]] (prerequisite: planning is the core responsibility of the model at the heart of an agent)
- [[chain-of-thought-prompting]] (contrast: coupling planning and execution in one prompt vs. decoupling them for validation)
- [[function-calling]] (prerequisite: executing a validated plan's external-tool steps requires function calling)
- [[planning-granularity]] (part-of: how detailed or high-level a generated plan is)
- [[control-flow]] (part-of: the order in which a plan's actions are executed)
- [[reinforcement-learning-versus-foundation-model-planners]] (contrast: how RL agents and FM agents differ in how their planners are built)
- [[planning-failures]] (see-also: agent evaluation category covering planning-specific errors)
- [[foundation-model]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch06-planning]]
