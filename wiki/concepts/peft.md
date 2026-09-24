---
type: concept
sources: [ch07-parameter-efficient-finetuning]
---
# PEFT (Parameter-Efficient Finetuning)

PEFT is finetuning that achieves performance close to [[full-finetuning]] while updating several orders of magnitude fewer parameters than the model's total; there is no fixed threshold, but the term is used when trainable parameters are dramatically reduced without much performance loss (AIE p.334). The idea was introduced by Houlsby et al. (2019), who inserted two adapter modules into each transformer block of a BERT model and updated only those adapters, achieving performance within 0.4% of full finetuning while training only 3% as many parameters, on the GLUE benchmark (AIE p.334-335). The cost of this approach is added inference latency, since the adapters introduce extra layers in the forward pass (AIE p.335).

PEFT lowers the hardware bar for finetuning and tends to also be sample-efficient: full finetuning may need tens of thousands to millions of examples for meaningful gains, while some PEFT methods perform well with just a few thousand (AIE p.335).

PEFT techniques split into two families. **Adapter-based (additive) methods** add trainable modules to the model's weights, as in Houlsby et al.'s original approach; besides [[lora]] (by far the most popular as of this writing), the family includes BitFit (Zaken et al., 2021), IA3 (Liu et al., 2022, notable for multi-task-friendly mixed batching and reported to sometimes outperform both LoRA and full finetuning), and LongLoRA (Chen et al., 2023, a context-length-extending LoRA variant) (AIE p.336). **Soft prompt-based methods** instead introduce trainable continuous-vector tokens ('soft prompts') fed alongside the input, contrasted with static, human-readable 'hard prompts'; soft prompts are optimized via backpropagation during tuning. Variants include prefix-tuning (Li and Liang, 2021), P-Tuning (Liu et al., 2021), and prompt tuning (Lester et al., 2021), which differ mainly in where the soft prompt tokens are inserted (AIE p.336-337). An analysis of over 1,000 open GitHub issues on huggingface/peft (October 2024) found LoRA dominates usage, with soft-prompt methods less common (AIE p.337-338).

## Key figures
- Houlsby et al. (2019): adapters reach within 0.4% of full-finetuning performance on GLUE using only 3% of the trainable parameters (AIE p.335)

## Examples
- [[lora]] (dominant adapter-based PEFT method)
- [[qlora]] (quantized LoRA variant)

## Related
- [[full-finetuning]] (contrast: updates all parameters vs. a small added or reparameterized subset)
- [[partial-finetuning]] (contrast: partial finetuning is parameter-inefficient, needing far more trainable parameters than PEFT for comparable performance)
- [[lora]] (part-of: LoRA is PEFT's dominant adapter-based technique)
- [[bert]] (example-of: Houlsby et al.'s original adapter experiments were run on BERT)
- [[finetuning]] (part-of: PEFT is a memory- and sample-efficient approach to finetuning)

## Provenance
- [[sources/ch07-parameter-efficient-finetuning]]
