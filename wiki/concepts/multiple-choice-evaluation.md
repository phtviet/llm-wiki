---
type: concept
sources: [ch04-domain-specific-capability]
---
# Multiple-Choice Evaluation

A close-ended approach to evaluating a model's domain-specific capability: rather than asking the model to generate an open-ended solution, the model is given several options and must pick the correct one. Close-ended outputs are easier to verify and reproduce than open-ended generation, which is why this format dominates public benchmarks -- in April 2024, 75% of tasks in Eleuther's lm-evaluation-harness were multiple-choice, including [[mmlu]], Microsoft's AGIEval (2023), and the AI2 Reasoning Challenge (ARC-C) (2018) (AIE p.162).

A multiple-choice question (MCQ) may have one or more correct answers. The common metric is accuracy, the share of questions the model gets right; some tasks use a point system where harder questions are worth more points, or award partial points across multiple correct options. Classification is a special case of multiple choice where the same choices apply to every question (e.g. NEGATIVE, POSITIVE, NEUTRAL for tweet sentiment); classification tasks add metrics such as F1 score, precision, and recall (AIE p.162).

MCQs are popular because they are easy to create, verify, and evaluate against a random baseline: with four options and one correct answer, random-guess accuracy is 25%, so a score meaningfully above that baseline typically, though not always, indicates the model is doing better than chance (AIE p.162).

A drawback is prompt sensitivity: Alzahrani et al. (2024) found that adding an extra space between question and answer, or adding an instructional phrase like 'Choices:', can change a model's answer. MCQs test the ability to differentiate good responses from bad ones (classification), which differs from the ability to generate good responses, so they suit evaluating knowledge and reasoning but not generation capabilities such as summarization, translation, and essay writing (AIE p.163).

## Key figures
- 75% of Eleuther's lm-evaluation-harness tasks were multiple-choice as of April 2024 (AIE p.162)
- Random-baseline accuracy is 25% for a four-option, single-correct-answer question (AIE p.162)

## Examples
- [[mmlu]]  (UC Berkeley's multiple-choice benchmark, includes monopoly-regulation example question)

## Related
- [[domain-specific-capability]]  (part-of: multiple-choice evaluation is a common way to evaluate non-coding domain capabilities)
- [[exact-evaluation]]  (example-of: multiple-choice questions produce unambiguous, exactly-verifiable judgments)
- [[generation-capability]]  (boundary: MCQs test classification/discrimination between responses, not the ability to generate good responses, so they are not ideal for evaluating generation capabilities)
- [[prompt-engineering]]  (boundary: small changes in question/option presentation, such as extra spacing or added instructional phrases, can change a model's MCQ answer)

## Provenance
- [[sources/ch04-domain-specific-capability]]
