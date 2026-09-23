---
type: concept
sources: [ch02-the-probabilistic-nature-of-ai]
---
# Inconsistency

Inconsistency is when a model generates very different responses for the same or slightly different prompts (AIE p.106). It manifests in two scenarios: (1) the same input produces different outputs across separate calls, and (2) a slightly different input -- even a single capitalized letter -- produces a drastically different output (AIE p.106). The book's example: asking ChatGPT to score the same essay twice returned 3/5 one time and 5/5 the next (AIE p.106).

For the same-input case, mitigations include caching answers, fixing sampling variables such as [[temperature]], [[top-p-sampling]], and [[top-k-sampling]], and fixing the random seed used for token sampling. Even with all variables fixed, consistency is not guaranteed 100% of the time, since the hardware executing the model can also affect output, and hosted API providers (e.g., OpenAI, Google) control that hardware, not the developer (AIE p.106). The slightly-different-input case is harder: fixing generation settings does not force identical outputs across different prompts, though carefully crafted prompts and a memory system can bring responses closer to what's wanted (AIE p.106).

## Key figures
- ChatGPT essay-scoring example: same prompt scored 3/5 on one run and 5/5 on another (AIE p.106)

## Related
- [[probabilistic-nature-of-ai]]  (part-of: inconsistency is a direct consequence of probabilistic sampling)
- [[hallucination]]  (contrast: inconsistency stems from sampling randomness alone, whereas hallucination has more nuanced causes beyond randomness)
- [[temperature]]  (prerequisite: fixing temperature is one mitigation for same-input inconsistency)
- [[top-p-sampling]]  (prerequisite: fixing top-p is one mitigation for same-input inconsistency)
- [[top-k-sampling]]  (prerequisite: fixing top-k is one mitigation for same-input inconsistency)

## Provenance
- [[sources/ch02-the-probabilistic-nature-of-ai]]
