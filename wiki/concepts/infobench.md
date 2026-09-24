---
type: concept
sources: [ch04-instruction-following-capability]
---
# INFOBench

INFOBench, created by Qin et al. (2024), takes a broader view of instruction-following than [[ifeval]]. Beyond format, it evaluates a model's ability to follow content constraints (e.g. 'discuss only climate change'), linguistic guidelines (e.g. 'use Victorian English'), and style rules (e.g. 'use a respectful tone') -- categories that can't be easily automated (AIE p.174).

For verification, INFOBench authors wrote a list of yes/no criteria per instruction. For example, the instruction 'Make a questionnaire to help hotel guests write hotel reviews' is checked with three yes/no questions: is the output a questionnaire, is it designed for hotel guests, and is it helpful for writing reviews. A model succeeds on an instruction only if its output meets all of that instruction's criteria; when an evaluator (human or AI) judges a model as meeting only some criteria, the score for that instruction is the fraction met (e.g. 2/3), and the benchmark's final score is the total criteria met divided by total criteria across all instructions (AIE p.174). The INFOBench authors found [[gpt-4|GPT-4]] a reasonably reliable and cost-effective evaluator -- less accurate than human experts but more accurate than Amazon Mechanical Turk annotators -- concluding the benchmark can be automatically verified using AI judges (AIE p.174).

## Key figures
None.

## Examples
- None beyond the hotel-review questionnaire example described above.

## Related
- [[ifeval]] (contrast: broader content/linguistic/style criteria vs. IFEval's automatically verifiable format checks)
- [[instruction-following-capability]] (part-of: INFOBench operationalizes a wide-scope version of instruction-following evaluation)
- [[ai-as-a-judge]] (example-of: GPT-4 used as a cost-effective evaluator for INFOBench's yes/no criteria)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch04-instruction-following-capability]]
