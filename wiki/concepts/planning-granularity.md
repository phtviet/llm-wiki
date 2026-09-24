---
type: concept
sources: [ch06-planning]
---
# Planning Granularity

A plan's roadmap can exist at different levels of granularity -- for example, a quarter-by-quarter plan is higher-level than a month-by-month plan, which is higher-level than a week-to-week plan (AIE p.290). This creates a planning/execution trade-off: a detailed plan is harder to generate but easier to execute, while a higher-level plan is easier to generate but harder to execute. Hierarchical planning circumvents the trade-off: a planner first generates a high-level plan, then the same or a different planner expands each high-level step into a more detailed plan (AIE p.290).

A separate granularity axis is how plan steps are named. Plans can use exact function names (e.g. `get_time()`), which is precise but brittle: if a tool is renamed or the tool inventory changes, prompts and examples -- and any finetuned planner -- must be updated. Plans can instead be expressed in natural language (e.g. 'get current date'), which is more robust to tool-API changes and less prone to hallucination if the underlying model was trained mostly on natural language, at the cost of needing a separate translator to convert each natural-language action into an executable command. Translation, however, is a simpler task than planning and can be done by weaker models with lower hallucination risk (AIE p.290).

## Key figures
None.

## Examples
None.

## Related
- [[planning]] (part-of: granularity is a property of the plan planning produces)
- [[plan-generation]] (boundary: exact-function-name plans are brittle to tool-inventory changes; natural-language plans need a translator)
- [[control-flow]] (see-also: another structural dimension of how a plan is organized)

## Provenance
- [[sources/ch06-planning]]
