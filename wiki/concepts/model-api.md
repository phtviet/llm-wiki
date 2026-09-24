---
type: concept
sources: [ch04-model-build-versus-buy]
---
# Model API

A model API is the interface users interact with to access a model's [[inference-service]]. The term is typically used for the inference service's API specifically, though model developers also expose other services such as finetuning APIs and evaluation APIs. Model APIs can be offered by model providers (OpenAI, Anthropic), cloud providers (Azure, GCP), or third-party API providers (Databricks Mosaic, Anyscale). The same model can be available through multiple APIs with different features, constraints, and pricing -- for example [[gpt-4|GPT-4]] is available via both OpenAI and Azure, and performance can differ slightly between them since providers may optimize the model differently (AIE p.183-184).

Commercial models are accessible only via APIs licensed by their developers, whereas open source models can be served by any API provider, letting users pick a provider on price or features. Because API providers without their own models compete on the API itself, they may be more motivated to offer better pricing and functionality. Many API providers mimic OpenAI's API format to ease model swapping (AIE p.184, p.187-188).

A commonly cited limitation is that many providers restrict or withhold [[logprobs]] out of concern that exposing them would let others replicate the model (AIE p.187).

## Key figures
None.

## Related
- [[inference-service]]  (part-of: the model API is the interface exposed by an inference service)
- [[model-build-versus-buy]]  (part-of: using a model API is one side of the build-vs-buy decision)
- [[logprobs]]  (boundary: model APIs often limit or omit logprobs even though they are useful for classification, evaluation, and interpretability)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch04-model-build-versus-buy]]
