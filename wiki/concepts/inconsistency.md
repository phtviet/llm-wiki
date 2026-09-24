---
type: concept
sources: [ch02-the-probabilistic-nature-of-ai]
---
# Inconsistency

Inconsistency is when a model generates very different responses for the same or slightly different prompts (AIE p.106). It manifests in two scenarios: (1) same input, different outputs -- the same prompt run twice produces two very different responses; and (2) slightly different input, drastically different outputs -- a minor change, such as accidentally capitalizing a letter, produces a very different response (AIE p.106). The book illustrates scenario 1 with an essay-scoring example where the same prompt to ChatGPT produced scores of 3/5 and 5/5 on two runs (AIE p.106).

Inconsistency creates a jarring user experience, since users expect a level of consistency comparable to human-to-human communication (AIE p.106). For the same-input scenario, mitigations include caching the answer, fixing sampling variables such as [[temperature]], [[top-p-sampling]], and [[top-k-sampling]], and fixing the random seed used for token sampling (AIE p.106). Even with all variables fixed, the hardware running generation can still affect output, since different machines execute instructions and handle numeric ranges differently; hosting your own model gives some control over this, while using a model API provider leaves this control with the provider (AIE p.106-107). Fixing generation settings does not guarantee 100% consistency and does not by itself inspire trust in the system (AIE p.106-107). The second scenario -- slightly different input -- is harder to fix; it is helped by careful prompting and by memory systems, but fixing generation variables alone won't force identical outputs across different inputs (AIE p.107).

## Key figures
- Same essay-scoring prompt produced scores of 3/5 and 5/5 on two separate runs of ChatGPT (AIE p.106)

## Examples
- ChatGPT essay-scoring example, same prompt scored 3/5 then 5/5 (AIE p.106)

## Related
- [[probabilistic-nature-of-ai]]  (part-of: inconsistency is a manifestation of the model's probabilistic sampling)
- [[hallucination]]  (contrast: inconsistency is about varying outputs across runs; hallucination is about a single output being ungrounded in fact)
- [[temperature]]  (prerequisite: fixing this sampling variable is one mitigation for same-input inconsistency)
- [[top-p-sampling]]  (prerequisite: fixing this sampling variable is one mitigation for same-input inconsistency)
- [[top-k-sampling]]  (prerequisite: fixing this sampling variable is one mitigation for same-input inconsistency)

## Provenance
- [[sources/ch02-the-probabilistic-nature-of-ai]]
