---
type: concept
sources: [ch08-traditional-data-synthesis-techniques]
---
# Perturbation

Perturbation adds noise to existing data to generate new data. Researchers first discovered that small perturbations can trick models into misclassifying inputs—for instance, adding white noise to a picture of a ship can cause a model to misclassify it as a car (AIE p.385). The paper 'One Pixel Attack for Fooling Deep Neural Networks' (Su et al., 2017) showed that changing just one pixel could cause misclassification in 67.97% of natural images in the Kaggle CIFAR-10 test set and 16.04% of ImageNet test images (AIE p.385). Such vulnerabilities pose real risks, e.g. tricking a system into misidentifying an unauthorized person as an employee, or a self-driving car into mistaking a divider for a lane.

Training on perturbed data can both improve performance and increase robustness against such attacks (Goodfellow et al., 2013; Moosavi-Dezfooli et al., 2015). Hendrycks and Dietterich (2019) created ImageNet-C and ImageNet-P by applying 15 common visual corruptions (e.g. brightness changes, snow, contrast changes, noise) to ImageNet images (AIE p.385). Perturbation also applies to text: to train [[bert]], the authors replaced 1.5% of tokens with random words, which produced a small performance boost (Devlin et al., 2018) (AIE p.385).

## Key figures
- One-pixel changes misclassified 67.97% of Kaggle CIFAR-10 test images and 16.04% of ImageNet test images (AIE p.385)
- BERT training replaced 1.5% of tokens with random words as perturbation (AIE p.385)

## Examples
- [[bert]]  (trained with 1.5% random token replacement as perturbation)

## Related
- [[data-augmentation]]  (part-of: perturbation is one form of augmenting existing data with noise)
- [[data-synthesis]]  (part-of: a traditional technique predating AI-powered synthesis)

## Provenance
- [[sources/ch08-traditional-data-synthesis-techniques]]
