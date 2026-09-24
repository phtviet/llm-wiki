---
type: concept
sources: [ch06-rag-architecture]
---
# RAG Architecture

A RAG (retrieval-augmented generation) system has two components: a retriever that retrieves information from external memory sources, and a generator that generates a response based on the retrieved information (AIE p.256). In the original RAG paper, Lewis et al. trained the retriever and the generative model together, but in today's RAG systems the two components are often trained separately, with many teams building RAG systems from off-the-shelf retrievers and models; finetuning the whole system end-to-end can still improve performance significantly (AIE p.256).

In a worked example, the external memory is a database of documents (e.g. a company's memos, contracts, and meeting notes). Since a document can range from 10 tokens to 1 million tokens, naively retrieving whole documents can make the context arbitrarily long, so documents are split into more manageable chunks first. For each query, the goal is to retrieve the chunks most relevant to it; minor post-processing then joins the retrieved chunks with the user prompt to form the final prompt fed to the generative model (AIE p.257). The book uses "document" to refer to both a full document and a chunk of one, since a chunk is technically also a document, keeping terminology consistent with classical NLP and information-retrieval usage (AIE p.257).

## Key figures
- A document can range from 10 tokens to 1 million tokens (AIE p.257)

## Examples
- [[retriever]]  (indexing and querying component of a RAG system)

## Related
- [[retriever]]  (part-of: the retriever is one of the two components of a RAG architecture)
- [[context-construction]]  (part-of: retrieval is one method of gathering context for a query)
- [[chunking]]  (prerequisite: documents must be chunked before retrieval to keep context manageable)

## Provenance
- [[sources/ch06-rag-architecture]]
