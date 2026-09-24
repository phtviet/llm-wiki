---
type: concept
sources: [ch03-similarity-measurements-against-reference-data]
---
# Semantic Similarity

Semantic similarity measures how close two texts are in meaning rather than surface form, and is therefore also called embedding similarity. Lexically dissimilar sentences like "What's up?" and "How are you?" can be semantically close, while lexically similar sentences like "Let's eat, grandma" and "Let's eat grandma" can mean very different things (AIE p.131-132).

Computing semantic similarity first requires transforming text into a numerical [[embedding]] (e.g. "the cat sits on a mat" might become [0.11, 0.02, 0.54]). The similarity between two embeddings is then commonly computed with cosine similarity: for embeddings A and B, cosine similarity = (A · B) / (||A|| ||B||), where A · B is the dot product and ||A|| is the Euclidean (L2) norm of A. A score of 1 means the embeddings are identical; –1 means they are opposite (AIE p.132).

Semantic similarity applies to embeddings of any data modality, not just text (for text specifically it is sometimes called semantic textual similarity). It is classified here as an exact-evaluation technique in the sense that, given two embeddings, the similarity score between them is computed exactly -- though it can be considered subjective, since different embedding algorithms produce different embeddings for the same text (AIE p.132). Metrics for semantic textual similarity include BERTScore (embeddings from BERT) and MoverScore (embeddings from a mixture of algorithms) (AIE p.132).

Unlike lexical similarity, semantic similarity does not require as comprehensive a set of reference responses. However, its reliability depends entirely on the quality of the underlying embedding algorithm -- two texts with the same meaning can still score low if their embeddings are poor -- and computing embeddings can require nontrivial compute and time (AIE p.132).

## Key figures
None. (The 0.11/0.02/0.54 vector and cosine-similarity bounds of 1 / -1 are illustrative of the mechanism, not load-bearing figures about a specific model or dataset.)

## Examples
- [[bert]]  (BERTScore uses BERT-generated embeddings for semantic textual similarity)

## Related
- [[reference-based-evaluation]]  (part-of: semantic similarity is one of the three reference-based similarity measurements)
- [[embedding]]  (prerequisite: semantic similarity requires first transforming text into embeddings)
- [[lexical-similarity]]  (contrast: semantic similarity compares meaning vs. surface token overlap)
- [[exact-match]]  (contrast: semantic similarity is a sliding-scale meaning comparison vs. exact match's binary surface comparison)

## Provenance
- [[sources/ch03-similarity-measurements-against-reference-data]]
