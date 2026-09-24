---
type: concept
sources: [ch07-finetuning-tactics]
---
# Finetuning Frameworks and Methods (Practical Choice)

Choosing how to finetune requires picking a base model, a finetuning method, and a framework. Finetuning APIs (offered by model providers, cloud providers, and third parties) let a user upload data, select a base model, and receive a finetuned model back, but they limit users to supported base models and may not expose all tunable knobs (AIE p.358).

Alternatively, finetuning frameworks such as LLaMA-Factory, unsloth, PEFT, Axolotl, and LitGPT support a wide range of methods, especially adapter-based techniques; many base models also publish open source training code for full finetuning. Doing finetuning yourself gives more flexibility but requires provisioning compute: adapter-based methods can often run on a mid-tier GPU, while distributed training across multiple machines needs a framework such as DeepSpeed, PyTorch Distributed, or ColossalAI (AIE p.358).

The choice of finetuning method also depends on data volume: full finetuning typically needs at least thousands of examples, while PEFT methods such as [[lora]] can perform well with far smaller datasets, sometimes only a few hundred examples. Serving considerations matter too -- adapter-based methods like LoRA let multiple finetuned models share one base model at serving time, whereas full finetuning requires serving a separate full model per finetune (AIE p.358).

## Key figures
None.

## Related
- [[finetuning]]  (prerequisite: this practical guidance builds on the finetuning concept)
- [[finetuning-development-path]]  (see-also: both describe practical finetuning workflow decisions)
- [[model-api]]  (contrast: finetuning APIs mirror inference APIs' provider/cloud/third-party structure but return a finetuned model instead of serving inference)

## Provenance
- [[sources/ch07-finetuning-tactics]]
