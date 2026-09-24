---
type: concept
sources: [ch08-data-coverage]
---
# Data Coverage

Data coverage is the requirement that a model's training data span the range of problems the application expects to solve, including how differently users express those problems. Because coverage depends on having enough variety in the data, it is often called data diversity (AIE p.369).

Which dimensions of diversity matter depends on the application: a French-to-English translation tool doesn't need language diversity but benefits from diversity in topic, length, and speaking style, while a global product-recommendation chatbot needs linguistic and cultural diversity more than domain diversity. For general-purpose chatbots, finetuning data should be diverse across topics and speaking patterns (AIE p.369).

Diversity is not an unqualified good: 'The Data Addition Dilemma' (Shen et al., 2024) found that adding more heterogeneous data can in some cases worsen performance (AIE p.369). An experiment by Zhou et al. (2023) trained a 7B-parameter model on three 2,000-example datasets -- high-quality-but-not-diverse, diverse-but-low-quality, and both diverse-and-high-quality -- and found the both-diverse-and-high-quality dataset produced the best generation quality, showing quality and diversity compound rather than substitute for each other (AIE p.371).

One consistent diversity axis across pre-training, supervised finetuning, and preference finetuning is domain diversity, though the ideal mix of domains differs by phase; [[llama-3]] illustrates this with its differing domain-mix percentages at each phase (AIE p.370). Post-training data has additional diversity axes not captured by domain mix alone, such as token count (context and response length), number of conversational turns, and -- for models using synthetic data -- the ratio of human-generated to AI-generated data (AIE p.370).

A simple approach to choosing a data mix is to reflect real-world application usage; a more rigorous approach runs scaling-law experiments, training several small models on candidate data mixes to predict a large model's performance on each, then picking the best-guess mix (AIE p.371).

## Key figures
None. The concept carries no figure of its own; Llama 3's domain-mix percentages are entity-specific and live on [[llama-3]].

## Examples
- [[llama-3]]  (domain mix shifts across pre-training, supervised finetuning, and preference finetuning)
- [[nemotron-4]]  (curated for task, topic, and instruction diversity)

## Related
- [[training-data-curation]]  (part-of: data coverage/diversity is one quality dimension curators optimize for)
- [[dataset-engineering]]  (part-of: data coverage is a consideration within the broader dataset engineering process)
- [[scaling-law]]  (prerequisite: scaling-law experiments on small models are used to predict optimal data mixes for large models)
- [[llama-3]]  (example-of: domain mix table shows diversity considerations differing by training phase)

## Provenance
- [[sources/ch08-data-coverage]]
