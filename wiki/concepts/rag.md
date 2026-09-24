---
type: concept
sources: [ch06-rag]
---
# RAG (Retrieval-Augmented Generation)

RAG is a technique that enhances a model's generation by retrieving relevant information from external memory sources -- an internal database, a user's previous chat sessions, or the internet (AIE p.253). Because instructions are common to all queries while context is specific to each query, RAG constructs context per query instead of reusing the same context for every query; the book likens this to feature engineering for classical ML models, since both serve to give a model the information it needs to process an input (AIE p.255).

The retrieve-then-generate pattern was first introduced in 'Reading Wikipedia to Answer Open-Domain Questions' (Chen et al., 2017), where a system retrieves the five Wikipedia pages most relevant to a question and a reader model uses them to generate an answer. The term retrieval-augmented generation itself was coined in 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks' (Lewis et al., 2020), proposed for knowledge-intensive tasks where all available knowledge cannot be input into the model directly; only the information the retriever judges most relevant is retrieved and input into the model. Lewis et al. found that access to relevant information helps a model generate more detailed responses while reducing hallucinations (AIE p.254).

RAG emerged early as a way to overcome models' context-length limitations. The book argues a sufficiently long context will not end RAG's usefulness, for two reasons: available data only grows over time, so context length will never expand fast enough for every application's data needs; and a model that can process long context does not necessarily use that context well, since longer contexts make a model more likely to focus on the wrong part, and every extra context token adds cost and potential latency. RAG lets a model use only the most relevant information per query, cutting input tokens while potentially increasing performance (AIE p.255).

## Key figures
None. The concept carries no intrinsic load-bearing figure of its own beyond the illustrative token count on the Anthropic mention (AIE p.256).

## Examples
- [[rag-architecture]]  (two-component retriever/generator design implementing this pattern)

## Related
- [[agent]]  (contrast: agentic pattern uses tools like web search and news APIs to gather information, and can do far more than construct context, unlike RAG which is chiefly for context construction)
- [[context-construction]]  (part-of: RAG is one method of context construction, alongside web search)
- [[context-length]]  (boundary: longer context does not eliminate the need for RAG, since data needs keep growing and models may not use long context effectively)
- [[hallucination]]  (see-also: Lewis et al. found relevant retrieved information reduces hallucination)

## Provenance
- [[sources/ch06-rag]]
