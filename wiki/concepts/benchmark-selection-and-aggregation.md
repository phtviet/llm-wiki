---
type: concept
sources: [ch04-navigate-public-benchmarks]
---
# Benchmark Selection and Aggregation

Building a leaderboard from public benchmarks requires answering two questions: which benchmarks to include, and how to aggregate their results into a ranking. With thousands of benchmarks available, it is impossible to examine them all, and models can rank differently across benchmarks measuring different things (e.g. coding vs. toxicity), making the choice of what to include and how to weigh it consequential (AIE p.191).

Public leaderboards balance coverage against compute cost. Compute constraints force most leaderboards to use only a small subset of benchmarks: HELM Lite excluded MS MARCO for cost reasons, and Hugging Face opted out of [[humaneval]] due to its heavy compute requirements. Hugging Face's Open LLM Leaderboard started with four benchmarks in 2023, grew to six by year end, and was overhauled again in June 2024 with a harder, more practical benchmark set (replacing GSM-8K with MATH lvl 5 and MMLU with MMLU-PRO, and adding GPQA, MuSR, BBH, and [[ifeval]]) as the old set saturated. Stanford's HELM Leaderboard used ten benchmarks at the same time Hugging Face used six, with only MMLU and GSM-8K shared between them, reflecting no clear standard for what 'coverage' means (AIE p.192-194).

Aggregation methods also diverge: Hugging Face averaged scores across benchmarks, treating each equally regardless of difficulty or relevance, while HELM used mean win rate -- the fraction of times a model beats another model, averaged across scenarios -- instead of averaging (AIE p.195).

Benchmark correlation matters for selection: strongly correlated benchmarks are redundant and can exaggerate biases. Among Hugging Face's six benchmarks (measured January 2024), ARC-C, MMLU, and WinoGrande were strongly correlated (all testing reasoning), while TruthfulQA was only moderately correlated with the others, suggesting reasoning/math improvements don't reliably improve truthfulness (AIE p.194).

For a specific application, the same process applies at smaller scale: gather benchmarks relevant to the target capability (e.g. code benchmarks for a coding agent), check benchmark reliability, and favor recent, unsaturated benchmarks. A model that ranks well on a general public leaderboard will often, but not always, perform well for a specific application (AIE p.195).

## Key figures
- Hugging Face's Open LLM Leaderboard began with 4 benchmarks (2023), expanded to 6 by year end, then was replaced with a new set in June 2024 (AIE p.192-194)
- HELM Leaderboard used 10 benchmarks, only 2 (MMLU, GSM-8K) overlapping with Hugging Face's 6 (AIE p.193)
- ARC-C/MMLU correlation: 0.8672; MMLU/WinoGrande: 0.9011; ARC-C/WinoGrande: 0.8856; TruthfulQA correlations range roughly 0.42-0.55 with the others (AIE p.194)
- Stanford spent approximately $80,000-$100,000 to evaluate 30 models on the full HELM suite ($38,000 for commercial APIs plus 19,500 GPU hours for open models) (AIE p.196)

## Examples
- [[helm]]  (Stanford's holistic leaderboard, ten benchmarks, mean win rate aggregation)
- [[hugging-face-open-llm-leaderboard]]  (Hugging Face's leaderboard, averaging six then a revised benchmark set)

## Related
- [[evaluation-harness]]  (prerequisite: running many candidate benchmarks at scale depends on a harness)
- [[benchmark-saturation]]  (boundary: saturation is why leaderboards must periodically replace their benchmark sets)
- [[data-contamination]]  (see-also: public benchmark scores can be misleading independent of selection, due to contamination)
- [[model-selection]]  (part-of: benchmark selection and aggregation is how public benchmarks feed into narrowing candidate models)
- [[mmlu]]  (example-of: MMLU is a benchmark commonly included in these leaderboards, later replaced by MMLU-PRO)
- [[truthfulqa]]  (example-of: TruthfulQA is one of the benchmarks whose correlation with others was analyzed)
- [[humaneval]]  (see-also: mentioned in this page's text)
- [[ifeval]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch04-navigate-public-benchmarks]]
