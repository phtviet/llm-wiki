---
type: concept
sources: [ch02-model-size]
---
# Dataset Size (Training Data Scale)

Dataset size for foundation models is best measured in number of tokens rather than number of training samples, since training samples vary hugely in information content (a sentence versus a whole book) (AIE p.68-69). Token counts are also imperfect since different models tokenize the same data differently, but tokens are the unit a model actually operates on, so token count best reflects how much a model can potentially learn from a dataset (AIE p.69).

The number of tokens in a dataset is not the same as the number of training tokens: if a 1-trillion-token dataset is used for two epochs (passes through the dataset), the model is trained on 2 trillion training tokens (AIE p.69). Data quantity, quality, and diversity are described as the three golden goals for training data (AIE p.69).

## Key figures
- Llama 1 trained on 1.4 trillion tokens; Llama 2 on 2 trillion tokens; Llama 3 on 15 trillion tokens (AIE p.69)
- RedPajama-v2 open dataset contains 30 trillion tokens, equivalent to about 450 million books or 5,400x the size of Wikipedia (AIE p.69)
- LaMDA: 137B parameters / 168B training tokens; GPT-3: 175B / 300B; Jurassic: 178B / 300B; Gopher: 280B / 300B; MT-NLG 530B: 530B / 270B; Chinchilla: 70B / 1.4 trillion (AIE p.69-70)

## Related
- [[model-size]]  (see-also: model size must be considered jointly with dataset size)
- [[scaling-law]]  (prerequisite: the Chinchilla scaling law derives the compute-optimal ratio between dataset size and model size)
- [[tokenization]]  (prerequisite: token counts depend on the tokenization process used)
- [[data-restrictions]]  (boundary: growing legal and terms-of-service restrictions are shrinking the pool of usable web data)

## Provenance
- [[sources/ch02-model-size]]
