---
type: concept
sources: [ch06-planning]
---
# Control Flow (Agent Plans)

The order in which a plan's actions can be executed is called a control flow (AIE p.291). Sequential control flow executes task B only after task A completes, typically because B depends on A's output (e.g. an SQL query executed only after it's translated from natural language). Parallel control flow executes tasks A and B simultaneously (e.g. retrieving the top 100 best-selling products, then fetching each one's price concurrently). If-statement control flow executes task B or task C depending on the output of a previous step (e.g. checking an earnings report before deciding to buy or sell a stock). For-loop control flow repeats a task until a condition is met (e.g. generating random numbers until a prime is found) (AIE p.291).

In traditional software engineering, control-flow conditions are exact; with AI-powered agents, the AI model itself determines the control flow, and plans with non-sequential control flows are harder both to generate and to translate into executable commands. When evaluating an agent framework, it matters what control flows it supports -- for example, whether it can browse multiple websites in parallel, which can significantly reduce user-perceived latency (AIE p.292).

## Key figures
None.

## Examples
None.

## Related
- [[planning]] (part-of: control flow governs how a generated plan's steps are ordered/executed)
- [[planning-granularity]] (see-also: another structural dimension of plan organization)

## Provenance
- [[sources/ch06-planning]]
