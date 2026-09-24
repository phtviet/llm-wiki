---
type: concept
sources: [ch02-model-size]
---
# FLOP and FLOP/s

FLOP (floating point operation) measures the number of floating point operations performed for a task, and is a standardized way to express a model's compute requirement independent of specific hardware (AIE p.70). FLOPs (plural) measures total compute required for a task, while FLOP/s (floating point operations per second) measures a machine's peak performance -- the two are easily confused, and some companies use 'FLOP/s-day' to avoid the ambiguity (1 FLOP/s-day = 86,400 FLOPs) (AIE p.70).

Utilization measures how much of a machine's maximum compute capacity is actually used in practice; roughly 50% utilization is considered okay and above 70% is considered great (AIE p.71).

## Key figures
- Google's PaLM-2 was trained using 10^22 FLOPs; GPT-3-175B was trained using 3.14 x 10^23 FLOPs (AIE p.70)
- An NVIDIA H100 NVL GPU delivers up to 60 TeraFLOP/s (6 x 10^13 FLOPs/second, 5.2 x 10^18 FLOPs/day) (AIE p.70)
- Training GPT-3-175B on 256 H100s at peak capacity would take ~236 days (~7.8 months) (AIE p.70)
- At 70% utilization and $2/hour per H100, training GPT-3-175B would cost over $4 million (AIE p.71)

## Related
- [[model-size]]  (part-of: FLOPs is one of three numbers, alongside parameters and training tokens, that signal a model's scale)
- [[scaling-law]]  (prerequisite: compute budget in FLOPs is the fixed constraint the scaling law optimizes model/dataset size against)

## Provenance
- [[sources/ch02-model-size]]
