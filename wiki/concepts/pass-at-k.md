---
type: concept
sources: [ch03-functional-correctness]
---
# Pass@k

Pass@k is a metric for scoring a model's code-generation performance using functional correctness. For each problem, a model generates k code samples; the model is considered to have solved the problem if any of the k samples passes all of the problem's test cases. The pass@k score is the fraction of problems solved out of all problems (AIE p.127).

Generating more code samples per problem gives the model more chances to solve each one, so pass@k scores increase with k: in expectation, pass@1 should be lower than pass@3, which in turn should be lower than pass@10 (AIE p.127).

## Key figures
- Worked example: with 10 problems and k=3, solving 5 of them gives a pass@3 score of 50% (AIE p.127)

## Examples
- [[humaneval]]  (benchmark that scores models using pass@k)

## Related
- [[functional-correctness]]  (part-of: pass@k is the scoring method for functional-correctness evaluation of code generation)
- [[humaneval]]  (example-of: benchmark that reports pass@k scores)

## Provenance
- [[sources/ch03-functional-correctness]]
