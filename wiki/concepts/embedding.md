---
type: concept
sources: [ch03-introduction-to-embedding]
---
# Embedding

An embedding is a numerical representation, in vector form, that aims to capture the meaning of the original data (AIE p.134). Since computers work with numbers, models convert input into embeddings before processing it; many models, including GPTs and Llamas, include a step to generate embeddings, typically within a [[transformer-architecture]]'s embedding layer (AIE p.134).

An embedding algorithm is considered good if more-similar inputs have closer embeddings, measured by cosine similarity or related metrics -- for example, the embedding of 'the cat sits on a mat' should be closer to 'the dog plays on the grass' than to 'AI research is super fun' (AIE p.135). Embedding quality can also be evaluated by utility for a downstream task; embeddings are used in classification, topic modeling, recommender systems, and RAG (AIE p.135).

Embeddings are not limited to text: ecommerce solutions have product embeddings, and Pinterest has embeddings for images, graphs, queries, and users (AIE p.135). A joint embedding space that represents data of different modalities is called a multimodal embedding space; in a text-image joint space, an image of a man fishing should embed closer to 'a fisherman' than to 'fashion show', enabling applications like text-based image search (AIE p.136).

## Key figures
- Embedding vector size is typically between 100 and 10,000 elements (AIE p.134)

## Examples
- [[bert]]  (BERT base: 768, BERT large: 1024 embedding size)
- [[clip]]  (image and text embeddings, both size 512)
- [[sentence-transformers]]  (open source model trained specifically to produce embeddings)

## Related
- [[multimodal-model]]  (part-of: a joint multimodal embedding space is what makes multimodal mapping possible)
- [[mteb]]  (evaluates: MTEB benchmarks embedding quality across multiple tasks)
- [[transformer-architecture]]  (part-of: transformer models include an embedding layer as an internal step)
- [[clip]]  (example-of: CLIP maps text and images into a joint embedding space)

## Provenance
- [[sources/ch03-introduction-to-embedding]]
