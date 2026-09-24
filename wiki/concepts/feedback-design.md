---
type: concept
sources: [ch10-feedback-design]
---
# Feedback Design

Feedback design is the practice of deciding when and how an AI application collects [[user-feedback]], so that collection is valuable to the product without disrupting the user's workflow. Feedback should be collectable throughout the user journey, and the option to give it -- especially to report errors -- should be nonintrusive (AIE p.480).

Particularly valuable moments to collect feedback include: at the beginning of use, to calibrate the application for a new user (e.g. a face ID scan, a voice-assistant wake-word sample, a language-learning skill check); when something bad happens, such as a hallucination, a blocked legitimate request, or a slow response, so users can downvote, regenerate, switch models, or hand off to a human; and when the model has low confidence, where showing multiple candidate outputs side by side lets the user's choice serve as a comparative signal usable for [[preference-finetuning]] (AIE p.481-483).

Good feedback should also seamlessly integrate into the user's workflow, be easy to ignore, and carry an incentive for users to give it thoughtfully. Explaining to users how their feedback will be used (personalization, aggregate statistics, or model training) can motivate better-quality feedback (AIE p.486-487). Design missteps -- ambiguous rating scales, confusing icon choices, or asking users to judge things they can't evaluate (e.g. a statistical answer presented as a preference choice) -- produce noisy or unreliable feedback (AIE p.487-488). Whether a feedback signal is shown publicly or kept private also changes user behavior: private signals tend to produce more candid, higher-quality feedback, but reduce discoverability and explainability of recommendations built on them (AIE p.489).

## Key figures
None. The figures in this section belong to specific companies' feedback mechanisms rather than to feedback design as a general concept.

## Examples
- [[midjourney]]  (four-image generation with upscale/variation/regenerate options as implicit feedback)
- [[github-copilot]]  (lighter-colored draft suggestions accepted via Tab or ignored by continued typing)
- [[google-gemini]]  (partial side-by-side responses for comparative feedback)
- [[google-photos]]  (asks for confirmation when uncertain whether two faces match)

## Related
- [[conversational-feedback]]  (part-of: feedback design determines when/how the explicit and implicit signals described there get collected)
- [[comparative-evaluation]]  (see-also: side-by-side low-confidence outputs generate comparative signals usable the same way as comparative evaluation data)
- [[preference-finetuning]]  (prerequisite: comparative user feedback signals can feed preference finetuning)
- [[data-flywheel]]  (part-of: well-designed feedback collection is how a product's own usage data becomes a flywheel)
- [[user-feedback]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch10-feedback-design]]
