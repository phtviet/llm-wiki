---
type: concept
sources: [ch10-feedback-limitations]
---
# Degenerate Feedback Loop

A degenerate feedback loop arises in a system where [[user-feedback]] modifies a model's behavior, and the model's own predictions then influence the feedback it receives, which in turn influences the next iteration of the model, amplifying initial biases (AIE p.491). Also known as exposure bias, popularity bias, or filter bubbles, this is a well-studied problem (AIE p.491).

In a video-recommendation example, videos ranked higher get shown first, so they receive more clicks, which reinforces the system's belief that they are the best picks; a minor initial ranking edge can compound until one video dominates and others never surface. The same mechanism can narrow a product's focus and user base: if a small number of users give positive feedback on cat photos, the system generates more cat photos, attracting cat lovers who reinforce the pattern further, until the application skews entirely toward cats — and the same mechanism can instead amplify biases such as racism, sexism, or a preference for explicit content (AIE p.491).

Acting on user feedback can also push a conversational agent toward sycophancy: training a model on user feedback can teach it to give users what they want to hear rather than what is accurate or beneficial (Stray, 2023). Sharma et al. (2023) show that AI models trained on human feedback tend toward sycophancy, becoming more likely to present responses matching the user's own view (AIE p.491-492).

## Key figures
None.

## Related
- [[feedback-biases]]  (prerequisite: a degenerate loop compounds biases already present in individual feedback signals)
- [[conversational-feedback]]  (boundary: feedback is inherently incomplete, since it is only collected on what is shown to users, which is a precondition for the loop)
- [[rlhf]]  (see-also: both involve training on human/user feedback signals, with sycophancy as a shared risk)
- [[user-feedback]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch10-feedback-limitations]]
