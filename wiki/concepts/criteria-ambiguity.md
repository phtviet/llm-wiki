---
type: concept
sources: [ch03-limitations-of-ai-as-a-judge]
---
# Criteria Ambiguity

Unlike many human-designed metrics, AI-as-a-judge criteria are not standardized, which makes them easy to misinterpret and misuse. Different evaluation tools define the same-named criterion differently, both in what they ask the judge and in what scale they use for the answer, so their outputs are not comparable (AIE p.142).

As an example, the open source tools MLflow, Ragas, and LlamaIndex all implement a criterion called faithfulness (how faithful a generated output is to its given context), but with different prompts and different scoring systems: MLflow scores faithfulness from 1 to 5, Ragas scores it as 0 or 1, and LlamaIndex's prompt asks the judge to answer YES or NO. Given a single (context, answer) pair, MLflow might return 3, Ragas might return 1, and LlamaIndex might return NO -- with no principled way to reconcile which score to trust (AIE p.142-143).

A related standardization problem: because an AI judge is itself an AI application, it can change over time (a prompt tweak, a typo fix, a model swap), so a shift in an application's measured score month to month may reflect a changed judge rather than a changed application -- especially risky when the application team and the judge team are different groups. The book advises not trusting any AI judge whose model and prompt cannot be inspected (AIE p.143).

## Key figures
None. The tool-specific scoring systems (MLflow 1-5, Ragas 0/1, LlamaIndex YES/NO) are illustrative of the ambiguity rather than load-bearing figures of a single concept.

## Related
- [[ai-as-a-judge]]  (boundary: unstandardized criteria are a limitation on how trustworthy AI-judge scores are)
- [[ai-judge-bias]]  (see-also: another source of untrustworthy AI-judge scores)

## Provenance
- [[sources/ch03-limitations-of-ai-as-a-judge]]
