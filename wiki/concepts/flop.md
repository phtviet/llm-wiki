---
type: concept
sources: [ch02-model-size]
---
# FLOP / FLOP/s

FLOP (floating point operation) is a standardized unit measuring the number of floating point operations performed for a task, used to quantify a model's compute requirement independent of specific hardware (AIE p.70). FLOP/s (floating point operations per second) instead measures a machine's peak performance, and is often confused with FLOPs in notation; some companies use FLOP/s-day to avoid ambiguity, where 1 FLOP/s-day = 86,400 FLOPs (AIE p.70).

Utilization measures how much of a machine's maximum compute capacity is actually used during training; 50% utilization is considered okay and above 70% is considered great (AIE p.70).

## Key figures
- Google's PaLM-2 was trained using 10^22 FLOPs; GPT-3-175B was trained using 3.14 × 10^23 FLOPs (AIE p.70)
- An NVIDIA H100 NVL GPU delivers up to 60 TeraFLOP/s (6 × 10^13 FLOPs/second, or 5.2 × 10^18 FLOPs/day) (AIE p.70)
- Training GPT-3-175B on 256 H100s at peak capacity would take ~236 days (~7.8 months) (AIE p.70)
- At 70% utilization and $2/hour per H100, training GPT-3-175B would cost over $4 million (AIE p.71)

## Examples
- None

## Related
- [[model-size]]  (part-of: FLOPs form the third of three numbers, alongside parameters and tokens, that signal model scale)
- [[chinchilla-scaling-law]]  (prerequisite: the scaling law optimizes model and dataset size for a fixed FLOP compute budget)

## Provenance
- [[sources/ch02-model-size]]
