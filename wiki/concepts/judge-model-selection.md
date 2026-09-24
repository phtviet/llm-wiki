---
type: concept
sources: [ch03-what-models-can-act-as-judges]
---
# Judge Model Selection

When using [[ai-as-a-judge]], the judge can be stronger, weaker, or the same as the model being judged, and each choice trades off differently. A stronger judge can make better judgments and can help improve weaker models by guiding them toward better responses, but if a stronger model is already available, cost and latency often motivate using a cheaper or faster model to generate responses while reserving the stronger model to judge only a subset (e.g. a cheap in-house model generates responses while GPT-4 evaluates 1% of them) (AIE p.145). A fast model can also generate responses while a slower, stronger model judges in the background, triggering remedy actions (such as substituting the strong model's own response) when it flags a weak response as bad; the reverse pattern -- a strong generator with a weak background judge -- is also common (AIE p.145-146).

Using the strongest available model as judge creates two problems: the strongest model itself has no eligible judge, and an alternative method is needed to determine which model is strongest in the first place (AIE p.146). Whether a weaker model can judge a stronger one is an open question: some argue judging is easier than generating (anyone can have an opinion about a song without being able to write one), so weaker models should in principle be able to judge stronger ones. Zheng et al. (2023) found stronger models correlate better with human preference, pushing practitioners toward the strongest affordable judge, though that finding was limited to general-purpose judges (AIE p.146). Small, specialized judges -- trained on specific criteria and scoring systems -- are an active research direction and can be more reliable than larger general-purpose judges for specific judgments (AIE p.146).

## Key figures
None.

## Examples
- [[self-evaluation]]  (judge is the same model being judged)

## Related
- [[ai-as-a-judge]]  (part-of: judge-strength choice is a design decision within the AI-as-a-judge approach)
- [[self-evaluation]]  (example-of: same-model judging is one point on the stronger/weaker/same spectrum)
- [[ai-judge-bias]]  (boundary: self-bias is a specific risk that complicates same-model judging)
- [[lmsys-chatbot-arena]]  (see-also: Zheng et al.'s human-preference correlation finding relates to comparative human-judged leaderboards)

## Provenance
- [[sources/ch03-what-models-can-act-as-judges]]
