---
type: concept
sources: [ch06-retrieval-optimization]
---
# Chunking Strategy

Chunking strategy is how documents are split into smaller pieces before indexing for retrieval, and how they are split significantly impacts retrieval performance (AIE p.267). The simplest approach splits documents into equal-length units — characters, words, sentences, or paragraphs (e.g. 2,048 characters or 512 words per chunk) — or a fixed number of sentences/paragraphs per chunk. A recursive strategy splits by increasingly smaller units (section, then paragraph, then sentence) only as needed to fit a maximum chunk size, reducing the chance of related text being arbitrarily broken off. Specific document types support creative strategies: language-specific code splitters, Q&A pairs as chunks, or different handling for Chinese versus English text (AIE p.268).

Splitting without overlap risks cutting a chunk off mid-context and losing critical information (e.g. "I left my wife a note" split into "I left my wife" and "a note" loses the point of the sentence). Overlapping chunk boundaries (e.g. a 20-character overlap for a 2,048-character chunk size) ensures boundary information appears in at least one chunk. Chunk size must not exceed the generative model's maximum context length, or, for embedding-based retrieval, the embedding model's context limit. Chunking can also be done by tokens using the generative model's own tokenizer, which eases downstream use but forces reindexing if the generative model (and its tokenizer) changes (AIE p.268).

Chunk size involves a tradeoff: smaller chunks let more diverse chunks fit into a model's context (halving chunk size roughly doubles how many chunks fit), but risk splitting a topic's information across chunks so part of it is never retrieved, and increase computational overhead — halving chunk size doubles the number of chunks to index, embeddings to generate and store, and the size of the vector search space, which can slow queries. There is no universal best chunk size or overlap size; it requires experimentation (AIE p.269).

## Key figures
- Example chunk size of 2,048 characters with a 20-character overlap (AIE p.268)
- Halving chunk size roughly doubles the number of chunks, embeddings, and vector search space, which can reduce query speed (AIE p.269)

## Examples
- [[contextual-retrieval]]  (augments chunks after they're split, to address lost context)

## Related
- [[reranking]]  (see-also: another retrieval-optimization tactic applied after chunks are indexed and retrieved)
- [[contextual-retrieval]]  (prerequisite: contextual retrieval augments chunks that chunking strategy first produces)
- [[context-length]]  (boundary: chunk size is capped by the generative or embedding model's context limit)
- [[embedding-based-retrieval]]  (see-also: chunk size directly affects the number of embeddings generated and indexed)

## Provenance
- [[sources/ch06-retrieval-optimization]]
