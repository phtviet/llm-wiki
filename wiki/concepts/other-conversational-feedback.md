---
type: concept
sources: [ch10-extracting-conversational-feedback]
---
# Other Conversational Feedback (Action-Based)

Other conversational feedback covers signals derived from user actions rather than message content. Regeneration -- a user requesting another response, sometimes from a different model -- may signal dissatisfaction with the first response, or simply a desire to compare options (common for creative requests like image or story generation). Regeneration signals tend to be stronger in usage-based-billing applications than subscription ones, since users are less likely to regenerate out of idle curiosity when it costs money. Some applications explicitly ask users to compare the new response against the previous one after a regeneration; this better-or-worse data can be used for [[preference-finetuning]] (AIE p.478-479).

Conversation organization actions -- delete, rename, share, bookmark -- also carry signal. Deleting a conversation is usually a strong negative signal (unless the user is removing an embarrassing exchange); renaming suggests the conversation itself was good but the auto-generated title was not (AIE p.479).

Conversation length (number of turns) is ambiguous on its own: a long conversation may indicate enjoyment for an AI companion application, but inefficiency for a productivity-oriented application like customer support. Length is best interpreted together with dialogue diversity (measured by distinct token or topic count) -- a long conversation with little diversity may mean the user is stuck in a repetitive loop with the bot (AIE p.479-480).

## Key figures
None.

## Examples
None.

## Related
- [[conversational-feedback]]  (part-of: action-based feedback is the other category of conversational feedback, alongside natural language feedback)
- [[natural-language-feedback]]  (contrast: inferred from user actions vs. inferred from message content)
- [[comparison-data]]  (example-of: explicit post-regeneration comparisons produce winning/losing response pairs usable as comparison data)
- [[conversational-bots]]  (see-also: conversation length and diversity signals are especially relevant for companion and customer-support bots)
- [[preference-finetuning]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch10-extracting-conversational-feedback]]
