---
type: synthesis
sources: [ch08-dataset-engineering]
---
# Data-Centric vs. Model-Centric AI

The book contrasts two approaches to improving AI performance. Model-centric AI
improves performance by enhancing the model itself: designing new architectures,
increasing [[model-size]], or developing new training techniques. Data-centric AI instead
improves performance by enhancing the data: developing new data processing techniques
and creating high-quality datasets that let a better model be trained with fewer
resources (AIE p.364).

Early deep learning benchmarks were largely model-centric: given a fixed dataset like
ImageNet, researchers competed to train the best possible model on it. More recent
benchmarks have shifted to being data-centric: given a fixed model, participants
compete to build the dataset that yields the best performance. Andrew Ng's 2021
data-centric AI competition asked participants to improve a fixed base dataset (fixing
incorrect labels, adding edge cases, augmenting data). DataComp (Gadre et al., 2023)
had participants build the best training dataset for a CLIP model, with a standardized
script training and scoring each submission across 38 downstream tasks; a 2024 edition
extended this to language models from 412M to 7B parameters (Li et al., 2024). Other
data-centric benchmarks include DataPerf and dcbench (AIE p.364).

The book treats this as a framing device rather than a strict binary: meaningful
progress in practice usually requires investment in both model and data improvements,
not a choice of one over the other (AIE p.365).

## Key figures
- DataComp evaluated submitted datasets on 38 downstream tasks (AIE p.364)
- 2024 DataComp language-model edition spanned model scales from 412M to 7B parameters (AIE p.364)

## Related
- [[dataset-engineering]]  (prerequisite: dataset engineering is the practical discipline this data-centric framing motivates)
- [[training-data-curation]]  (see-also: curating data for quality is a core data-centric-AI activity)
- [[model-size]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch08-dataset-engineering]]
