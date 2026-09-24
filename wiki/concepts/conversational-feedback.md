---
type: concept
sources: [ch10-extracting-conversational-feedback]
---
# Conversational Feedback

Conversational feedback is [[user-feedback]] extracted from conversations with an AI application. It splits into explicit feedback (information given in direct response to a request, such as thumbs up/down, star ratings, or a yes/no answer to "Did we solve your problem?") and implicit feedback (information inferred from user actions, application-dependent since it hinges on what actions a user can take) (AIE p.475). Explicit feedback is standard across applications and therefore fairly well understood, but demands extra user effort and is prone to response bias: unhappy users are more likely to complain, skewing feedback negative. Implicit feedback is more abundant -- limited only by imagination -- but noisier and harder to interpret, since the same action (e.g. sharing a conversation) can be a positive or negative signal depending on the user (AIE p.479).

The conversational interface makes feedback easier to give: users can encourage good behavior and correct errors the same way they would in daily dialogue, so the language a user uses to direct the AI conveys both performance feedback and preference information (AIE p.475). Extracted conversational feedback serves three purposes: evaluation (deriving metrics to monitor the application), development (training or guiding future models), and personalization (tailoring the application to each user) (AIE p.476). Interpreting conversational cues reliably requires rigorous data analysis and user studies, not just intuition (AIE p.476).

The topic predates ChatGPT: the reinforcement learning community has tried to get RL algorithms to learn from natural language feedback since the late 2010s (Fu et al., 2019; Goyal et al., 2019; Zhou and Small, 2020; Sumers et al., 2020), and natural language feedback was studied for earlier conversational AI products such as Amazon Alexa, Spotify's voice control, and Yahoo! Voice (AIE p.476).

## Key figures
None. The concept itself carries no intrinsic load-bearing figure; the FITS clustering percentages are specific to that dataset and live on [[natural-language-feedback]].

## Examples
- [[natural-language-feedback]]  (feedback inferred from message content: early termination, error correction, complaints, sentiment)
- [[other-conversational-feedback]]  (feedback inferred from user actions: regeneration, conversation organization, length, diversity)

## Related
- [[natural-language-feedback]]  (part-of: feedback inferred from message content is one category of conversational feedback)
- [[other-conversational-feedback]]  (part-of: feedback inferred from user actions is the other category of conversational feedback)
- [[comparison-data]]  (see-also: user edits and post-regeneration comparisons produce winning/losing response pairs usable as comparison data for preference finetuning)
- [[human-in-the-loop]]  (see-also: both rely on user actions and input to steer or improve an AI system)
- [[user-feedback]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch10-extracting-conversational-feedback]]
