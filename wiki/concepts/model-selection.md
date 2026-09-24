---
type: concept
sources: [ch04-model-selection]
---
# Model Selection

Model selection is the process of evaluating models against the criteria defined for a specific application, since the goal is not the best model overall but the best model for the application at hand (AIE p.179). Model selection recurs throughout [[application-development]]: as a team progresses through different adaptation techniques, it must re-select models at each stage. For example, [[prompt-engineering]] might start with the strongest available model to evaluate feasibility, then work backward to see if smaller models suffice, while [[finetuning]] might start with a small model to validate code before moving toward the biggest model that fits hardware constraints, such as a single GPU (AIE p.179).

In general, the selection process for a given technique involves two steps: first, figuring out the best achievable performance; second, mapping models along cost-performance axes and choosing the model that gives the best performance for the cost. The book notes the actual process is more nuanced than these two steps suggest (AIE p.179).

## Key figures
None.

## Related
- [[model-selection-workflow]]  (part-of: the four-step iterative filtering/benchmarking/experimenting/monitoring process is a fuller elaboration of this two-step selection process)
- [[model-build-versus-buy]]  (prerequisite: choosing between commercial APIs and self-hosted open source models is itself a model-selection decision)
- [[prompt-engineering]]  (example-of: illustrates starting from the strongest model and working backward during selection)
- [[finetuning]]  (example-of: illustrates starting from a small model and scaling up during selection)
- [[application-development]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch04-model-selection]]
