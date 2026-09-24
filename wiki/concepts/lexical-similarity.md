---
type: concept
sources: [ch03-similarity-measurements-against-reference-data]
---
# Lexical Similarity

Lexical similarity measures how much two texts overlap, by first breaking each text into tokens and comparing them. In its simplest form, it counts how many tokens two texts have in common: given reference "My cats scare the mice" and candidate "My cats eat the mice" (4 of 5 words match, 80% similarity) versus "Cats and mice fight all the time" (3 of 5 words match, 60% similarity), the first candidate scores higher (AIE p.130).

One method is approximate string matching (fuzzy matching), which counts the edit distance -- the number of deletions, insertions, and substitutions needed to convert one text into another (some fuzzy matchers also count transposition as an edit, others count it as a deletion plus insertion). For example, "bad" is one edit from "bard" but three edits from "cash", so "bad" is considered more similar to "bard" (AIE p.130).

Another method is n-gram similarity, based on overlap of n-token sequences rather than single tokens: a unigram is one token, a bigram is a set of two tokens ("My cats scare the mice" has four bigrams). N-gram similarity measures what percentage of the reference's n-grams also appear in the generated response (AIE p.131).

Common lexical-similarity metrics are BLEU, ROUGE, METEOR++, TER, and CIDEr, differing in how overlap is calculated; these were common before foundation models, especially for translation, and are still used by benchmarks like WMT, COCO Captions, and GEMv2 (AIE p.131).

Drawbacks: lexical similarity requires a comprehensive set of reference responses -- a correct response can score low if no reference resembles it (Adept found this happening with its Fuyu model on an image-captioning benchmark). References themselves can also be wrong (WMT 2023 Metrics shared-task organizers found many bad reference translations), which is part of why reference-free metrics have become strong contenders on correlation to human judgment (Freitag et al., 2023). Additionally, higher lexical similarity doesn't always mean a better response: on [[humaneval]], OpenAI found BLEU scores similar for correct and incorrect code solutions, showing that optimizing for BLEU is not the same as optimizing for functional correctness (Chen et al., 2021) (AIE p.131).

## Key figures
- Example word-overlap scores: 80% (4/5 words) vs. 60% (3/5 words) for two candidate responses against the same reference (AIE p.130)

## Related
- [[reference-based-evaluation]]  (part-of: lexical similarity is one of the three reference-based similarity measurements)
- [[exact-match]]  (contrast: exact match is binary and requires an identical response, lexical similarity is a sliding-scale overlap score)
- [[semantic-similarity]]  (contrast: lexical similarity measures surface-level token overlap vs. meaning)
- [[functional-correctness]]  (boundary: high lexical similarity (BLEU) does not imply functional correctness, as shown on HumanEval)
- [[humaneval]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch03-similarity-measurements-against-reference-data]]
