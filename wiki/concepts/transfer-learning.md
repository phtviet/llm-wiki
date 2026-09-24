---
type: concept
sources: [ch07-finetuning-overview]
---
# Transfer Learning

Transfer learning is the concept of transferring knowledge gained from one task to accelerate learning for a new, related task, first introduced by Bozinovski and Fulgosi in 1976 (AIE p.308). [[finetuning]] is one way to do transfer learning: for LLMs, knowledge gained from [[pre-training]] on text completion (a task with abundant data) is transferred to more specialized tasks, like legal question answering or text-to-SQL, which often have less available data. This transfer capability is what makes [[foundation-model]]s particularly valuable (AIE p.308).

An early large-scale success was Google's multilingual translation system (Johnson et al., 2016), which transferred its knowledge of Portuguese-English and English-Spanish translation to translate Portuguese to Spanish directly, despite no Portuguese-Spanish examples in training data (AIE p.308).

Transfer learning improves [[sample-efficiency]], letting a model learn the same behavior from fewer examples: training from scratch for legal question answering may need millions of examples, while finetuning a good base model might need only a few hundred (AIE p.309). OpenAI's [[instructgpt]] paper (2022) suggested viewing finetuning as unlocking capabilities a model already has but that are difficult to access via prompting alone (AIE p.309).

Finetuning is not the only way to do transfer learning; [[feature-based-transfer]] is another approach (AIE p.309).

## Key figures
None.

## Examples
- [[finetuning]]  (dominant transfer-learning method for LLMs)
- [[feature-based-transfer]]  (alternative approach, common in computer vision)

## Related
- [[finetuning]]  (example-of: finetuning is one way to do transfer learning)
- [[feature-based-transfer]]  (contrast: reuses extracted features via another model rather than continuing training)
- [[sample-efficiency]]  (part-of: transfer learning's main benefit is improved sample efficiency)
- [[instructgpt]]  (see-also: its 2022 paper frames finetuning as unlocking existing capabilities)
- [[pre-training]]  (prerequisite: transfer learning moves knowledge from pre-training to a target task)

## Provenance
- [[sources/ch07-finetuning-overview]]
