---
type: entity
sources: [ch04-navigate-public-benchmarks]
---
# HELM (Holistic Evaluation of Language Models)

HELM is Stanford's leaderboard project for evaluating language models. Its 'HELM Lite' variant used ten benchmarks -- including MATH, LegalBench, MedQA, WMT 2014, NarrativeQA, OpenBookQA, and two settings of Natural Questions -- of which only MMLU and GSM-8K overlapped with Hugging Face's six-benchmark leaderboard at the same time. HELM Lite excluded the MS MARCO information-retrieval benchmark because it was too expensive to run. Rather than averaging benchmark scores like Hugging Face, HELM ranks models by mean win rate: the fraction of times a model scores better than another model, averaged across scenarios (AIE p.192-195).

## Key figures
- HELM Lite uses 10 benchmarks, sharing only 2 (MMLU, GSM-8K) with Hugging Face's leaderboard (AIE p.193)
- Stanford spent approximately $80,000-$100,000 to evaluate 30 models on the full HELM suite ($38,000 commercial API costs plus 19,500 GPU hours for open models) (AIE p.196)

## Related
- [[benchmark-selection-and-aggregation]]  (example-of: HELM is a worked case of leaderboard benchmark selection and mean-win-rate aggregation)
- [[hugging-face-open-llm-leaderboard]]  (contrast: ten benchmarks and mean win rate vs. six/updated benchmarks and averaging)

## Provenance
- [[sources/ch04-navigate-public-benchmarks]]
