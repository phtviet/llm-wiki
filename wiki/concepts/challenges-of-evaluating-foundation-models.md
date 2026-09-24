---
type: concept
sources: [ch03-challenges-of-evaluating-foundation-models]
---
# Challenges of Evaluating Foundation Models

Evaluating foundation models is harder than evaluating traditional ML models for several distinct reasons. First, the more intelligent a model is, the harder its outputs are to check: few people can validate a PhD-level math solution or a coherent-but-wrong book summary, so evaluation of sophisticated tasks requires fact-checking, reasoning, and domain expertise rather than judging by how a response sounds (AIE p.114-115). Second, foundation models are open-ended, which undermines the traditional approach of comparing outputs against a curated list of ground truths: unlike a close-ended classification task, an open-ended task has too many possible correct responses to enumerate (AIE p.115). Third, most foundation models are treated as black boxes, since providers often withhold architecture, training data, and training-process details, or developers lack the expertise to interpret them, forcing evaluation to rely on observing outputs alone (AIE p.115). Fourth, public evaluation benchmarks saturate quickly as models improve, requiring frequent replacement (AIE p.115-116). Last, general-purpose models expand the scope of evaluation beyond measuring performance on known trained tasks -- evaluation must also discover new tasks a model can do, including tasks beyond human capabilities (AIE p.116).

Despite these challenges prompting a fast-growing body of new evaluation methods and benchmarks, investment in evaluation lags behind investment in modeling, training, and AI orchestration tooling, leading to inadequate infrastructure and ad hoc practices such as eyeballing results or relying on a small, personally curated set of go-to prompts (AIE p.116-117).

## Key figures
- LLM-evaluation papers grew from about 2 per month to almost 35 per month over the first half of 2023 (AIE p.116)
- Over 50 of the top 1,000 AI-related GitHub repositories (by stars, as of May 2024) were dedicated to evaluation (AIE p.116)
- GLUE (2018) became saturated within a year, prompting SuperGLUE (2019); NaturalInstructions (2021) was replaced by SuperNaturalInstructions (2022); MMLU (2020) was largely replaced by MMLU-Pro (2024) (AIE p.115-116)

## Examples
- [[benchmark-saturation]]

## Related
- [[evaluation]]  (part-of: this concept enumerates why the broader activity of evaluation is difficult for foundation models)
- [[ai-as-a-judge]]  (see-also: subjective automatic-evaluation approach rising partly in response to these challenges)
- [[foundation-model]]  (boundary: the open-ended, black-box, general-purpose nature of foundation models is what drives these evaluation difficulties, unlike task-specific traditional ML models)

## Provenance
- [[sources/ch03-challenges-of-evaluating-foundation-models]]
