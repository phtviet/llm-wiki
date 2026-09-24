---
type: concept
sources: [ch01-from-language-models-to-large-language-models]
---
# Supervision

Supervision is the process of training ML algorithms using labeled data: examples are labeled to show the desired behavior, the model is trained on those examples, and the trained model is then applied to new data (AIE p.6). The success of AI models in the 2010s rested on supervision -- [[alexnet]] (Krizhevsky et al., 2012), the model that started the deep learning revolution, was trained on labeled ImageNet data to classify images into 1,000 categories (AIE p.6).

A core drawback of supervision is that data labeling is expensive and slow: at 5 cents per image, labeling 1 million ImageNet images costs $50,000, and double that for cross-checked dual labeling; scaling to 1 million categories would push labeling costs to roughly $50 million (AIE p.7). Labeling cost also varies with task difficulty -- everyday-object labeling is cheap, but tasks like generating Latin translations or reading CT scans for cancer are far more costly (AIE p.7). As of September 2024, Amazon SageMaker Ground Truth charged 8 cents per image for labeling under 50,000 images, but only 2 cents per image for over 1 million images (AIE p.6).

## Key figures
- Labeling 1 million ImageNet images at 5 cents each costs $50,000; doubling for cross-checked labels (AIE p.7)
- Scaling to 1 million categories raises labeling cost to about $50 million (AIE p.7)
- Amazon SageMaker Ground Truth: 8 cents/image under 50,000 images, 2 cents/image over 1 million images (AIE p.6)

## Examples
- [[alexnet]]  (supervised model trained on labeled ImageNet data)

## Related
- [[self-supervision]]  (contrast: requires labeled data vs. infers labels from the input itself)

## Provenance
- [[sources/ch01-from-language-models-to-large-language-models]]
