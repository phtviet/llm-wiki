---
type: concept
sources: [ch05-break-complex-tasks-into-simpler-subtasks]
---
# Prompt Decomposition

Prompt decomposition (breaking complex tasks into simpler subtasks) splits a multi-step task into separate subtasks, each with its own prompt, which are then chained together. For example, a customer support chatbot can decompose responding to a request into intent classification followed by response generation conditioned on the identified intent; with ten possible intents, this requires ten different response prompts (AIE p.224).

How small each subtask should be is use-case dependent, traded off against performance, cost, and latency; the right decomposition and chaining requires experimentation. Models are improving at following complex instructions but still perform better with simpler ones, so decomposition tends to improve performance (AIE p.226).

Benefits beyond raw performance include: monitoring intermediate outputs as well as the final one; debugging, since a failing step can be isolated and fixed independently; parallelization of independent steps (e.g. generating three reading-level versions of a story simultaneously); and effort, since simple prompts are easier to write than complex ones (AIE p.226).

Decomposition has costs. It can increase perceived latency, especially when users don't see intermediate outputs, since more steps mean a longer wait before the final step's first output token. It also typically increases the number of model queries, though total cost need not double, since smaller prompts often use fewer tokens and simpler steps can route to cheaper models (e.g. a weaker model for intent classification, a stronger one for response generation) (AIE p.226).

## Key figures
None. The concept carries no intrinsic load-bearing figure of its own; GoDaddy's prompt-length figure is a use-case illustration, not a general property of decomposition.

## Examples
- [[customer-support-chatbot]]  (intent classification then response generation, decomposed into per-intent prompts)

## Related
- [[prompt-engineering]]  (part-of: decomposition is a prompt engineering technique for complex tasks)
- [[structured-outputs]]  (see-also: the intent classification example outputs JSON, combining decomposition with format control)
- [[cost-and-latency]]  (boundary: decomposition can raise perceived latency and query count even as it may cut per-step token cost)

## Provenance
- [[sources/ch05-break-complex-tasks-into-simpler-subtasks]]
