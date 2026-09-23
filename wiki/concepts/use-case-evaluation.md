---
type: concept
sources: [ch01-use-case-evaluation]
---
# Use Case Evaluation

Use case evaluation is the practice of deciding *why* and *how* to build an AI application before building it. The first question is why the application is worth building at all: building an AI application is typically a response to risks or opportunities, ranked from high to low: (1) an existential risk, where competitors using AI could make you obsolete; (2) a missed opportunity to boost profits and productivity; (3) uncertainty about where AI fits, but a fear of being left behind (AIE p.29). In the 2023 Gartner study, 7% of respondents cited business continuity (existential risk) as their reason for embracing AI, most common in document processing, information aggregation, and creative work (AIE p.29).

Once a good reason exists, the next question is whether to build the capability in-house or buy it: existential-risk use cases favor building in-house, while profit/productivity use cases often have viable buy options that save time and money (AIE p.29-30).

Evaluating a use case also means examining the role AI plays in the product, along three axes (drawing on an Apple framework): critical-or-complementary (does the app still work without AI), reactive-or-proactive (does AI respond to a user action or act opportunistically), and dynamic-or-static (is the AI feature updated continually per-user or only periodically) (AIE p.30). Finally, evaluation must consider the role of humans in the application -- whether AI supports human decisions, makes decisions directly, or both -- and the product's defensibility, since a thin layer built on top of a foundation model risks being subsumed if the underlying model's capabilities expand (AIE p.31).

## Key figures
- 7% of 2023 Gartner study respondents cited business continuity (existential risk) as their reason for embracing AI (AIE p.29)
- 95% acceptance-rate example: if human agents use AI-suggested responses verbatim 95% of the time for simple requests, customers can be let to interact with AI directly for those requests (AIE p.30)

## Examples
- [[human-in-the-loop]]  (framework for the role of humans in AI decision-making)
- [[ai-product-defensibility]]  (evaluating whether an AI product layer is defensible)

## Related
- [[human-in-the-loop]]  (part-of: clarifying humans' role in the application is one part of use case evaluation)
- [[ai-product-defensibility]]  (part-of: assessing defensibility is one part of evaluating a use case)
- [[milestone-planning]]  (see-also: both concern planning an AI product beyond the initial demo)
- [[competitive-advantage]]  (see-also: existential-risk reasoning and buy-vs-build overlap with sources of competitive advantage)

## Provenance
- [[sources/ch01-use-case-evaluation]]
