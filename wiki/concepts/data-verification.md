---
type: concept
sources: [ch08-ai-powered-data-synthesis]
---
# Data Verification

Data verification is the process of checking the quality of (typically synthetic) training data, using the same tools used to evaluate other AI outputs: functional correctness and AI judges (AIE p.391). Coding data is especially popular to synthesize because it can be functionally verified by execution; most of Llama 3's synthetic training data is coding-related for this reason (AIE p.391).

For data that can't be verified by functional correctness, AI verifiers -- a general-purpose AI judge or a specialized scorer -- can assign a 1-5 quality score or classify examples as good/bad against stated quality requirements (AIE p.392). Factual-consistency detection can filter out likely hallucinations. Creative verification approaches include training an AI content detector (if real vs. synthetic data is easy to distinguish, the synthetic data is weak), training an acceptance classifier against a target quality bar (e.g. predicting NeurIPS acceptance), topic-relevance filtering, and anomaly detection for outliers (AIE p.392). Heuristic filters -- removing empty, too-short, too-long, repetitive, or duplicate-instruction examples -- are also common; the Self-Instruct authors (Wang et al., 2022) used exactly these heuristics (AIE p.392-393). Ultimately, the real test of synthetic data quality is whether it improves real-world model performance (AIE p.393).

## Key figures
None.

## Related
- [[data-synthesis]] (prerequisite: synthetic data should be verified before being used for training)
- [[functional-correctness]] (example-of: functional correctness is one verification method applied to synthetic data)
- [[ai-as-a-judge]] (example-of: AI judges are used as general-purpose data verifiers)

## Provenance
- [[sources/ch08-ai-powered-data-synthesis]]
