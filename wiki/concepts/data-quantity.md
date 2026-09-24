---
type: concept
sources: [ch08-data-quantity]
---
# Data Quantity

How much data is needed for finetuning varies enormously by situation, from single-example learning experiments up to millions of examples -- still small compared to the trillions of tokens used to pre-train a [[foundation-model]] from scratch (AIE p.372).

Beyond [[data-quality]] and [[data-coverage]], three factors determine how much finetuning data is needed: the [[finetuning-frameworks-and-methods|finetuning technique]] used (full finetuning needs orders of magnitude more data than [[peft]] methods like [[lora]]), task complexity (simple classification needs far less data than complex reasoning tasks), and the base model's starting performance (closer-to-desired performance needs fewer examples; bigger base models often need fewer finetuning examples, the opposite of [[pre-training|pre-training]], where bigger models need more data) (AIE p.373).

If you have only a few hundred to a few thousand examples, PEFT tends to work best; with tens of thousands to millions of (instruction, response) pairs, full finetuning becomes attractive (AIE p.373). OpenAI's finetuning guide shows that with few examples (100), more advanced models finetune to better performance, likely because they already perform better out of the box; but after finetuning on 550,000 examples, five different models performed similarly (AIE p.373).

A practical starting strategy: begin with a small, well-crafted dataset (e.g., 50 examples) before investing in a large one. Clear improvement suggests more data will help further; no improvement with a small set means a bigger dataset will rarely help, though hyperparameters, data quality, and prompt design can also be the cause rather than data volume (AIE p.374). Experimenting with subsets (25%, 50%, 100% of a current dataset) and plotting the resulting performance-gain curve estimates how much more data is needed. Additional examples typically yield diminishing returns -- the first 1,000 examples might raise accuracy by ten percentage points while the next 1,000 raise it by only five (AIE p.375).

Data diversity across task types, topics, and output formats also affects how much data is needed, since a model benefits from being exposed to a broad set of tasks during finetuning (AIE p.376). How much data to use is also bounded by budget: annotation cost per example limits the maximum affordable dataset size, and money spent on data trades off against money available for compute (AIE p.377).

## Key figures
- [[llama-2]] trained on 2 trillion tokens, [[llama-3]] on 16 trillion tokens -- equivalent to roughly 1 billion and 15 billion 2,000-token examples, respectively (AIE p.372)
- With 100 examples, more advanced models give much better finetuning performance; with 550,000 examples, all five tested models perform similarly (AIE p.373)
- In most cases, finetuning improvements with as few as 50-100 examples should be observable (AIE p.374)
- Example diminishing-returns pattern: first 1,000 examples improve accuracy by ten percentage points, next 1,000 by only five (AIE p.375)

## Examples
- [[ossification]]  (why more finetuning data can sometimes hurt rather than help)
- [[progressive-finetuning-strategy]]  (technique for reducing high-quality data needs)

## Related
- [[finetuning]]  (prerequisite: data quantity is a design input to how finetuning is planned)
- [[peft]]  (contrast: needs far less data than full finetuning)
- [[full-finetuning]]  (contrast: needs orders of magnitude more data than PEFT)
- [[data-quality]]  (see-also: quantity is one of several data-curation factors alongside quality and coverage)
- [[data-coverage]]  (see-also: diversity/coverage of tasks and topics affects how much data is needed)
- [[ossification]]  (boundary: explains when more finetuning data can make results worse)
- [[scaling-law]]  (contrast: pre-training scaling favors bigger models needing more data, the opposite of the finetuning base-model-size relationship described here)
- [[foundation-model]]  (see-also: mentioned in this page's text)
- [[pre-training]]  (see-also: mentioned in this page's text)
- [[llama-2]]  (see-also: mentioned in this page's text)
- [[llama-3]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch08-data-quantity]]
