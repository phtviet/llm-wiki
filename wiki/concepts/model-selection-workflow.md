---
type: concept
sources: [ch04-model-selection-workflow]
---
# Model Selection Workflow

The [[model-selection]] workflow is a four-step, iterative process for choosing which
model(s) to use for an application: (1) filter out models whose hard attributes don't
work for you, based on internal policies and whether you want commercial APIs or
self-hosted models; (2) use publicly available information such as benchmark
performance and leaderboard ranking to narrow down promising models to experiment
with, balancing quality, latency, and cost; (3) run experiments with your own
evaluation pipeline to find the best model, again balancing objectives; and (4)
continually monitor the model in production to detect failures and collect feedback
(AIE p.179-180).

The steps are iterative: a decision from an earlier step may be revisited in light of
later information. For example, a team might initially plan to host open source
models, but after public and private evaluation find that open source models can't
reach the desired performance level and switch to commercial APIs instead
(AIE p.180).

## Key figures
None.

## Examples
- [[hard-and-soft-attributes]]  (step 1 relies on classifying attributes as hard or soft)

## Related
- [[hard-and-soft-attributes]]  (prerequisite: filtering by hard attributes is the workflow's first step)
- [[model-build-versus-buy]]  (see-also: the API-vs-self-host question the workflow revisits at step 1)
- [[evaluation]]  (part-of: steps 2-4 of the workflow are forms of model evaluation)
- [[model-selection]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch04-model-selection-workflow]]
