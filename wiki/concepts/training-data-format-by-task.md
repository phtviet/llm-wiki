---
type: concept
sources: [ch08-data-curation]
---
# Training Data Format by Task

What data a model needs depends on the training task. Self-supervised finetuning needs sequences of raw data. Instruction finetuning needs data in the (instruction, response) format. Preference finetuning needs data in the (instruction, winning response, losing response) format. A reward model can be trained on the same preference-finetuning format, or on data annotated with a score per example, in the ((instruction, response), score) format (AIE p.365).

Training data should exhibit the behaviors the model is meant to learn, which is straightforward for simple instructions but much harder for complex behaviors such as chain-of-thought reasoning and tool use (AIE p.365).

## Key figures
None.

## Examples
- [[chain-of-thought-data]]
- [[tool-use-data]]

## Related
- [[supervised-finetuning]]  (prerequisite: instruction-formatted data is what supervised finetuning trains on)
- [[preference-finetuning]]  (prerequisite: winning/losing response pairs are what preference finetuning trains on)
- [[reward-model]]  (prerequisite: scored or comparison-formatted data trains the reward model)
- [[self-supervised-finetuning]]  (prerequisite: raw data sequences are what this training step consumes)

## Provenance
- [[sources/ch08-data-curation]]
