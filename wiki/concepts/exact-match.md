---
type: concept
sources: [ch03-similarity-measurements-against-reference-data]
---
# Exact Match

Exact match considers a generated response correct if it matches one of the reference responses exactly. It works for tasks expecting short, exact responses, such as simple math problems, common knowledge queries, and trivia-style questions (e.g., "What's 2 + 3?" or "Who was the first woman to win a Nobel Prize?") (AIE p.129).

A common variation accepts any output that *contains* the reference response as a match. For "What's 2 + 3?" with reference "5", this accepts "The answer is 5" or "2 + 3 is 5". This variation can misfire: for "What year was Anne Frank born?" (correct answer 1929), an output like "September 12, 1929" contains the correct year but is factually wrong about the date (AIE p.129-130).

Beyond simple tasks, exact match rarely works. A French sentence like "Comment ça va?" has many valid English translations ("How are you?", "How is everything?", "How are you doing?"); a correct but unlisted translation such as "How is it going?" would be marked wrong. The longer and more complex the text, the more valid responses exist, making an exhaustive reference set impossible. For complex tasks, lexical and semantic similarity work better (AIE p.130).

## Key figures
None.

## Related
- [[reference-based-evaluation]]  (part-of: exact match is one of the three similarity-measurement techniques against reference data)
- [[lexical-similarity]]  (contrast: exact match requires identical text, whereas lexical similarity scores partial overlap on a sliding scale)
- [[semantic-similarity]]  (contrast: exact match compares surface text, whereas semantic similarity compares meaning)

## Provenance
- [[sources/ch03-similarity-measurements-against-reference-data]]
