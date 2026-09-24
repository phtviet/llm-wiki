---
type: concept
sources: [ch04-instruction-following-capability]
---
# IFEval

IFEval (Instruction-Following Evaluation) is a Google benchmark focused on whether a model's output follows an expected, automatically verifiable format. Zhou et al. (2023) identified 25 types of instructions that can be checked programmatically, grouped into categories such as keyword inclusion/frequency, forbidden words, letter frequency, response language, length constraints (paragraphs, words, sentences), detectable content (postscripts, placeholders), and detectable format (bullet counts, titles, JSON format, multiple sections) (AIE p.173). For example, an instruction to use the word 'ephemeral' can be checked by a simple program for the word's presence. A model's score is the fraction of instructions in the evaluation set that it follows correctly (AIE p.173).

## Key figures
- 25 types of automatically verifiable instructions identified by Zhou et al. (AIE p.173)

## Related
- [[instruction-following-capability]] (part-of: IFEval operationalizes a narrow, format-focused slice of instruction-following)
- [[infobench]] (contrast: restricted to automatically verifiable format instructions vs. INFOBench's broader content/linguistic/style coverage)
- [[structured-outputs]] (see-also: many IFEval instruction types, like JSON format, directly test structured-output ability)

## Provenance
- [[sources/ch04-instruction-following-capability]]
