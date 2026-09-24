---
type: concept
sources: [ch06-rag-beyond-texts]
---
# Multimodal RAG

Multimodal RAG augments a query's context with non-text data, such as images, video,
or audio, in addition to or instead of text documents. Given a query, the retriever
fetches both texts and other-modality items relevant to it — for example, given "What's
the color of the house in the Pixar movie Up?", the retriever can fetch a picture of the
house to help the model answer (AIE p.273).

If retrieved items (e.g. images) have metadata such as titles, tags, and captions, they
can be retrieved via that metadata — an image is retrieved if its caption is judged
relevant to the query. To retrieve based on content instead, the system needs a way to
compare items across modalities directly, which requires a multimodal embedding model
capable of generating embeddings for both texts and images, such as [[clip]] (Radford et
al., 2021). The retriever then: (1) generates embeddings for all data, text and images,
and stores them in a [[vector-database]]; (2) generates an embedding for the query; (3)
queries the vector database for all images and texts whose embeddings are close to the
query embedding (AIE p.273).

## Key figures
None.

## Examples
- [[clip]]  (multimodal embedding model enabling text-to-image retrieval)

## Related
- [[rag-architecture]]  (part-of: multimodal RAG extends the retriever/generator design to non-text modalities)
- [[embedding]]  (prerequisite: requires embeddings comparable across modalities to match queries to images)
- [[retriever]]  (part-of: the retriever component is what fetches multimodal items)
- [[rag-with-tabular-data]]  (contrast: augments context with structured table data instead of unstructured multimodal data)
- [[clip]]  (example-of: multimodal embedding model used to generate embeddings for both texts and images)
- [[vector-database]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch06-rag-beyond-texts]]
