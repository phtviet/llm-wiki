---
type: concept
sources: [ch03-what-models-can-act-as-judges]
---
# Specialized AI Judges

Because AI judges can be used in many ways, many specialized judges exist, each trained to make a specific kind of judgment using specific criteria and scoring systems, rather than being a general-purpose model repurposed for evaluation (AIE p.146). The book groups them into three kinds: [[reward-model|reward models]], which score a (prompt, response) pair for how good the response is; reference-based judges, which compare a generated response against one or more reference responses to produce a similarity or quality score; and [[preference-model|preference models]], which take (prompt, response 1, response 2) and output which response is preferred (AIE p.146-147).

Reference-based judges output either a similarity score between candidate and reference, or a quality score for how good the generated response is relative to the reference (assuming the reference itself earns a top score) (AIE p.147). Preference models predict human preference directly, which is valuable because preference data is essential for aligning models to human preference yet challenging and expensive to collect firsthand; a good preference predictor can make evaluation easier and models safer (AIE p.147).

## Key figures
None. Model-specific figures (Cappy's parameter count, BLEURT's and Prometheus's score ranges) live on their entity pages.

## Examples
- [[cappy]]  (specialized reward model)
- [[bleurt]]  (reference-based judge)
- [[prometheus]]  (reference-based judge)
- [[pandalm]]  (preference model)

## Related
- [[ai-as-a-judge]]  (part-of: specialized judges are a refinement of the general AI-as-a-judge approach)
- [[reward-model]]  (part-of: reward models are one category of specialized judge)
- [[reference-based-evaluation]]  (part-of: reference-based judges implement reference-based evaluation)
- [[preference-model]]  (part-of: preference models are one category of specialized judge)
- [[criteria-ambiguity]]  (boundary: specialized judges can still disagree on scoring criteria, e.g. BLEURT's confusing score range)

## Provenance
- [[sources/ch03-what-models-can-act-as-judges]]
