---
type: concept
sources: [ch06-retrieval-optimization]
---
# Contextual Retrieval

Contextual retrieval augments each chunk with relevant context to make it easier for a retriever to find the relevant chunk. A simple technique augments a chunk with metadata like tags and keywords — for ecommerce, a product chunk can be augmented with its description and reviews, and images or videos can be queried by title or caption. Metadata can also include entities automatically extracted from the chunk, such as a specific error code, so the chunk remains retrievable by that keyword even after being converted to embeddings (AIE p.271).

Chunks can also be augmented with the questions they can answer — for customer support, an article on resetting a password might be augmented with queries like "How to reset password?" or "I forgot my password." When a document is split into multiple chunks, some chunks lack enough context on their own; augmenting each chunk with context from the original document (e.g. its title and summary) addresses this. Anthropic used AI models to generate a short context, typically 50-100 tokens, explaining a chunk and its relationship to the original document, using a prompt that supplies the whole document and the chunk and asks for succinct situating context (Anthropic, 2024). The generated context is prepended to each chunk before the augmented chunk is indexed (AIE p.271-272).

## Key figures
- Anthropic's generated context is typically 50-100 tokens per chunk (AIE p.271)

## Examples
None.

## Related
- [[chunking-strategy]]  (prerequisite: contextual retrieval augments chunks that chunking strategy has already produced)
- [[embedding-based-retrieval]]  (boundary: augmented metadata like extracted entities lets a chunk be retrieved by keyword even after conversion to embeddings)

## Provenance
- [[sources/ch06-retrieval-optimization]]
