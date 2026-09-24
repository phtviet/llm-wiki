---
type: concept
sources: [ch08-data-quantity]
---
# Progressive Finetuning Strategy

A technique for reducing the amount of high-quality, task-specific data needed by first finetuning on lower-quality or less-relevant data, then further finetuning on the smaller set of high-quality, relevant data (AIE p.374). Three examples given:

- **Self-supervised to supervised**: finetune first on abundant unlabeled domain documents (e.g., legal documents) in a self-supervised manner, then further finetune on a small set of labeled (question, answer) pairs (AIE p.374).
- **Less-relevant to relevant data**: finetune first on abundant data from a related but different task (e.g., tweet sentiment), then further finetune on the small target dataset (e.g., product review sentiment) (AIE p.374).
- **Synthetic to real data**: use AI models to synthesize a large volume of training data first, then further finetune on limited real data (e.g., sensitive medical reports) (AIE p.375).

The synthetic-to-real approach is harder to execute correctly, since it requires two distinct, coordinated finetuning jobs; done poorly, it can consume more compute while producing a worse model than finetuning directly on the smaller high-quality dataset (AIE p.375).

## Key figures
None.

## Related
- [[data-quantity]]  (part-of: a strategy for reducing the high-quality data volume otherwise required)
- [[data-synthesis]]  (prerequisite: the synthetic-to-real variant depends on AI-generated training data)
- [[self-supervised-finetuning]]  (example-of: the self-supervised-to-supervised variant is an application of self-supervised finetuning)
- [[transfer-learning]]  (see-also: both reuse knowledge from one task/domain to accelerate learning on another)

## Provenance
- [[sources/ch08-data-quantity]]
