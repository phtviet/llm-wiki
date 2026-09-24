---
type: concept
sources: [ch08-ai-powered-data-synthesis]
---
# Model Collapse

Model collapse is a phenomenon where recursively training models on AI-generated data causes irreversible defects, degrading performance over time. Shumailov et al. (2023), in 'The Curse of Recursion: Training on Generated Data Makes Models Forget,' named the phenomenon and demonstrated it in Variational Autoencoders, Gaussian mixture models, and LLMs; it can occur during both pre-training and post-training (AIE p.394).

One explanation: AI models are more likely to generate probable events and less likely to generate improbable ones, so over multiple generations of recursive training, probable events become over-represented and rare events are forgotten (AIE p.394). Gerstgrasser et al. (2024) argue collapse is inevitable only if the entire training dataset is synthetic, and can be avoided by mixing synthetic with real data; Bertrand et al. (2023) and Dohmatob et al. (2024) show similar results, though none of these give a definitive recommendation for the synthetic-to-real ratio (AIE p.394). Counterexamples exist: synthetic data scaled to about one million samples showed no clear saturation when finetuning Llama 2-7B on math problems (Li et al., 2024), and Nemotron-4 340B-Instruct used 98% synthetic data during its instruction- and preference-finetuning phases -- though these are single-model-iteration results (AIE p.394).

## Key figures
- Synthetic data showed no clear saturation up to ~1 million samples finetuning Llama 2-7B on math (AIE p.394)
- Nemotron-4 340B-Instruct used 98% synthetic data in its instruction/preference finetuning (AIE p.394)

## Related
- [[data-synthesis]] (boundary: recursive training on purely synthetic data risks collapse, limiting how synthetic data can be used)
- [[nemotron-4]] (example-of: large-scale use of synthetic data without observed collapse, in a single iteration)

## Provenance
- [[sources/ch08-ai-powered-data-synthesis]]
