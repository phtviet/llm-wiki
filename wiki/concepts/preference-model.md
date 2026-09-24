---
type: concept
sources: [ch03-summary]
---
# Preference Model

A preference model is a specialized AI judge trained to predict which of two responses a
human user would prefer. It was motivated by the fact that both comparative evaluation
and the post-training alignment process (RLHF) need preference signals, and collecting
those signals from humans is expensive; a preference model supplies this signal
automatically (AIE p.156).

## Key figures
None.

## Examples
None given in this section.

## Related
- [[reward-model]]  (see-also: both are AI judges trained on comparison data to predict human preference; reward-model is used specifically to guide RLHF optimization)
- [[comparative-evaluation]]  (prerequisite: comparative evaluation and RLHF alignment both require preference signals, which preference models supply cheaply)
- [[ai-as-a-judge]]  (part-of: a preference model is a specialized kind of AI judge)
- [[rlhf]]  (prerequisite: RLHF's alignment process needs the same preference signals a preference model predicts)

## Provenance
- [[sources/ch03-summary]]
