---
type: concept
sources: [ch02-structured-outputs]
---
# Post-processing (Structured Outputs)

Post-processing corrects a model's output after generation using a script, rather than changing the prompt or the model. It is simple and cheap, and works well when a model repeats similar, easily-fixable mistakes across queries — such as a JSON object missing its closing bracket, which a script can add back. Post-processing only works when the mistakes are easy to fix, i.e. when the model's outputs are already mostly correctly formatted with occasional small errors (AIE p.101-102).

LinkedIn's defensive YAML parser is the book's example: it raised the percentage of correct YAML outputs from 90% to 99.99% (Bottaro and Ramgopal, 2020) (AIE p.102). LinkedIn chose YAML over JSON as their output format because YAML is less verbose and requires fewer output tokens, even though their underlying model ([[gpt-4|GPT-4]]) worked with both (AIE p.102).

## Key figures
- LinkedIn's defensive YAML parser raised correct-YAML-output rate from 90% to 99.99% (AIE p.102)

## Related
- [[structured-outputs]]  (part-of: one of the layers at which structured generation can be guided)
- [[prompting-for-structure]]  (contrast: corrects output after generation vs. shapes the instruction before generation)
- [[constrained-sampling]]  (contrast: cheap post-hoc fix vs. filtering the sampling process itself)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-structured-outputs]]
