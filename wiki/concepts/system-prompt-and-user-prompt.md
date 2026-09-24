---
type: concept
sources: [ch05-system-prompt-and-user-prompt]
---
# System Prompt and User Prompt

Many model APIs let a prompt be split into a system prompt and a user prompt: the system prompt can be thought of as the task description, and the user prompt as the task itself. Typically, instructions from application developers go into the system prompt, while instructions or data from end users go into the user prompt, though developers can be creative and move instructions between the two (AIE p.215).

A common pattern is [[roleplaying]]: a real-estate-disclosure chatbot might carry 'You're an experienced real estate agent...' as its system prompt, with the uploaded disclosure and the user's question in the user prompt. Almost all generative AI applications, including ChatGPT, use system prompts (AIE p.215).

Given a system prompt and a user prompt, the model concatenates them into a single final prompt, typically following the model's [[chat-template]]; from the model's perspective the two are processed identically (AIE p.217). Any performance boost a system prompt provides is therefore attributed to one or both of: it comes first in the final prompt, and models may be better at processing leading instructions; or the model was post-trained to pay more attention to the system prompt specifically, as in OpenAI's [[instruction-hierarchy]] work, which also helps mitigate [[prompt-attacks]] (AIE p.217).

## Key figures
None.

## Examples
- Real-estate disclosure chatbot: roleplaying instruction in the system prompt, disclosure and question in the user prompt (AIE p.215)

## Related
- [[chat-template]]  (prerequisite: the model combines system and user prompts using its chat template)
- [[instruction-hierarchy]]  (see-also: post-training to prioritize the system prompt is one explanation for its performance boost)
- [[prompt-structure]]  (see-also: both concern how a prompt's parts are composed and ordered)
- [[prompt-engineering]]  (part-of: system/user prompt splitting is a mechanism within prompt engineering)
- [[prompt-attacks]]  (see-also: mentioned in this page's text)
- [[roleplaying]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch05-system-prompt-and-user-prompt]]
