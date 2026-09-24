---
type: concept
sources: [ch02-sampling-strategies]
---
# Logprobs

Logprobs, short for log probabilities, are the probabilities a model computes for tokens expressed on the log scale. Log scale is preferred when working with a neural network's probabilities because it helps reduce the underflow problem, where a number too small to be represented in a given format gets rounded down to zero (AIE p.93). A language model might work with a vocabulary size of 100,000, so probabilities for many tokens can be too small to represent without this transform (AIE p.93).

Logprobs are useful for building applications (especially classification), evaluating applications, and understanding how models work under the hood. As of the book's writing, many model providers don't expose their models' logprobs, or expose only a limited API, likely for security reasons: exposed logprobs make a model easier for others to replicate (AIE p.93). OpenAI's API, for instance, only shows the logprobs of up to the 20 most likely tokens and discontinued arbitrary logprob access in September 2023; Anthropic doesn't expose its models' logprobs at all (AIE p.93).

## Key figures
- Vocabulary size example of 100,000 tokens, illustrating the underflow risk without log scale (AIE p.93)
- OpenAI API exposes logprobs for only the top 20 most likely tokens, having discontinued arbitrary logprob access in September 2023 (AIE p.93)

## Related
- [[logit-vector]]  (prerequisite: logprobs are derived from the same logits, via softmax then a log transform)
- [[softmax]]  (prerequisite: probabilities are computed from logits by softmax before being expressed as logprobs)
- [[sampling]]  (part-of: logprobs expose the probability distribution that sampling draws from)

## Provenance
- [[sources/ch02-sampling-strategies]]
