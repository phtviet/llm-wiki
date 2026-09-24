---
type: concept
sources: [ch08-data-acquisition-and-annotation]
---
# Data Annotation

Data annotation is often necessary to produce data for finetuning when acquired data lacks labels or responses. It is challenging not only because of the annotation process itself but because of the difficulty of creating clear annotation guidelines: guidelines must explicitly state what a good response looks like and what makes it good, including edge cases like whether a correct-but-unhelpful response counts, and what distinguishes adjacent scores on a rubric. Annotation guidelines are needed for both manual and AI-powered annotation. Some teams, including LinkedIn, have reported that writing annotation guidelines was among the most challenging parts of their AI engineering pipeline, and teams sometimes abandon careful annotation partway through due to the time and effort required, hoping models will learn correct responses on their own instead -- a risky bet for many applications (AIE p.379).

Annotation guidelines are the same as those used for evaluation data, which is an argument for investing more time in curating evaluation guidelines and data: good evaluation examples can then be reused, augmented, or used as seed examples to synthesize new training data (AIE p.379-380).

## Key figures
None.

## Related
- [[data-acquisition]] (part-of: annotation is one of the acquisition methods alongside sourcing, purchasing, and synthesizing)
- [[evaluation-guideline]] (see-also: annotation guidelines and evaluation guidelines are described as the same kind of specification)
- [[data-synthesis]] (prerequisite: evaluation examples can serve as seed examples for synthesizing new data)

## Provenance
- [[sources/ch08-data-acquisition-and-annotation]]
