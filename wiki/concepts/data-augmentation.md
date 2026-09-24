---
type: concept
sources: [ch08-traditional-data-synthesis-techniques]
---
# Data Augmentation

Data augmentation creates new data from existing real data via transformations, contrasted with data synthesis, which generates data from scratch. For images, common transformations include random rotation, cropping, scaling, or erasing part of an image—a flipped image of a cat should still be a cat. Krizhevsky et al. (2012) used this technique in the legendary [[alexnet]] paper to augment the ImageNet dataset (Deng et al., 2009) (AIE p.384).

For text, augmentation can replace a word with a similar word (found via a synonym dictionary or nearby embeddings) without changing meaning or sentiment—e.g., 'She's a fantastic nurse' becomes 'She's a great nurse.' This can go further via AI-based rephrasing or translation. The technique can also mitigate bias: replacing gendered words (e.g. 'she' with 'he', or swapping names and roles) helps counter associations like 'nurse' with women and 'doctor' with men (AIE p.384). Snap (2022) documented augmenting character assets—varying skin color, body type, hairstyle, clothes, and facial expression—to create underrepresented corner cases and mitigate implicit bias in training data for AI models (AIE p.385).

[[perturbation]], adding noise to existing data, is a related form of augmentation used for both images and text.

## Key figures
None. No load-bearing figures are specific to data augmentation itself; see [[perturbation]] for its figures.

## Examples
- [[alexnet]]  (used image augmentation—rotation, cropping, scaling—on ImageNet)

## Related
- [[perturbation]]  (part-of: a form of data augmentation that adds noise rather than applying geometric or lexical transforms)
- [[data-synthesis]]  (contrast: augmentation transforms existing real data vs. synthesis generates new data from scratch)
- [[rule-based-data-synthesis]]  (see-also: both traditional, pre-AI techniques for expanding training data)

## Provenance
- [[sources/ch08-traditional-data-synthesis-techniques]]
