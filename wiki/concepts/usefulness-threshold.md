---
type: concept
sources: [ch01-milestone-planning]
---
# Usefulness Threshold

A usefulness threshold is a clear expectation of how good an AI product has to be before it is put in front of customers. It exists so a product isn't shipped before it's ready, and is typically defined by a group of metrics rather than a single number (AIE p.33).

Threshold metric groups include: quality metrics for the model's response quality; latency metrics such as TTFT (time to first token), TPOT (time per output token), and total latency, where acceptable latency depends on the use case (e.g., faster than an existing human median response time may already be good enough); cost metrics measured per inference request; and other metrics such as interpretability and fairness (AIE p.33).

## Key figures
None. The section illustrates latency and cost as metric categories without giving general load-bearing figures; the one concrete number in the section (an hour median human response time) is a hypothetical example, not a figure about the concept itself.

## Examples
- A customer-support chatbot compared against a human median response time of an hour, where any faster response may already clear the threshold (AIE p.33)

## Related
- [[milestone-planning]]  (prerequisite: setting a usefulness threshold precedes planning the milestones to reach it)
- [[evaluation]]  (part-of: quality metrics within the usefulness threshold are an evaluation task)

## Provenance
- [[sources/ch01-milestone-planning]]
