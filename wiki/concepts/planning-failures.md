---
type: concept
sources: [ch06-agent-failure-modes-and-evaluation]
---
# Planning Failures

Planning is hard and can fail in many ways. The most common mode is tool use failure, where the agent's generated plan contains one of three errors: an **invalid tool** (e.g. calling `bing_search` when it isn't in the agent's [[tool-inventory]]), a **valid tool with invalid parameters** (e.g. calling `lbs_to_kg` with two parameters when it takes only one), or a **valid tool with incorrect parameter values** (e.g. passing 100 for `lbs` when it should be 120) (AIE p.298).

A second mode is **goal failure**: the agent fails to achieve the goal, either because the plan doesn't solve the task or because it solves the task while violating constraints (illustrated by planning a trip to the wrong city, or one that blows the budget). Time is a commonly overlooked constraint: an agent that finishes a grant proposal after the deadline isn't useful even if the output is otherwise correct (AIE p.298-299).

A third mode is caused by errors in **reflection**: the agent is convinced it has accomplished a task when it hasn't -- for example, claiming it assigned 50 people to 30 hotel rooms after assigning only 40 (AIE p.299).

To evaluate planning failures, the book proposes building a planning dataset of (task, tool inventory) pairs, generating K plans per task with the agent, and computing metrics: the fraction of generated plans that are valid, the average number of plans needed to get one valid plan, the fraction of tool calls that are valid, and the rates of invalid-tool calls, invalid-parameter calls, and incorrect-parameter-value calls. Analyzing which task types and tools the agent fails on most can point to fixes: better prompting, more examples, finetuning, or swapping out a hard-to-use tool (AIE p.299).

## Key figures
None.

## Examples
- lbs_to_kg parameter errors (invalid-parameter and incorrect-value illustrations)
- San Francisco-to-Hanoi trip planning (goal failure via wrong destination or budget overrun)
- 50-people/30-rooms assignment (reflection error)

## Related
- [[agent-failure-modes]]  (part-of: one of the three failure-mode categories)
- [[tool-failures]]  (contrast: planning failures occur in the generated plan itself vs. tool failures occur when a correctly-planned tool call returns wrong output)
- [[agent-efficiency]]  (see-also: a plan can be valid yet inefficient)
- [[tool-inventory]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch06-agent-failure-modes-and-evaluation]]
