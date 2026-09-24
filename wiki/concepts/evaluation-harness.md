---
type: concept
sources: [ch04-navigate-public-benchmarks]
---
# Evaluation Harness

An evaluation harness is a tool that runs a model against many benchmarks at once, rather than requiring each benchmark to be scripted separately. As of the book's writing, EleutherAI's lm-evaluation-harness supports over 400 benchmarks, and OpenAI's evals lets users run any of roughly 500 existing benchmarks and register new ones to evaluate OpenAI models, covering capabilities from math and puzzles to identifying ASCII art (AIE p.191).

## Key figures
- EleutherAI's lm-evaluation-harness supports over 400 benchmarks (AIE p.191)
- OpenAI's evals supports approximately 500 existing benchmarks (AIE p.191)

## Examples
- [[bigbench]]  (large benchmark collection an evaluation harness might run against)

## Related
- [[benchmark-selection-and-aggregation]]  (prerequisite: running many benchmarks via a harness is what makes leaderboard construction from public benchmarks practical)
- [[model-selection]]  (part-of: harnesses support the benchmarking step of model selection)

## Provenance
- [[sources/ch04-navigate-public-benchmarks]]
