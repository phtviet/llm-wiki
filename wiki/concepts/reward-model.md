---
type: concept
sources: [ch02-preference-finetuning]
---
# Reward Model

A reward model takes a (prompt, response) pair and outputs a scalar score for how good the response is; it is the scoring component that RLHF optimizes against (AIE p.84). Directly asking labelers to score responses ([[pointwise-evaluation]]) yields inconsistent scores, so reward models are instead trained on [[comparison-data]]: labelers rank or compare pairs of responses, and only the ranking is used for training, even when concrete 1-7 scores are also collected (AIE p.85-86).

The training objective, as used by [[instructgpt]], maximizes the difference between the reward model's scores for the winning response and the losing response for a given prompt, via a sigmoid-based log-loss formulation: for training tuple (x, yw, yl), the loss is -log(sigma(r(x,yw) - r(x,yl))), minimized in expectation over all samples (AIE p.86).

A reward model can be trained from scratch or finetuned on top of another model, such as the pre-trained or SFT model; finetuning on top of the strongest [[foundation-model]] tends to give the best performance (AIE p.87). Some believe the reward model must be at least as powerful as the foundation model it scores, but the book notes evidence (developed in the evaluation chapter) that a weaker model can judge a stronger one, since judging is believed easier than generation (AIE p.87).

## Key figures
None. Figures describing the underlying labeling process (cost, time, agreement) belong to [[comparison-data]].

## Examples
- None named as a specific reward model instance in this section.

## Related
- [[rlhf]]  (prerequisite: RLHF's first stage is training the reward model)
- [[comparison-data]]  (prerequisite: reward models are trained on comparison-labeled data rather than direct scores)
- [[preference-finetuning]]  (part-of: the reward model is the mechanism through which preference finetuning operationalizes human preference)
- [[pointwise-evaluation]]  (see-also: mentioned in this page's text)
- [[foundation-model]]  (see-also: mentioned in this page's text)
- [[instructgpt]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-preference-finetuning]]
