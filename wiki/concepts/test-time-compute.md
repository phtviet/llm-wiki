---
type: concept
sources: [ch02-sampling-fundamentals, ch02-test-time-compute]
---
# Test Time Compute

Test time compute is the strategy of spending extra inference-time computation to
improve a model's response quality, typically by generating multiple outputs per query
and selecting the best one rather than generating just one (AIE p.96). The name follows
existing literature even though it is applied to production inference, not just testing:
it is called test time compute because the number of outputs sampled is bounded by the
compute allocated to each inference call (AIE p.96).

Beyond naive independent sampling ([[best-of-n-sampling]]), a model can be more
strategic, e.g. using beam search to generate a fixed number of most-promising
candidates (the beam) at each generation step. Diversifying the sampled outputs --
often by varying sampling variables like [[temperature]] -- tends to increase the
chance of finding a good candidate (AIE p.96).

To pick the best output among several, options include: showing users all outputs and
letting them choose; selecting the output with the highest overall or average
[[logprobs]] (average is preferred, since raw summed logprobs bias toward shorter
sequences); scoring outputs with a [[reward-model]] or verifier; or applying
application-specific heuristics, such as preferring shorter responses or regenerating
until a syntactically valid output (e.g. valid SQL) is produced (AIE p.96-98).

Research is split on how far performance keeps improving with more samples. OpenAI
found gains only up to a point, after which performance dropped, hypothesized to be
due to adversarial outputs fooling the verifier; a separate Stanford study ("Monkey
Business", Brown et al., 2024) found the number of problems solved increasing
log-linearly from 1 to 10,000 samples. In practice, the author notes no production
system samples hundreds or thousands of outputs per input, since the cost would be
astronomical (AIE p.97-98).

## Key figures
- Generating two outputs costs approximately twice as much as generating one, on average (AIE p.96)
- OpenAI's verifier experiment: using a verifier boosted performance by roughly as much as a 30x model-size increase -- a 100-million-parameter model with a verifier could match a 3-billion-parameter model without one (AIE p.97)
- OpenAI found performance improved with more sampled outputs only up to about 400 outputs, after which it declined (AIE p.97)
- Stanford's "Monkey Business" study found problems solved increasing log-linearly as samples grew from 1 to 10,000 (AIE p.98)

## Examples
- [[best-of-n-sampling]]  (one method of test time compute: generate multiple, keep the reward-model-scored best)

## Related
- [[best-of-n-sampling]]  (part-of: best-of-N is one specific technique for doing test time compute)
- [[reward-model]]  (prerequisite: scoring-based selection of the best sampled output requires a trained reward model or verifier)
- [[logprobs]]  (part-of: average logprob is one selection method for choosing among sampled outputs)
- [[temperature]]  (see-also: varying sampling temperature is a common way to diversify outputs before selection)
- [[sampling]]  (part-of: test time compute is a strategy built on top of a model's per-token sampling behavior)

## Provenance
- [[sources/ch02-sampling-fundamentals]]
- [[sources/ch02-test-time-compute]]
