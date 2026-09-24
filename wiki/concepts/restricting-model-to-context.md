---
type: concept
sources: [ch05-provide-sufficient-context]
---
# Restricting a Model's Knowledge to Only Its Context

In many scenarios it is desirable for a model to respond using only information provided in its context, rather than drawing on its broader training knowledge. This is especially common for roleplaying and simulations: a model playing a character in a fictional universe should only know about that universe, not answer unrelated real-world questions (AIE p.223).

Achieving this reliably is difficult. Clear instructions -- such as telling the model to answer using only the provided context, paired with examples of questions it shouldn't answer -- can help, as can instructing the model to quote where in the corpus its answer comes from, nudging it toward context-supported answers (AIE p.224). Since there is no guarantee a model follows all instructions, prompting alone may not reliably produce the desired outcome. Finetuning a model on a specific corpus is another option, but pre-training data can still leak into its responses. The safest method is training a model exclusively on the permitted corpus of knowledge, though this is often infeasible -- the corpus may also be too limited to train a high-quality model (AIE p.224).

## Key figures
None.

## Examples
- Roleplaying a Skyrim character that should not answer questions like 'What's your favorite Starbucks item?' (AIE p.223)

## Related
- [[context-construction]]  (prerequisite: needs constructed context to restrict the model to)
- [[finetuning]]  (contrast: an alternative, imperfect route to restriction, since pre-training data can still leak through)
- [[roleplaying]]  (example-of: a common use case motivating context-only restriction)
- [[hallucination]]  (boundary: restricting to context reduces but does not guarantee elimination of ungrounded answers)

## Provenance
- [[sources/ch05-provide-sufficient-context]]
