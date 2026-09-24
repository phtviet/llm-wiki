---
type: concept
sources: [ch06-tools]
---
# Knowledge Augmentation

Knowledge augmentation (also called context construction) is a category of agent tools that help augment an agent's knowledge of its environment. Examples include text retrievers, image retrievers, SQL executors, internal people search, an inventory API, Slack retrieval, and email readers, which give a model access to an organization's private processes and information (AIE p.279).

Knowledge-augmentation tools can also give models access to public information, especially from the internet, via [[web-browsing]]. Web browsing prevents a model from going stale: a model goes stale when the data it was trained on becomes outdated, so without web browsing it cannot answer questions requiring information newer than its training cutoff -- weather, news, upcoming events, stock prices, or flight status (AIE p.279). Web browsing is used as an umbrella term covering all tools that access the internet, including web browsers and specific APIs such as search APIs, news APIs, GitHub APIs, and social media APIs (e.g. X, LinkedIn, Reddit). While it lets an agent reference up-to-date information and reduce hallucination, it can also expose the agent to harmful internet content, so internet APIs should be selected with care (AIE p.279).

## Key figures
None.

## Examples
- [[web-browsing]]

## Related
- [[tool-inventory]]  (part-of: knowledge augmentation is one of three tool categories)
- [[context-construction]]  (see-also: knowledge augmentation is also called context construction)
- [[hallucination]]  (boundary: web browsing reduces but does not eliminate hallucination risk)

## Provenance
- [[sources/ch06-tools]]
