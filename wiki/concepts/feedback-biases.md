---
type: concept
sources: [ch10-feedback-limitations]
---
# Feedback Biases

[[user-feedback]] carries systematic biases that must be understood and designed around, since each application's feedback has its own patterns (AIE p.490). The section identifies four:

**Leniency bias** is the tendency to rate items more positively than warranted, often to avoid conflict or because it is the easiest option. On a five-star scale, users may feel pressured toward five stars, reserving four for when something goes wrong. Uber found that in 2015 the average driver rating was 4.8, with scores below 4.6 putting drivers at risk of deactivation; despite the bias, the rating system still differentiated good drivers from bad ones. Removing the strong negative connotation of low numeric ratings (e.g. replacing 1-5 stars with descriptive phrases) can help surface more granular feedback (AIE p.490).

**Randomness** occurs when users give feedback without real motivation to be thoughtful, such as clicking one of two long side-by-side responses at random rather than reading both, or randomly picking an image to generate variations from (AIE p.490-491).

**Position bias** is the tendency for the position an option is shown in to affect how it is perceived; users are more likely to click the first suggestion regardless of its quality. It can be mitigated by randomly varying suggestion positions or by modeling a suggestion's position-adjusted true success rate (AIE p.491).

**Preference bias** covers biases such as preferring a longer response in a side-by-side comparison even when it is less accurate, since length is easier to notice than inaccuracy, and recency bias, where people favor the answer they see last (AIE p.491).

## Key figures
- Uber's 2015 average driver rating was 4.8, with scores below 4.6 risking driver deactivation (AIE p.490)

## Related
- [[conversational-feedback]]  (part-of: these biases affect feedback collected through conversational and other user-facing signals)
- [[degenerate-feedback-loop]]  (boundary: biases distort individual feedback signals, while a degenerate loop is the compounding effect of acting on biased feedback over time)
- [[feedback-design]]  (prerequisite: understanding these biases should inform how a feedback system is designed)
- [[user-feedback]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch10-feedback-limitations]]
