---
type: concept
sources: [ch04-step-1-evaluate-all-components-in-a-system]
---
# Twenty Questions Benchmark

The twenty_questions benchmark, part of the [[bigbench]] benchmark suite, is an example of task-based evaluation inspired by the classic game Twenty Questions. One instance of the model (Alice) chooses a concept, such as apple, car, or computer. A second instance of the model (Bob) asks Alice a series of yes/no questions to try to identify the concept. The score is based on whether Bob successfully guesses the concept, and how many questions it takes (AIE p.201).

In a sample conversation from BIG-bench's GitHub repository, Bob narrows the concept down through questions ('Is the concept an animal?' 'Is the concept a plant?' 'Does it grow in a tree?') before correctly guessing 'apple' (AIE p.201).

## Key figures
None.

## Examples
- Alice/Bob apple-guessing conversation from BIG-bench's GitHub repository (AIE p.201)

## Related
- [[bigbench]]  (part-of: twenty_questions is one benchmark within the BIG-bench suite)
- [[turn-based-versus-task-based-evaluation]]  (example-of: a concrete instance of task-based evaluation)

## Provenance
- [[sources/ch04-step-1-evaluate-all-components-in-a-system]]
