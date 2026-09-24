---
type: concept
sources: [ch04-generation-capability]
---
# Textual Entailment

Textual entailment (also known as natural language inference, or NLI) is a long-standing NLP task of determining the relationship between two statements: given a premise (context) and a hypothesis (the output, or part of it), the pair falls into one of three categories (AIE p.168):

- **Entailment** — the hypothesis can be inferred from the premise (e.g. given "Mary likes all fruits", "Mary likes apples" is entailment).
- **Contradiction** — the hypothesis contradicts the premise (e.g. "Mary hates oranges").
- **Neutral** — the premise neither entails nor contradicts the hypothesis (e.g. "Mary likes chickens").

Entailment implies factual consistency, contradiction implies factual inconsistency, and neutral implies consistency can't be determined. This framing lets factual-consistency verification be posed as a classification task over (premise, hypothesis) pairs (AIE p.168).

## Key figures
None.

## Related
- [[factual-consistency]]  (prerequisite: entailment classification is one way to determine factual consistency)

## Provenance
- [[sources/ch04-generation-capability]]
