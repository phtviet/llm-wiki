---
type: entity
sources: [ch03-functional-correctness]
---
# HumanEval

HumanEval is OpenAI's benchmark for evaluating AI code-generation capabilities, using functional correctness (pass@k) as its metric. Each benchmark problem comes with a set of test cases, each consisting of a scenario the code should run and the expected output, expressed as assert statements checked against the candidate function (AIE p.126).

## Key figures
None.

## Related
- [[functional-correctness]]  (example-of: benchmark applying functional-correctness evaluation to code generation)
- [[pass-at-k]]  (example-of: benchmark scored using the pass@k metric)
- [[mbpp]]  (contrast: both are functional-correctness code-generation benchmarks, from OpenAI vs. Google)

## Provenance
- [[sources/ch03-functional-correctness]]
