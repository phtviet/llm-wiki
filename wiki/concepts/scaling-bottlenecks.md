---
type: concept
sources: [ch02-model-size]
---
# Scaling Bottlenecks

Every order-of-magnitude increase in model size has historically improved model performance — GPT-2 had roughly ten times the parameters of GPT-1, and GPT-3 had roughly one hundred times the parameters of GPT-2 — but two visible bottlenecks threaten continued scaling: training data and electricity (AIE p.75).

**Data bottleneck.** Foundation models consume so much data that the training-dataset growth rate now outpaces the rate at which new data is generated (Villalobos et al., 2022), raising a realistic concern about running out of internet data within years (AIE p.75). Content published on the internet should be assumed to be included in future training data. Companies are also responding by restricting data access: Longpre et al. (2024) found that between 2023 and 2024, data restrictions rendered over 28% of the most critical sources in the C4 dataset fully restricted, and 45% of C4 is now restricted due to Terms of Service and crawling changes (AIE p.76). Once public human-generated data is exhausted, proprietary data (copyrighted books, translations, contracts, medical records, genome sequences) becomes the most feasible path to more training data and a competitive advantage (AIE p.76).

A related concern is recursive training on AI-generated content, since the internet is increasingly populated by model outputs; some researchers worry this causes model collapse, where new models gradually forget original data patterns and degrade over time (Shumailov et al., 2023) (AIE p.76).

**Electricity bottleneck.** Data centers are estimated to consume 1-2% of global electricity as of the book's writing, projected to reach 4-20% by 2030 (Patel, Nishball, and Ontiveros, 2024); without new energy production, data centers can grow at most about 50 times (fewer than two orders of magnitude), raising concern about power shortages and rising electricity costs (AIE p.77).

## Key figures
- GPT-2 (1.5 billion parameters) is roughly an order of magnitude larger than GPT-1 (117 million); GPT-3 (175 billion) is roughly two orders of magnitude larger than GPT-2 (AIE p.75)
- Over 28% of C4's most critical sources became fully restricted between 2023-2024; 45% of C4 is now restricted overall (AIE p.76)
- Data centers consume an estimated 1-2% of global electricity, projected to reach 4-20% by 2030; can grow at most ~50x before hitting energy limits (AIE p.77)

## Examples
- None

## Related
- [[model-size]]  (boundary: marks the practical limits on how far model-and-data scaling can continue)
- [[data-synthesis]]  (see-also: recursive training on AI-generated internet content risks model collapse, a concern adjacent to synthetic-data training)

## Provenance
- [[sources/ch02-model-size]]
