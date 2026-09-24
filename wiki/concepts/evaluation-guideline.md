---
type: concept
sources: [ch04-step-2-create-an-evaluation-guideline]
---
# Evaluation Guideline

An evaluation guideline is a clear, unambiguous specification of what an AI application should and shouldn't do, used to produce reliable evaluation scores. Creating this guideline is considered the most important step of the evaluation pipeline: an ambiguous guideline leads to ambiguous scores that can be misleading, and if you don't know what a bad response looks like, you can't catch it. The guideline must define not just desired behavior but out-of-scope inputs -- for example, whether a customer support chatbot should answer questions unrelated to the product -- along with how to detect such inputs and how the application should respond (AIE p.202).

A guideline is built around evaluation criteria: dimensions along which a response is judged good or bad. A correct response is not always a good response -- LinkedIn found that for their AI-powered Job Assessment application, 'You are a terrible fit' might be correct but unhelpful, since a good response should explain the gap between job requirements and the candidate's background and how to close it. LangChain's State of AI 2023 report found users applied 2.3 different feedback criteria on average to evaluate an application. For a customer support application, three example criteria are relevance (relevant to the user's query), factual consistency (consistent with the context), and safety (not toxic). Criteria are typically derived by testing real user queries, generating multiple responses, and judging them good or bad (AIE p.202).

For each criterion, a scoring system must be chosen -- binary, a 1-5 scale, a 0-1 continuous range, or another scheme (for factual consistency, some teams use binary 0/1, others use -1/0/1 for contradiction/neutral/entailment). Given a scoring system, a rubric with concrete examples should be written for each score value and validated with humans; if people find the rubric hard to follow, it must be refined until unambiguous. This guideline can later be reused for training [[data-annotation]] (AIE p.202-203).

Finally, evaluation metrics should be tied to business metrics: understanding what a given evaluation score means for the business (e.g. what proportion of support requests can be automated at a given factual-consistency level) helps decide where to invest improvement effort, and feeds into setting a [[usefulness-threshold]]. Business metrics themselves often split into stickiness metrics (DAU/WAU/MAU) and engagement metrics (conversations per month, visit duration), and prioritizing them can create tension between revenue and user well-being, since stickiness/engagement optimization can favor addictive features or extreme content (AIE p.203).

## Key figures
- LangChain's State of AI 2023: users applied an average of 2.3 different feedback criteria per application (AIE p.202)
- Illustrative business-metric mapping: factual consistency of 80% -> automate 30% of requests; 90% -> automate 50%; 98% -> automate 90% (AIE p.203)

## Examples
- customer support chatbot criteria: relevance, factual consistency, safety

## Related
- [[evaluation]]  (part-of: guideline creation is a step within designing an evaluation pipeline)
- [[usefulness-threshold]]  (prerequisite: business-metric mapping informs setting a usefulness threshold)
- [[evaluation-driven-development]]  (see-also: both frame evaluation criteria as defined before or alongside building the application)
- [[factual-consistency]]  (example-of: factual consistency is one criterion the guideline can define, with scoring-system choices shown here)
- [[customer-support-chatbot]]  (example-of: the book's running example used to illustrate criteria and business-metric mapping)
- [[data-annotation]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch04-step-2-create-an-evaluation-guideline]]
