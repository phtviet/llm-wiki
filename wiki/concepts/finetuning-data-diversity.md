---
type: concept
sources: [ch08-data-quantity]
---
# Finetuning Data Diversity

Beyond raw example count, the diversity of finetuning data -- across task types (e.g., summarization vs. question answering), topics (e.g., fashion, finance, technology), and expected output formats (e.g., JSON vs. yes/no answers) -- affects model performance (AIE p.376). "Scaling Instruction-Finetuned Language Models" (Chung et al., 2022) found that performance increased significantly as the number of finetuning tasks grew from 9 to 282, with gains plateauing but still incrementally positive up to 1,836 tasks, showing the model benefits from exposure to a diverse set of tasks during finetuning (AIE p.376).

## Key figures
- Performance increased significantly as finetuning tasks grew from 9 to 282; incremental gains continued up to 1,836 tasks before largely plateauing (AIE p.376)

## Related
- [[data-quantity]]  (part-of: diversity is a factor alongside raw example count in determining data needs)
- [[data-coverage]]  (see-also: both describe the need for training data to span a broad range of cases)
- [[training-data-curation]]  (see-also: diversity is one dimension considered when curating training data)

## Provenance
- [[sources/ch08-data-quantity]]
