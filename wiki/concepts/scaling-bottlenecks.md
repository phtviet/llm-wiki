---
type: concept
sources: [ch02-model-size]
---
# Scaling Bottlenecks

Every order-of-magnitude increase in [[model-size]] has historically increased performance -- GPT-2 had an order of magnitude more parameters than GPT-1 (1.5 billion vs. 117 million), and GPT-3 had two more orders of magnitude than GPT-2 (175 billion vs. 1.5 billion) (AIE p.75). But two visible bottlenecks threaten continued scaling: training data and electricity (AIE p.75).

On data: the rate of training-dataset-size growth is outpacing the rate of new data being generated on the internet (Villalobos et al., 2022), raising a realistic concern about running out of internet data within a few years (AIE p.75). Compounding this, the internet is increasingly populated with AI-generated content, so future models trained on web data will be partially trained on AI output; some researchers worry that recursively training models on AI-generated data causes gradual forgetting of original data patterns and degraded performance (Shumailov et al., 2023) (AIE p.76). Data owners are also increasingly restricting scraping: Longpre et al. (2024) found that between 2023 and 2024, over 28% of the most critical sources in the C4 dataset became fully restricted, and 45% of C4 is now restricted overall due to Terms of Service and crawling changes (AIE p.76-77).

On electricity: data centers are estimated to consume 1-2% of global electricity today, projected to reach 4-20% by 2030 (Patel, Nishball, and Ontiveros, 2024); without new energy production, data centers can grow at most 50x (less than two orders of magnitude), raising concern about power shortages and rising electricity costs (AIE p.77).

## Key figures
- GPT-2 vs GPT-1: 1.5 billion vs. 117 million parameters; GPT-3 vs GPT-2: 175 billion vs. 1.5 billion (AIE p.75)
- Over 28% of C4's most critical sources became fully restricted 2023-2024; 45% of C4 now restricted overall (AIE p.76-77)
- Data centers consume an estimated 1-2% of global electricity today, projected 4-20% by 2030 (AIE p.77)
- Without new energy production, data centers can grow at most ~50x (AIE p.77)

## Related
- [[dataset-size]]  (boundary: data scarcity and restrictions limit how much training data can keep scaling)
- [[data-restrictions]]  (part-of: legal/ToS restrictions are one facet of the data bottleneck)
- [[scaling-law]]  (see-also: scaling law assumes ever-larger data and compute remain available; bottlenecks question that assumption)
- [[model-size]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch02-model-size]]
