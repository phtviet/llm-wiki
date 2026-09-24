---
type: concept
sources: [ch05-context-length-and-context-efficiency]
---
# Needle in a Haystack (NIAH) Test

Needle in a haystack (NIAH) is a test for evaluating how effectively a model uses different parts of a long prompt. It works by inserting a random piece of information (the needle) at different locations within a long prompt (the haystack) and asking the model to find it (Liu et al., 2023) (AIE p.218). Results from Liu et al.'s paper show all tested models performed much better at finding the needle when it was closer to the beginning or end of the prompt than in the middle (AIE p.218-219).

The original test used a randomly generated string, but real questions and answers can substitute for it — for example, asking a model to recall a drug mentioned in a long doctor-visit transcript, or a patient's blood type (AIE p.219). Test information should be private and not present in the model's training data; otherwise the model may answer from memorized internal knowledge rather than from the prompt's context, invalidating the test (AIE p.219). A similar test, RULER (Hsieh et al., 2024), can also evaluate how well a model processes long prompts (AIE p.219).

## Key figures
None. The test's results (relative performance by position) are qualitative in this section; no load-bearing number is given beyond the context-length figures that live on [[context-length]].

## Related
- [[context-length]]  (prerequisite: NIAH is used to evaluate how a model uses positions within its available context length)
- [[data-contamination]]  (boundary: test information must be private/unseen or the model may rely on memorized training data instead of context)
- [[prompt-engineering]]  (part-of: NIAH informs best practices for structuring prompts)

## Provenance
- [[sources/ch05-context-length-and-context-efficiency]]
