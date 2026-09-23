---
type: concept
sources: [ch02-model-size]
---
# Training Tokens

For language models, dataset size is better measured in tokens than in training samples, since samples (a sentence, a Wikipedia page, a book) vary enormously in value; a token is the unit a model actually operates on, so counting tokens shows how much a model could potentially learn from the data (AIE p.68-69). Token counts aren't perfectly comparable across models either, since different tokenization processes yield different token counts for the same dataset (AIE p.69).

The number of tokens in a dataset differs from the number of *training* tokens, which counts tokens actually seen during training, including repeats across epochs: a 1-trillion-token dataset trained for two epochs yields 2 trillion training tokens (AIE p.69). As of the book's writing, large models are typically pre-trained on only one epoch of data (AIE p.69).

The [[chinchilla-scaling-law]] ties training-token count to parameter count for compute-optimal training: roughly 20 training tokens per parameter (AIE p.72).

## Key figures
- Meta's Llama datasets: 1.4 trillion tokens (Llama 1), 2 trillion tokens (Llama 2), 15 trillion tokens (Llama 3) (AIE p.69)
- RedPajama-v2 has 30 trillion tokens, equivalent to about 450 million books or 5,400 times the size of Wikipedia (AIE p.69)
- LaMDA: 137B parameters / 168B training tokens; GPT-3: 175B parameters / 300B training tokens; Jurassic: 178B parameters / 300B training tokens; Gopher: 280B parameters / 300B training tokens; MT-NLG 530B: 530B parameters / 270B training tokens; Chinchilla: 70B parameters / 1.4 trillion training tokens (AIE p.69-70)

## Examples
- [[llama-2]]
- [[llama-3]]

## Related
- [[model-size]]  (prerequisite: token counts must be weighed alongside parameter counts to judge model capability)
- [[chinchilla-scaling-law]]  (part-of: the scaling law's compute-optimal ratio is expressed in training tokens per parameter)
- [[token]]  (prerequisite: a training token is a count of the same base unit defined by the token concept)

## Provenance
- [[sources/ch02-model-size]]
