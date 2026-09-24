---
type: synthesis
sources: [ch04-model-build-versus-buy]
---
# Model Build Versus Buy

Since most companies won't build foundation models from scratch, "build versus buy" for them means choosing between using commercial [[model-api]]s or self-hosting an [[open-source-models|open source model]]. The book frames this as a decision across seven axes: data privacy, data lineage and copyright, performance, functionality, cost, control/access/transparency, and on-device deployment (AIE p.183).

**Data privacy.** Sending data to external model APIs risks leaks (e.g. Samsung employees leaking proprietary data into ChatGPT, leading to a company ban in May 2023) and risks the provider using submitted data to train its own models, as Zoom's 2023 terms-of-service change permitted. Self-hosting avoids sending data externally but offers fewer checks on data lineage (AIE p.184-185).

**Data lineage and copyright.** Most model developers disclose little about training data -- Google's Gemini technical report said only that data-enrichment workers were paid a living wage, and OpenAI's CTO could not clearly answer what data trained their models. IP law around AI is still evolving (the USPTO held in 2024 that AI-assisted inventions are not categorically unpatentable, but patentability depends on the significance of human contribution). Concerns over lineage push some companies toward fully open models whose data can be inspected, though inspecting a foundation-model-scale dataset is itself difficult; other companies instead prefer commercial models, since infringement claims are more likely to target the model's user than an open source model's developer, and commercial contracts can offer legal protection (AIE p.184-186).

**Performance.** The gap between open source and proprietary models on benchmarks like MMLU has been closing, but the book argues incentives favor keeping the strongest models proprietary: developers who have the best model are more likely to capitalize on it directly than open source it, and open models also lack the user feedback loop that improves commercial models in the wild (AIE p.185-186).

**Functionality.** Needed functionality includes scalability, function calling, structured outputs, and output guardrails. API providers often build these in, but restrict users to what the API exposes -- commonly limiting or omitting [[logprobs]] and finetuning access. Self-hosted open source models support full or partial finetuning and access to logprobs and intermediate outputs, at the cost of engineering effort (AIE p.186-188).

**Cost.** Model APIs charge per usage and can become prohibitively expensive at scale; self-hosting trades that for talent, time, and engineering cost to optimize, scale, and maintain an inference service (AIE p.188).

**Control, access, and transparency.** A 2024 a16z study found control and customizability are key reasons enterprises favor open source models. API users are subject to rate limits, risk losing access if a provider drops support or is banned (e.g. Italy's brief 2023 ban of OpenAI) or goes out of business, and face safety guardrails that can block legitimate use cases -- Convai, a 3D AI character company, hit this when commercial models refused physical-interaction responses and ended up finetuning open source models instead. Open source models can be frozen to preserve behavior, though the freezer is then responsible for maintaining that frozen service (AIE p.188-190).

**On-device deployment.** Third-party APIs cannot run on-device; only self-hosted or downloaded open source models can, which matters for offline use or for keeping data from leaving a device (AIE p.190).

The book concludes that these axes should substantially narrow a company's candidate model pool before further refinement using public performance data (AIE p.190-191).

## Related
- [[open-source-models]]  (part-of: openness of weights/data is a major input to the decision)
- [[model-licenses]]  (part-of: license terms constrain both commercial-use viability and distillation)
- [[model-api]]  (part-of: buying means consuming a commercial model API)
- [[inference-service]]  (part-of: building means self-hosting an inference service)
- [[logprobs]]  (boundary: a concrete functionality gap between many APIs and self-hosted models)
- [[mmlu]]  (evaluates: MMLU is used to illustrate the closing performance gap between open source and proprietary models)

## Provenance
- [[sources/ch04-model-build-versus-buy]]
