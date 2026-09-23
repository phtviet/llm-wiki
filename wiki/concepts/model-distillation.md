---
type: concept
sources: [ch08-model-distillation]
---
# Model Distillation

Model distillation (also called knowledge distillation) is a method in which a small
model (student) is trained to mimic a larger model (teacher) (Hinton et al., 2015). The
knowledge of the big model is distilled into the small model, hence the term. Traditionally,
the goal of model distillation is to produce smaller models for deployment: deploying a
big model can be resource-intensive, and distillation can produce a smaller, faster
student model that retains performance comparable to the teacher (AIE p.395).

The student model can be trained from scratch, like [[distilbert]], or finetuned from a
pre-trained model, like [[alpaca]] (AIE p.395). This is a required use of synthetic data:
the student trains on the teacher's generated outputs, which is what distinguishes
distillation as a special case of data synthesis rather than a merely optional one. A
practical limit: many model licenses prohibit using a model's outputs to train other,
particularly competing, models, so not all models can be distilled (AIE p.395).

## Key figures
None. The concept carries no intrinsic load-bearing figure; the model-specific numbers
(DistilBERT's 40% / 97% / 60%, Alpaca's 4%) live on the entity pages, per fact-placement.

## Examples
- [[distilbert]]  (student trained from scratch; distilled from BERT)
- [[alpaca]]  (student finetuned from a pre-trained model; Llama-7B tuned on text-davinci-003 outputs)

## Related
- [[quantization]]  (contrast: other main model-compression method; lowers numerical precision vs. trains a small student)
- [[data-synthesis]]  (part-of: distillation is a required use of synthetic data, since the student trains on the teacher's generated outputs; boundary: not all synthetic-data training is distillation)
- [[nemotron-4]]  (boundary: training a student to surpass its teacher on synthetic data is not distillation, since distillation implies the teacher's performance is the student's gold standard)

## Provenance
- [[sources/ch08-model-distillation]]
