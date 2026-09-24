---
type: concept
sources: [ch04-model-build-versus-buy]
---
# Open Source, Open Weight, and Open Model

"Open source model" originally meant any model people could download and use, but the term is now contentious. Some argue a model should only count as open if its training data is also public, since a model's performance is largely a function of its training data. Open data enables retraining from scratch with architecture or data modifications, easier auditing (e.g. checking for compromised or illegally acquired data), and greater transparency (AIE p.181).

To disambiguate, "open weight" refers to models whose weights are public but training data is not, while "open model" refers to models whose training data is also public. As of writing, the vast majority of open source models are open weight only -- developers often withhold training data details to avoid public scrutiny and lawsuits. This book uses "open source" loosely to mean any model whose weights are public, regardless of data availability or license (AIE p.181-182).

## Key figures
None.

## Examples
- [[llama-2]]  (open weight only; Llama 2 Community License)
- [[llama-3]]  (open weight only; Llama 3 Community License)

## Related
- [[model-licenses]]  (prerequisite: openness of weights/data is one factor a license governs)
- [[model-build-versus-buy]]  (part-of: open-vs-proprietary status is a key input to the build-vs-buy decision)

## Provenance
- [[sources/ch04-model-build-versus-buy]]
