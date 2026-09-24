---
type: concept
sources: [ch08-data-curation]
---
# Chain-of-Thought Data

To teach a model to generate step-by-step responses, its training data must itself include chain-of-thought (CoT) responses that work through a problem before giving the final answer, rather than jumping straight to the answer (AIE p.365).

"Scaling Instruction-Finetuned Language Models" (Chung et al., 2024) shows that incorporating step-by-step responses in finetuning data greatly enhances performance on CoT tasks across model sizes, with accuracy nearly doubling for certain tasks. Generating multi-step responses is more tedious and time-consuming to annotate than giving a final answer alone -- explaining a math solution step-by-step takes far more effort than stating the answer -- so CoT datasets are less common than other instruction datasets (AIE p.365-366).

## Key figures
- Incorporating CoT responses in finetuning data nearly doubles accuracy on certain tasks (AIE p.365)

## Examples
- Boiling point question answered with a bare figure ('-320.4F') vs. an apple-counting question answered by reasoning through each arithmetic step (AIE p.365-366)

## Related
- [[chain-of-thought-prompting]]  (prerequisite: CoT training data is what teaches a model the step-by-step behavior that CoT prompting elicits at inference time)
- [[training-data-format-by-task]]  (part-of: one of the behavior-specific data types a model may need)
- [[demonstration-data]]  (example-of: CoT responses are a harder-to-produce kind of demonstration data)

## Provenance
- [[sources/ch08-data-curation]]
