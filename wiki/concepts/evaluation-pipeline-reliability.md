---
type: concept
sources: [ch04-step-3-define-evaluation-methods-and-data]
---
# Evaluation Pipeline Reliability

Evaluation pipeline reliability is the practice of evaluating the evaluation pipeline itself, not just the AI system it evaluates, to improve trustworthiness and efficiency (AIE p.207). This matters especially for subjective methods such as [[ai-as-a-judge]], where scores can be noisy or inconsistent (AIE p.207).

The book poses four questions to assess an evaluation pipeline's quality: whether it produces the right signals (do better responses get higher scores, and do better metrics correspond to better business outcomes); how reliable it is (does rerunning the same pipeline, or running it on different evaluation datasets, change the results — the goal is high reproducibility and low variance, e.g. setting an AI judge's temperature to 0 for consistency); how correlated its metrics are (perfectly correlated metrics are redundant, while uncorrelated metrics may reveal either a genuine model insight or an untrustworthy metric); and how much [[cost-and-latency]] the pipeline itself adds to the application, since skipping evaluation to save latency is described as a risky bet (AIE p.207-208).

Evaluation criteria and pipelines are also expected to iterate over time as needs and user behavior change, but should retain enough consistency that results remain usable to guide development; experiment tracking should log every variable that can change, including evaluation data, rubric, and judge prompt/sampling configuration (AIE p.208).

## Key figures
None.

## Examples
None.

## Related
- [[ai-as-a-judge]]  (prerequisite: judge reliability, e.g. fixing temperature to 0, is a specific case this practice addresses)
- [[benchmark-selection-and-aggregation]]  (see-also: metric correlation concerns raised here echo the aggregation-benchmark discussion)
- [[evaluation-guideline]]  (part-of: reliability checking is part of designing and maintaining an evaluation pipeline)
- [[cost-and-latency]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch04-step-3-define-evaluation-methods-and-data]]
