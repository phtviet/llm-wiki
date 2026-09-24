---
type: entity
sources: [ch06-retrieval-algorithms]
---
# Elasticsearch

Elasticsearch (Shay Banon, 2010), built on top of Lucene, is a term-based retrieval solution using a data structure called an inverted index: a dictionary mapping terms to the documents that contain them, enabling fast retrieval given a term. The index may also store term frequency and document counts to support [[tf-idf|TF-IDF]]-style scoring (AIE p.259).

## Key figures
None.

## Related
- [[term-based-retrieval]]  (example-of: a common term-based retrieval solution built on an inverted index)
- [[bm25]]  (see-also: both are common term-based retrieval solutions)
- [[tf-idf]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch06-retrieval-algorithms]]
