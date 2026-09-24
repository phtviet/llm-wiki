---
type: concept
sources: [ch10-monitoring-and-observability]
---
# Drift Detection

Drift detection is the practice of catching changes in an AI system's behavior caused by shifts elsewhere in the system. The book identifies three sources of drift in an AI application: system prompt changes, user behavior changes, and underlying model changes (AIE p.470-472).

System prompt changes can happen without a team's direct knowledge -- a prompt template the system prompt was built on could be updated, or a coworker could fix a typo -- and can typically be caught with simple change-detection logic (AIE p.470-471).

User behavior changes occur as users adapt to a technology over time, similarly to how people learned to frame queries for better search results or, per Liu et al. (2020), how people in self-driving-car areas learned to bully the cars into yielding. Users may learn instructions that make responses more concise, causing a gradual drop in response length that metrics alone will not explain without further investigation (AIE p.471).

Underlying model changes happen when a [[model-api]]'s interface stays fixed but the model behind it is updated, sometimes without disclosure by the provider. Chen et al. (2023) observed notable benchmark-score differences between the March 2023 and June 2023 versions of [[gpt-4|GPT-4]] and GPT-3.5, and Voiceflow reported a 10% performance drop switching from GPT-3.5-turbo-0301 to GPT-3.5-turbo-1106 (AIE p.472).

## Key figures
- Voiceflow reported a 10% performance drop switching from GPT-3.5-turbo-0301 to GPT-3.5-turbo-1106 (AIE p.472)

## Related
- [[observability]]  (example-of: drift is a category of problem observability aims to surface)
- [[monitoring]]  (prerequisite: monitoring metrics are what first reveal a drift's symptoms)
- [[model-api]]  (see-also: mentioned in this page's text)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch10-monitoring-and-observability]]
