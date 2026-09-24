---
type: concept
sources: [ch05-system-prompt-and-user-prompt]
---
# Chat Template

A chat template is the format a model's developers define for combining a system prompt and a user prompt into the single final prompt actually fed into the model. It is defined by the model developers and usually documented alongside the model; it differs from a prompt template, which any application developer can define to hydrate prompts with specific data (AIE p.216).

Different models use different chat templates, and the same provider can change the template between versions. Llama 2's chat template wraps the system prompt in `<<SYS>>` tags and the whole exchange in `[INST]` tags; Llama 3 replaced this with `<|start_header_id|>` / `<|end_header_id|>` role markers, where each `<|...|>` span is treated as a single token (AIE p.216).

Accidentally using the wrong template, or making small formatting mistakes such as an extra newline, can cause a model's performance to significantly degrade -- though deviations from the expected template have, uncommonly, also been reported to improve performance. Template mismatches are common when using third-party prompt-construction tools, and are hard to spot because they cause silent failures: the model still produces a reasonable-looking response even with a broken template. Recommended practice is to follow the model's chat template exactly, verify any third-party tool uses the correct template, and print the final prompt before sending it to check conformance (AIE p.216-217).

## Key figures
None.

## Examples
- [[llama-2]]  (chat template: `<s>[INST] <<SYS>>{{ system_prompt }}<</SYS>>{{ user_message }} [/INST]`)
- [[llama-3]]  (chat template: `<|begin_of_text|><|start_header_id|>system<|end_header_id|>...`)

## Related
- [[system-prompt-and-user-prompt]]  (prerequisite: the chat template is how system and user prompts get combined into one final prompt)
- [[llama-2]]  (example-of: uses `<<SYS>>`/`[INST]` template tags)
- [[llama-3]]  (example-of: uses `<|start_header_id|>` role-marker template, changed from Llama 2's)
- [[token]]  (boundary: special template spans like `<|begin_of_text|>` are treated as single tokens despite containing multiple characters)

## Provenance
- [[sources/ch05-system-prompt-and-user-prompt]]
