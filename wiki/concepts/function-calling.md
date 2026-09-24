---
type: concept
sources: [ch06-planning]
---
# Function Calling

Function calling is the mechanism by which an agent invokes tools -- since a tool is a function, invoking it is called function calling. Many model providers offer tool use for their models, effectively turning them into agents (AIE p.288).

Function calling generally works in two steps. First, create a tool inventory: declare all tools the model might use, each described by its execution entry point (function name), its parameters, and documentation of what it does and what parameters it needs. Second, specify what tools the agent can use for a given query; many APIs let a caller restrict the tool list per query and further control usage via settings: `required` (the model must use at least one tool), `none` (the model must not use a tool), and `auto` (the model decides) (AIE p.288).

Given a query, the agent generates which tools to use and their parameters; some function-calling APIs guarantee only valid functions are generated, though they cannot guarantee correct parameter values (AIE p.288-289). The book recommends always asking the system to report the parameter values used for each function call and inspecting them for correctness (AIE p.289).

## Key figures
None.

## Examples
- [[kitty-vogue-sql-agent-example]] (lbs_to_kg_tool example call with parameter 40)

## Related
- [[agent]] (prerequisite: function calling is how an agent's tools are actually invoked)
- [[plan-generation]] (part-of: a generated plan's steps are executed via function calling)
- [[tool-selection]] (prerequisite: a tool inventory must be chosen before function calling can use it)
- [[tool-failures]] (boundary: agent failures where the right tool is called but with wrong or hallucinated parameters)

## Provenance
- [[sources/ch06-planning]]
