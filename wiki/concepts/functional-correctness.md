---
type: concept
sources: [ch03-functional-correctness]
---
# Functional Correctness

Functional correctness evaluation means evaluating a system based on whether it performs its intended functionality -- for example, whether a generated website meets requirements, or a model succeeds at making a restaurant reservation. It is the ultimate metric for evaluating an application's performance, since it measures whether the application does what it is intended to do. However, it isn't always straightforward to measure, and its measurement can't always be automated (AIE p.126).

Tasks with measurable objectives can typically be evaluated using functional correctness. Code generation is a task where this can be automated: generated code is fed to an interpreter to check whether it is valid and produces the correct output for given inputs, an approach sometimes called execution accuracy. This practice predates AI, having long been standard in software engineering, where code is validated with unit tests, and is how coding platforms like LeetCode and HackerRank validate submissions. Game bots are another automatable category -- a Tetris bot's quality can be read directly from its score -- as is any task with a measurable objective, such as scheduling workloads to optimize energy consumption, where performance is measured by energy saved (AIE p.126-127).

## Key figures
None. The concept itself carries no intrinsic load-bearing figure; the worked pass@k example and benchmark-specific details live on [[pass-at-k]] and the individual benchmark entries.

## Examples
- [[pass-at-k]]  (metric for scoring code-generation functional correctness across multiple samples)
- [[humaneval]]  (OpenAI benchmark using functional correctness)
- [[mbpp]]  (Google benchmark using functional correctness)

## Related
- [[pass-at-k]]  (part-of: pass@k is the scoring method used to aggregate functional-correctness results over multiple generated samples)
- [[exact-evaluation]]  (see-also: both produce unambiguous, automatable judgments, contrasted with subjective evaluation)
- [[evaluation]]  (part-of: functional correctness is one evaluation approach within the broader evaluation methodology)

## Provenance
- [[sources/ch03-functional-correctness]]
