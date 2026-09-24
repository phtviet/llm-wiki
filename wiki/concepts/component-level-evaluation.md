---
type: concept
sources: [ch04-step-1-evaluate-all-components-in-a-system]
---
# Component-Level Evaluation

Real-world AI applications often consist of multiple components chained together, and a task may complete only after many turns. Evaluation can happen at different levels: per task, per turn, and per intermediate output. Rather than only scoring the end-to-end output, each component's intermediate output should be evaluated independently, since without doing so it is impossible to know exactly where a system fails (AIE p.200).

The book's example: an application that extracts a person's current employer from a resume PDF works in two steps -- extracting all text from the PDF, then extracting the current employer from that text. If the final answer is wrong, the fault could lie in either step. The first step can be evaluated using similarity between extracted text and ground truth text; the second can be evaluated using accuracy, given correctly extracted text, of how often the employer is correctly identified (AIE p.200).

## Key figures
None.

## Examples
- Resume-parsing pipeline: PDF-to-text step scored by similarity to ground truth; employer-extraction step scored by accuracy (AIE p.200)

## Related
- [[turn-based-versus-task-based-evaluation]]  (see-also: both are ways of slicing evaluation across a multi-step or multi-turn application)
- [[evaluation]]  (part-of: component-level evaluation is one granularity within the broader practice of evaluating AI systems)

## Provenance
- [[sources/ch04-step-1-evaluate-all-components-in-a-system]]
