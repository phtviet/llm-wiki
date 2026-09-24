---
type: concept
sources: [ch07-finetuning-overview]
---
# Feature-Based Transfer

Feature-based transfer is an approach to [[transfer-learning]] distinct from finetuning: a model is trained to extract features from data, usually as embedding vectors, which are then used by another model (AIE p.309). It was very common in computer vision: in the second half of the 2010s, many people used models trained on the ImageNet dataset to extract image features for use in other computer vision tasks such as object detection or image segmentation (AIE p.309). Part of a [[foundation-model]] can similarly be reused for a classification task by adding a classifier head (AIE p.309).

## Key figures
None.

## Related
- [[transfer-learning]]  (part-of: one of two approaches to transfer learning, alongside finetuning)
- [[finetuning]]  (contrast: reuses extracted features via a separate downstream model rather than continuing to train the model itself)
- [[embedding]]  (prerequisite: extracted features usually take the form of embedding vectors)
- [[foundation-model]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch07-finetuning-overview]]
