---
type: concept
sources: [ch02-test-time-compute]
---
# Test Time Compute

Test time compute is the strategy of generating multiple responses per query at inference time, instead of just one, to increase the chance of getting a good response (AIE p.96). The term follows existing literature's use of 'test time' to mean inference, even though the technique applies to production models generally, not just testing; it is called test time compute because the number of outputs sampled is bounded by how much compute is allocated to each inference call (AIE p.96).

A simple way to improve effectiveness is to increase output diversity, e.g. by varying the model's sampling variables across generations, since a more diverse candidate set is more likely to contain a good response (AIE p.96). Generating multiple outputs is expensive: generating two outputs costs roughly twice as much as generating one (AIE p.96).

After generating candidates, a selection method picks the final output: highest average logprob, a reward model or verifier score, application-specific heuristics (e.g. shortest response, or first valid SQL query), or the most common output across samples ([[self-consistency]]) (AIE p.97-99). DeepMind argues that scaling test time compute can be more efficient than scaling [[model-parameters]], and asks how much a fixed non-trivial inference-time compute budget can improve performance on a hard prompt (Snell et al., 2024) (AIE p.97). OpenAI found using a verifier gave a performance boost comparable to a 30x [[model-size]] increase (Cobbe et al., 2021) (AIE p.97).

Sampling more outputs helps only up to a point in some experiments, after which performance can decrease as adversarial outputs that fool the verifier become more likely to appear; a separate Stanford study found problems solved increasing log-linearly from 1 to 10,000 samples (Brown et al., 2024) (AIE p.98). In production, sampling hundreds or thousands of outputs per input is not practical due to cost (AIE p.98). Test time compute is also used to address latency: generating multiple responses in parallel and showing the user the first valid one to finish (AIE p.99).

## Key figures
- Generating two outputs costs approximately twice as much as generating one (AIE p.96)
- Using a verifier gave a performance boost roughly equivalent to a 30x model size increase (a 100M-parameter model with a verifier performing on par with a 3B-parameter model without one) (AIE p.97)
- In OpenAI's experiment, performance improved with more sampled outputs up to 400 outputs, then decreased (AIE p.97)
- A Stanford study found problems solved increased log-linearly as samples grew from 1 to 10,000 (AIE p.98)
- Google sampled 32 outputs per question when evaluating Gemini on MMLU, achieving a higher score than with one output (AIE p.99)

## Examples
- [[best-of-n]]  (generate multiple outputs, pick the one scored best)
- [[beam-search]]  (strategic generation of a fixed set of promising candidates)
- [[self-consistency]]  (pick the most common output among samples)
- [[gemini-mmlu-prompting-comparison]]  (Google sampling 32 outputs per MMLU question)

## Related
- [[best-of-n]]  (part-of: best-of-N is one way to do test time compute, generating outputs independently and picking the best)
- [[reward-model]]  (see-also: a reward model or verifier is one method for selecting the best sampled output)
- [[logprobs]]  (see-also: average logprob across a sequence is one method for selecting the best sampled output)
- [[sampling]]  (prerequisite: test time compute builds on sampling multiple whole outputs, extending single-token sampling choices)
- [[beam-search]]  (contrast: strategic fixed-beam generation vs. generating many independent candidates)
- [[model-parameters]]  (see-also: mentioned in this page's text)
- [[model-size]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-test-time-compute]]
