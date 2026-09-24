---
type: concept
sources: [ch06-agent-failure-modes-and-evaluation]
---
# Agent Efficiency

An agent might generate a valid plan using the right tools and still be inefficient. The book proposes tracking, on average per task: how many steps the agent needs, how much it costs, and how long each action takes, to identify actions that are especially time-consuming or expensive (AIE p.300).

These metrics can be compared against a baseline, such as another agent or a human operator. The comparison must account for the fact that humans and AI operate very differently, so what counts as efficient for a human may be inefficient for AI and vice versa: visiting 100 web pages sequentially is inefficient for a human who can view only one page at a time, but trivial for an AI agent able to visit many pages at once (AIE p.300).

## Key figures
None.

## Examples
- Visiting 100 web pages (trivial for an AI agent operating in parallel, inefficient for a sequential human operator)

## Related
- [[agent-failure-modes]]  (part-of: one of the three failure-mode categories)
- [[planning-failures]]  (boundary: a plan can be valid and use correct tools yet still score poorly on efficiency)
- [[tool-failures]]  (boundary: a tool can return correct output yet be slow or costly)

## Provenance
- [[sources/ch06-agent-failure-modes-and-evaluation]]
