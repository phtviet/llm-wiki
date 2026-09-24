---
type: entity
sources: [ch07-reasons-not-to-finetune]
---
# BloombergGPT

BloombergGPT is a domain-specific model introduced by Bloomberg in March 2023, built to perform well on financial tasks and to be hostable in-house for use cases involving sensitive data, at a time when the strongest models on the market were all proprietary (AIE p.313-314).

Research by Li et al. (2023) found that OpenAI's GPT-4-0314, released the same month, significantly outperformed BloombergGPT across financial benchmarks, illustrated by the book's FiQA sentiment analysis and ConvFinQA table. The book cites this as a caution against assuming domain-specific finetuning is necessary just because general-purpose models seem to underperform on a specialized domain, since general-purpose models keep improving at domain-specific tasks too (AIE p.314). It notes Bloomberg may still have gained value from the exercise even if BloombergGPT lags on benchmarks, since benchmarks don't fully capture real-world performance, and the effort likely built expertise for developing future models (AIE p.314).

## Key figures
- 50 billion parameters, trained using 1.3 million A100 GPU hours (AIE p.313)
- Estimated compute cost between $1.3 million and $2.6 million, excluding data costs (Wu et al., 2023) (AIE p.313)
- GPT-4-0314 (zero-shot) scored 87.15 (FiQA sentiment analysis, weighted F1) and 76.48 (ConvFinQA, accuracy), versus BloombergGPT's 75.07 and 43.41 (AIE p.314)

## Related
- [[reasons-not-to-finetune]]  (example-of: cited as a case where a costly domain-specific model was later outperformed by a general-purpose model)
- [[domain-specific-models]]  (example-of: a domain-specific model built for financial tasks, contrasted with general-purpose models)
- [[gpt-4]]  (contrast: GPT-4-0314 significantly outperformed BloombergGPT on financial benchmarks despite being general-purpose)

## Provenance
- [[sources/ch07-reasons-not-to-finetune]]
