---
type: concept
sources: [ch03-exact-evaluation]
---
# Exact Evaluation

Exact evaluation produces judgment without ambiguity: given a multiple-choice question with correct answer A, picking B is simply wrong, with no room for disagreement. This contrasts with subjective evaluation, such as essay grading, where scores depend on the grader and can even vary for the same grader asked twice, though clear grading guidelines can make subjective evaluation more exact. [[ai-as-a-judge]] is an example of subjective evaluation, since results can change based on the judge model and the prompt used (AIE p.125).

Two approaches produce exact scores: functional correctness and similarity measurements against reference data. Exact evaluation, as covered here, focuses on evaluating open-ended responses (arbitrary text generation) rather than close-ended responses (such as classification), not because foundation models lack close-ended uses -- many foundation model systems include a classification component, typically for intent classification or scoring -- but because close-ended evaluation is already well understood (AIE p.125).

## Key figures
None.

## Examples
- [[functional-correctness]]  (exact scoring by checking whether a task was accomplished)
- [[similarity-measurements-against-reference-data]]  (exact scoring by comparing output to a reference)

## Related
- [[ai-as-a-judge]]  (contrast: subjective evaluation whose results depend on judge model and prompt, vs. exact evaluation's unambiguous scoring)
- [[evaluation]]  (part-of: exact evaluation is one category of approaches to assessing model and application performance)

## Provenance
- [[sources/ch03-exact-evaluation]]
