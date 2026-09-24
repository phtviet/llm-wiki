---
type: concept
sources: [ch06-agent-failure-modes-and-evaluation]
---
# Tool Failures

Tool failures happen when the correct tool is used, but the tool's output is wrong -- for example, an image captioner returning a wrong description, or an SQL query generator returning a wrong SQL query. If the agent generates only high-level plans and a separate translation module converts each planned action into executable commands, failures can also arise from translation errors (AIE p.299).

Tool failures can also occur because the agent lacks access to the right tools for the task altogether -- for instance, needing to retrieve current stock prices without internet access. Because tool failures are tool-dependent, each tool needs to be tested independently: printing out every tool call and its output allows inspection, and a dedicated translator should have its own benchmarks. Detecting missing-tool failures requires understanding what tools should be used, which the book suggests doing by working with human domain experts and observing which tools they would use when an agent frequently fails on a specific domain (AIE p.299).

## Key figures
None.

## Examples
- Image captioner returning a wrong description
- SQL query generator returning a wrong query
- Missing internet access preventing stock-price retrieval

## Related
- [[agent-failure-modes]]  (part-of: one of the three failure-mode categories)
- [[planning-failures]]  (contrast: correct tool but wrong output/translation vs. errors in the plan itself)
- [[agent-efficiency]]  (see-also: a correctly-functioning tool call can still be inefficient)

## Provenance
- [[sources/ch06-agent-failure-modes-and-evaluation]]
