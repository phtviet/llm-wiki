---
type: concept
sources: [ch04-evaluation-criteria]
---
# Evaluation-Driven Development

Evaluation-driven development is the practice of defining evaluation criteria before building an AI application, named by analogy to test-driven development in software engineering, which writes tests before writing code (AIE p.160). The approach follows from a business observation: an application deployed without any way to know whether it works is worse than one never deployed at all, since it still costs money to maintain, and even more to take down, while its value remains unmeasured (AIE p.160).

Sensible business decisions still favor applications with clear, measurable evaluation criteria: recommender systems (measured by engagement or purchase-through rate increases), fraud detection (measured by money saved from prevented fraud), coding (measured by [[functional-correctness]] of generated code), and close-ended tasks like intent classification, sentiment analysis, and next-action prediction, which are much easier to evaluate than open-ended generation (AIE p.160-161).

The approach has a acknowledged limitation: focusing only on applications whose outcomes can be measured is like looking for a lost key under a lamppost at night — easier to search there, but not where the key necessarily is. This risks missing potentially game-changing applications that lack an easy evaluation method. The author frames evaluation as the biggest bottleneck to AI adoption, arguing that reliable evaluation pipelines will unlock new applications otherwise avoided for being hard to measure (AIE p.161).

## Key figures
None.

## Examples
- [[customer-support-chatbot]]  (companies deployed these en masse after ChatGPT's launch while remaining unsure whether they helped or hurt user experience)

## Related
- [[evaluation]]  (prerequisite: evaluation-driven development requires defining evaluation criteria, which is a subset of the broader evaluation problem)
- [[functional-correctness]]  (example-of: coding is a common generative AI use case because generated code can be scored via functional correctness)
- [[evaluation-driven-risk-mitigation]]  (see-also: both frame evaluation as central to why AI applications succeed or fail)

## Provenance
- [[sources/ch04-evaluation-criteria]]
