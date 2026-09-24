---
type: concept
sources: [ch03-what-models-can-act-as-judges]
---
# Self-Evaluation

Self-evaluation (also called self-critique or self-ask) is using a model to judge its own output (AIE p.146). It can seem like cheating, especially given self-bias, but it is useful for sanity checks: if a model judges its own response as incorrect, that is itself a signal the model may be unreliable. Beyond sanity checks, prompting a model to critique itself can nudge it to revise and improve its response (Press et al., 2022; Gou et al., 2023; Valmeekamet et al., 2023) (AIE p.146). A simple example: asked '10+3?', a model answers '30', is prompted 'Is this answer correct?', and revises to 'No it's not. The correct answer is 13' (AIE p.146).

## Key figures
None.

## Related
- [[judge-model-selection]]  (example-of: self-evaluation is the same-model case of the stronger/weaker/same judge spectrum)
- [[ai-judge-bias]]  (boundary: self-bias limits how much self-evaluation should be trusted beyond sanity checks)
- [[ai-as-a-judge]]  (part-of: self-evaluation is a mode of using a model as a judge)

## Provenance
- [[sources/ch03-what-models-can-act-as-judges]]
