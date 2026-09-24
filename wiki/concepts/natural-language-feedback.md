---
type: concept
sources: [ch10-extracting-conversational-feedback]
---
# Natural Language Feedback

Natural language feedback is conversational feedback extracted from the content of user messages. Useful signals to track in production include: early termination (a user stops a response generation halfway, exits the app, tells a voice assistant to stop, or leaves the agent hanging), which likely signals the conversation isn't going well; and error correction, where a user's follow-up starts with "No, ..." or "I meant, ...", or rephrases their request, indicating the model's prior response missed the mark (AIE p.476-477).

Users can also give action-correcting feedback pointing out specific mistakes (e.g. "Bill is the suspect, not the victim"), which is especially common in agentic use cases where users nudge an agent toward different actions (e.g. "Check the CEO's X profile"). Requests for explicit confirmation ("Are you sure?", "Check again", "Show me the sources") may signal that answers lack sufficient detail or that the user distrusts the model, even when the model isn't wrong (AIE p.477).

Some applications let users directly edit a model's response (e.g. editing generated code), which is a strong signal the original output wasn't quite right. User edits are also a valuable source of preference data: each edit forms a (query, winning response, losing response) example, with the original generation as the losing response and the edited version as the winning response, usable to align a model to human preference via preference finetuning (AIE p.477).

Complaints are another signal: users may state an answer is wrong, irrelevant, toxic, lengthy, lacking detail, or just bad, without attempting a correction. Automatic clustering of the FITS (Feedback for Interactive Talk & Search) dataset (Xu et al., 2022; results from Yuan et al., 2023) identified eight groups of natural language feedback (AIE p.478). Complaints can also appear as general negative sentiment (e.g. "Uggh") without stated reasons; tracking sentiment across a conversation, similar to how call centers track rising voice volume, can reveal how well a bot is performing. Natural language feedback can also be read from the model's own responses -- a high refusal rate (e.g. "Sorry, I don't know that one") likely signals user dissatisfaction (AIE p.478).

## Key figures
- FITS dataset clustering identifies 8 feedback-type groups; the largest, "clarify their demand again," accounts for 3,702 examples (26.54%), and the smallest, "complain about repetition/rudeness," accounts for 137 examples (0.99%) (AIE p.478)

## Examples
None.

## Related
- [[conversational-feedback]]  (part-of: natural language feedback is the message-content category of conversational feedback)
- [[other-conversational-feedback]]  (contrast: inferred from message content vs. inferred from user actions)
- [[comparison-data]]  (example-of: a user's edited response paired with the original generation forms a comparison-data example for preference finetuning)
- [[preference-finetuning]]  (prerequisite: comparison data derived from user edits feeds into preference finetuning)

## Provenance
- [[sources/ch10-extracting-conversational-feedback]]
