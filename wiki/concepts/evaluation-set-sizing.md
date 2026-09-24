---
type: concept
sources: [ch04-step-3-define-evaluation-methods-and-data]
---
# Evaluation Set Sizing

Evaluation set sizing is the question of how many examples an evaluation set needs to give reliable results while staying affordable to run (AIE p.206). A set that is too small can give results that swing wildly depending on which examples happen to be in it; a set that is too large becomes prohibitively expensive to evaluate against (AIE p.206).

One way to test whether a given evaluation set size is reliable is bootstrapping: repeatedly draw samples, with replacement, from the original evaluation set (matching its size), evaluate the model on each bootstrapped sample, and compare results across draws. If scores vary wildly across bootstraps (e.g. 90% on one, 70% on another), the evaluation pipeline is not trustworthy and needs a larger set (AIE p.206).

Evaluation set size also matters for comparing two systems (e.g. deciding whether a new prompt that scores 10% higher is genuinely better). In theory a statistical significance test can compute the needed sample size for a target confidence level from the true score distribution, but that distribution is rarely known in practice. OpenAI's rough estimation rule is that for every 3x decrease in the score difference to be detected, roughly 10x more samples are needed to remain 95% confident one system is better (AIE p.206-207).

As a reference point, among the benchmarks in Eleuther's lm-evaluation-harness, the median number of examples is 1,000 and the average is 2,159; the [[inverse-scaling]] prize organizers suggested 300 examples as an absolute minimum, preferring at least 1,000, especially for synthesized examples (McKenzie et al., 2023) (AIE p.207).

## Key figures
- OpenAI's rough estimate: detecting a 30% score difference needs ~10 samples for 95% confidence; 10% difference needs ~100; 3% difference needs ~1,000; 1% difference needs ~10,000 (AIE p.207)
- lm-evaluation-harness benchmarks: median 1,000 examples, average 2,159 examples (AIE p.207)
- Inverse Scaling prize guidance: 300 examples as absolute minimum, at least 1,000 preferred (AIE p.207)

## Examples
None.

## Related
- [[evaluation-guideline]]  (part-of: sizing the evaluation set is part of defining a workable evaluation pipeline)
- [[slice-based-evaluation]]  (see-also: both concern how evaluation data should be curated and sized for reliability)
- [[bigbench]]  (see-also: benchmark-scale example of curated evaluation examples referenced for sample-size context)
- [[inverse-scaling]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch04-step-3-define-evaluation-methods-and-data]]
