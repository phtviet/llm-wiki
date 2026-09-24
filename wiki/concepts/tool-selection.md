---
type: concept
sources: [ch06-planning]
---
# Tool Selection

Because tools often play a crucial role in a task's success, tool selection requires careful consideration. The right set of tools depends on the environment and task, and also on the AI model powering the agent; there is no foolproof selection guide (AIE p.295). More tools give an agent more capability but make efficient tool use harder -- similar to how a large toolset is harder for a human to master -- and adding tools grows the tool descriptions that must fit in the model's context (AIE p.295).

Recommended practices for choosing tools include: comparing agent performance across different tool sets; running ablation studies to see how much performance drops if a tool is removed (removing tools that cost nothing to drop); identifying tools the agent frequently misuses and changing them if extensive prompting or finetuning can't fix the problem; and plotting the distribution of tool calls to see which tools are most and least used (AIE p.295-296).

Experiments by Lu et al. (2023) using Chameleon show that different tasks require different tools (e.g. ScienceQA relies far more on knowledge retrieval than the tabular-math task TabMWP) and that different models have different tool preferences ([[gpt-4|GPT-4]] selects a wider tool set and favors knowledge retrieval, while ChatGPT favors image captioning) (AIE p.296). Chameleon also proposes studying tool transition -- after using tool X, how likely is the agent to call tool Y -- so that frequently co-used tools can be combined into a single more powerful tool (AIE p.297). Voyager (Wang et al., 2023) proposes a skill manager that tracks new skills (tools, each a coding program) an agent creates, adding successful ones to a skill library for later reuse on other tasks (AIE p.297).

## Key figures
None.

## Examples
None.

## Related
- [[agent]] (prerequisite: an agent's success depends on its tool inventory alongside its planning capability)
- [[function-calling]] (prerequisite: selected tools are invoked via function calling)
- [[agent-efficiency]] (see-also: tool-count and tool-quality choices affect an agent's efficiency)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch06-planning]]
