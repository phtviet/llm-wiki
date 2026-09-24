---
type: concept
sources: [ch04-navigate-public-benchmarks]
---
# Data Contamination

Data contamination (also called data leakage, training on the test set, or cheating) happens when a model was trained on the same data it is evaluated on. A contaminated model may simply memorize answers rather than demonstrate real capability, inflating its evaluation scores; a model trained directly on MMLU can score well on MMLU without being useful (AIE p.197).

Contamination is usually unintentional: models trained on internet-scraped data can accidentally ingest benchmark data published before training, which is also why benchmarks saturate quickly and developers keep creating new ones. It can also happen indirectly, when training data and benchmark data are drawn from the same source (e.g. the same textbook), or intentionally, when a developer continues training a selected best model on benchmark data before release to boost performance, even though this then contaminates that benchmark for future evaluation (AIE p.197-198).

Rylan Schaeffer's satirical 2023 paper 'Pretraining on the Test Set Is All You Need' demonstrated the effect starkly: a one-million-parameter model trained exclusively on several benchmarks' data achieved near-perfect scores, outperforming much larger models on those benchmarks (AIE p.197).

Detection relies on two heuristics: n-gram overlap (checking whether a long token sequence, e.g. 13 tokens, from an evaluation sample also appears in training data) and perplexity (unusually low perplexity on evaluation data suggests the model has seen it before). N-gram overlap is more accurate but expensive and requires training-data access; perplexity is less accurate but far cheaper (AIE p.198-199).

Because foundation-model developers rarely control or disclose full training data, older ML advice to simply remove evaluation samples from training data is hard to apply, and there will always be benchmarks created after a model's training cutoff. A common practice is for developers to remove benchmarks they specifically care about from training data beforehand, and ideally disclose contamination percentages and both contaminated and clean-sample performance. OpenAI's analysis of GPT-3 found 13 benchmarks with at least 40% of their data present in GPT-3's training data (Brown et al., 2020). Leaderboard hosts like Hugging Face plot standard deviations of model performance on a benchmark to spot contamination outliers (AIE p.199).

## Key figures
- A 1-million-parameter model trained on benchmark data achieved near-perfect scores, outperforming much larger models (AIE p.197)
- N-gram overlap detection example: a 13-token overlapping sequence marks an evaluation sample as dirty (AIE p.198)
- OpenAI found 13 benchmarks with at least 40% of their data in GPT-3's training set (AIE p.199)

## Examples
- [[gpt-4]]  (GPT-3.5/GPT-4 performance shifts between March and June 2023 raised contamination-adjacent questions about model updates)

## Related
- [[benchmark-selection-and-aggregation]]  (boundary: contamination undermines trust in public benchmark scores regardless of how well they're selected or aggregated)
- [[perplexity]]  (prerequisite: perplexity-based contamination detection relies on the general perplexity metric)
- [[benchmark-saturation]]  (see-also: contamination is one driver of benchmarks becoming saturated quickly)
- [[mmlu]]  (example-of: a model trained directly on MMLU can score well without being genuinely capable)

## Provenance
- [[sources/ch04-navigate-public-benchmarks]]
