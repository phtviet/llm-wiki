---
type: entity
sources: [ch04-generation-capability]
---
# TruthfulQA

TruthfulQA is a benchmark for factual consistency, comprising questions that some humans would answer incorrectly due to false beliefs or misconceptions, spanning categories including health, law, finance, and politics (AIE p.168). It comes with a specialized AI judge, GPT-judge, finetuned to automatically evaluate whether a response is factually consistent with the reference response (AIE p.168). The paper "TruthfulQA: Measuring How Models Mimic Human Falsehoods" (Lin et al., 2022) reports GPT-judge predicts human-judged truthfulness with 90-96% accuracy (AIE p.166). GPT-4's technical report (2023) shows several models' performance on TruthfulQA; the human expert baseline reported in the TruthfulQA paper is 94% (AIE p.169).

## Key figures
- 817 questions across 38 categories (AIE p.168)
- GPT-judge predicts human-judged truthfulness with 90-96% accuracy (AIE p.166)
- Human expert baseline: 94% (AIE p.169)

## Related
- [[factual-consistency]]  (example-of: benchmark and judge built specifically to measure factual consistency)
- [[gpt-4]]  (see-also: GPT-4's technical report is the source of the book's TruthfulQA performance comparison)

## Provenance
- [[sources/ch04-generation-capability]]
