---
type: concept
sources: [ch08-data-curation]
---
# Tool Use Data

Although a model may intuitively know how to use certain tools from its pre-training knowledge, its tool-use ability improves when it is shown tool-use examples: prompts that are tasks requiring tool use, paired with responses that are the actions needed to perform them. Such data is commonly created by domain experts, who are asked what tasks they perform, how, and with what tools (AIE p.366).

Asking human experts to explain their process risks missing steps they consider unimportant or forget, so directly observing how humans perform tasks is often necessary for accuracy. But what is efficient for a human is not necessarily efficient for a model -- a human might use a web browser and copy a query into a search bar, whereas a model can call a search API directly and process all results at once -- so human annotations are often a poor fit for AI agents. As a result, many teams rely on simulation and other synthetic techniques to generate tool-use data instead (AIE p.366).

Tool use also requires a different conversational format than typical single-message turns: an AI turn may need to produce multiple messages, each sent to a different destination (e.g., one to a code interpreter, one to the user). Llama 3's authors (Dubey et al., 2024) designed a multi-message chat format with message headers specifying each message's source and destination, and special termination tokens marking where human and AI turns start (AIE p.366).

## Key figures
None.

## Examples
- Personal-assistant tool use data gathered by asking professional personal assistants what tasks, methods, and tools they use (AIE p.366)

## Related
- [[training-data-format-by-task]]  (part-of: one of the behavior-specific data types a model may need)
- [[data-synthesis]]  (see-also: synthetic and simulation techniques are commonly used to generate tool-use data since human annotation is a poor fit)
- [[llama-3]]  (example-of: its authors designed a multi-message chat format to support tool-use data)
- [[function-calling]]  (prerequisite: tool-use training data is what teaches a model the behavior that function calling exercises at inference time)

## Provenance
- [[sources/ch08-data-curation]]
