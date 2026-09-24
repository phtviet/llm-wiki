---
type: concept
sources: [ch05-context-length-and-context-efficiency]
---
# Context Length

Context length is the maximum amount of information a model can accept in a prompt. It caps how much a prompt can include, and has expanded rapidly across model generations: the first three generations of GPT had 1K, 2K, and 4K context length respectively, growing 2,000 times within five years to Gemini-1.5 Pro's 2M context length (AIE p.218). Larger context lengths translate directly into usable capacity: a 100K context length can fit a moderate-sized book, and a 2M context length can fit approximately 2,000 Wikipedia pages or a reasonably complex codebase such as PyTorch (AIE p.218).

Not all parts of a prompt are used equally well: a model is much better at understanding instructions given at the beginning and end of a prompt than in the middle (Liu et al., 2023) (AIE p.218). This positional weakness is measured by the [[needle-in-a-haystack-test]] and by similar tests such as RULER (Hsieh et al., 2024). If a model's performance grows increasingly worse with a longer context, that is a signal to shorten prompts rather than rely on the model's full window (AIE p.219).

## Key figures
- GPT generations: 1K, 2K, 4K context length for the first three GPTs (AIE p.218)
- Context length grew 2,000x between February 2019 and May 2024, from GPT-2's 1K to Gemini-1.5 Pro's 2M (AIE p.218)
- 100K context length fits a moderate-sized book; this book is ~120,000 words / 160,000 tokens (AIE p.218)
- 2M context length fits ~2,000 Wikipedia pages or a codebase like PyTorch (AIE p.218)

## Examples
- [[needle-in-a-haystack-test]]  (method for evaluating how well a model uses different parts of its context window)

## Related
- [[needle-in-a-haystack-test]]  (prerequisite: evaluating positional effectiveness within a prompt requires a long enough context length to test)
- [[prompt-engineering]]  (part-of: context length is a constraint on what a prompt can contain)
- [[data-contamination]]  (boundary: private or unseen test information must be used in context-length tests so the model can't rely on memorized training data instead of the prompt)

## Provenance
- [[sources/ch05-context-length-and-context-efficiency]]
