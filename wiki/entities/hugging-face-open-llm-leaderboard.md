---
type: entity
sources: [ch04-navigate-public-benchmarks]
---
# Hugging Face Open LLM Leaderboard

Hugging Face's Open LLM Leaderboard is a public model leaderboard that launched in 2023 with four benchmarks, expanded to six by the end of that year (ARC-C, MMLU, HellaSwag, TruthfulQA, WinoGrande, GSM-8K), and ranked models by averaging scores across them. Hugging Face stated the benchmarks were chosen because they test 'a variety of reasoning and general knowledge across a wide variety of fields,' guided informally by which benchmarks then-popular models used. In June 2024 the leaderboard was overhauled with a harder, more practical set: GSM-8K was replaced by MATH lvl 5, MMLU by MMLU-PRO, and GPQA, MuSR, BBH, and IFEval were added, as the original six had become saturated or nearly so (AIE p.192-194).

## Key figures
- Started with 4 benchmarks (2023), expanded to 6 by year end, replaced with a new set in June 2024 (AIE p.192, p.194)
- Correlation among its original six benchmarks (Jan 2024): ARC-C/MMLU 0.8672, MMLU/WinoGrande 0.9011, ARC-C/WinoGrande 0.8856, TruthfulQA vs. others roughly 0.42-0.55 (AIE p.194)

## Related
- [[benchmark-selection-and-aggregation]]  (example-of: worked case of averaging-based leaderboard aggregation and benchmark churn)
- [[helm]]  (contrast: six/revised benchmarks and averaging vs. HELM's ten benchmarks and mean win rate)
- [[benchmark-saturation]]  (example-of: the 2024 overhaul was driven by saturation of the original six benchmarks)

## Provenance
- [[sources/ch04-navigate-public-benchmarks]]
