---
type: concept
sources: [ch04-instruction-following-capability]
---
# Instruction-Following Capability

Instruction-following capability measures how well a model does what it's told, independent of whether the instructions themselves are good and independent of the model's domain-specific capability. A model can understand a task (e.g. tweet sentiment) yet fail to follow the output instruction (e.g. outputting HAPPY/ANGRY instead of the requested NEGATIVE/POSITIVE/NEUTRAL), showing good domain-specific capability but poor instruction-following (AIE p.172). It is essential for applications needing structured outputs (JSON, regex-conforming text) but extends beyond structure to constraints like vocabulary limits or content/style rules. When a model performs poorly, the cause can be an incapable model or a badly written instruction, which makes evaluation ambiguous: a model that fails to write a lục bát poem may not know the form, or may not understand the request at all (AIE p.172-173).

Benchmarks differ in how broadly they define instruction-following. [[ifeval]] restricts itself to automatically verifiable formatting instructions, while [[infobench]] also covers content constraints, linguistic guidelines, and style rules that resist automated verification (AIE p.173-174). Because these public benchmarks' instruction sets are incomplete and unrepresentative of any given real-world use, the book recommends curating a custom benchmark using an application's own required instructions and criteria (AIE p.175).

## Key figures
None.

## Examples
- [[ifeval]] (automatically verifiable formatting instructions)
- [[infobench]] (broader criteria including content, linguistic, and style constraints)
- [[roleplaying]] (common real-world instruction type)

## Related
- [[domain-specific-capability]] (boundary: poor output can stem from either weak domain knowledge or weak instruction-following, and the two are easily conflated)
- [[structured-outputs]] (prerequisite: generating structured output requires the model to follow the format instruction given)
- [[instructgpt]] (example-of: named as the model finetuned specifically to follow instructions)
- [[evaluation-driven-development]] (see-also: motivates curating instruction-following benchmarks tailored to an application)

## Provenance
- [[sources/ch04-instruction-following-capability]]
