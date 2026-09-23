---
type: concept
sources: [ch01-from-foundation-models-to-ai-engineering]
---
# AI Engineering

AI engineering is the process of building applications on top of existing foundation models, as distinct from traditional ML engineering, which involves developing the models themselves (AIE p.12). Three factors together create the conditions for its rapid growth: foundation models' general-purpose capabilities let a single model support many more applications than a task-specific model could; the success of ChatGPT triggered a sharp rise in AI investment from venture capitalists and enterprises; and the model-as-a-service approach (models exposed via APIs) plus AI's own ability to write code lowers the barrier to building AI applications, since it removes the need to host and serve a model or even to write much code (AIE p.13-14).

The author chose the term "AI engineering" over alternatives like MLOps, AIOps, or LLMOps because the "Ops" suffix implies an operational focus, while the discipline is more about engineering (tweaking) foundation models to do what is wanted; "ML engineering" was rejected because working with foundation models differs from working with traditional ML models in important ways (AIE p.14-15). The choice was informed by surveying 20 practitioners, most of whom preferred "AI engineering" (AIE p.15).

Adapting an existing foundation model to a task is generally far easier than building a task-specific model from scratch, though task-specific models can still be smaller, faster, and cheaper to run; the buy-or-build decision remains one teams must answer for themselves (AIE p.12).

## Key figures
- AI investment could approach $100 billion in the US and $200 billion globally by 2025, per Goldman Sachs Research (AIE p.13)
- One in three S&P 500 companies mentioned AI in Q2 2023 earnings calls, three times the rate a year earlier (AIE p.13)
- Companies mentioning AI in earnings calls saw an average 4.6% stock price increase vs. 2.4% for those that didn't, per WallStreetZen (AIE p.13-14)
- Terms like "Generative AI" and "Prompt Engineering" were added to LinkedIn profiles at an average rate increase of 75% per month as of August 2023 (AIE p.14)

## Examples
- [[github-copilot]]  (early production success of a foundation-model-based application)

## Related
- [[ai-engineering-vs-ml-engineering]]  (part-of: this synthesis elaborates why AI engineering diverges from ML engineering)
- [[ai-engineering-vs-full-stack-engineering]]  (part-of: this synthesis elaborates how foundation models shift app-development priorities)
- [[model-adaptation]]  (prerequisite: AI engineering relies on adapting existing foundation models rather than training new ones)

## Provenance
- [[sources/ch01-from-foundation-models-to-ai-engineering]]
