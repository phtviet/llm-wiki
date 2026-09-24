---
type: concept
sources: [ch06-tools]
---
# Capability Extension

Capability extension is a category of agent tools that address the inherent limitations of AI models, giving a model a performance boost without needing to retrain it. AI models are notoriously bad at math: a model asked to divide 199,999 by 292 will likely fail, but the calculation becomes trivial if the model has access to a calculator. Rather than training a model to be good at arithmetic, it is far more resource-efficient to give it access to a tool (AIE p.279).

Other simple capability-extension tools include a calendar, timezone converter, unit converter, and translator for languages the model isn't good at. More complex and powerful are code interpreters: instead of training a model to understand code, giving it access to a code interpreter lets it execute code, return results, or analyze failures, letting the agent act as a coding assistant, data analyst, or research assistant. Automated code execution, however, carries the risk of code injection attacks, requiring proper security measures (AIE p.280).

External tools can also make a text-only or image-only model multimodal: a text-only model can use a text-to-image tool to also generate images (this is how ChatGPT uses DALL-E), and a text-only model can use image captioning, transcription, or OCR tools to process images, audio, or PDFs (AIE p.280).

Tool use can significantly boost a model's performance compared to prompting or finetuning alone. Chameleon (Lu et al., 2023) shows a GPT-4-powered agent augmented with a set of 13 tools -- including knowledge retrieval, a query generator, an image captioner, a text detector, and Bing search -- outperforming GPT-4 alone on several benchmarks (AIE p.280).

## Key figures
- Chameleon, a GPT-4 agent with 13 tools, improves the best published few-shot result on ScienceQA by 11.37% (AIE p.280)
- Chameleon improves accuracy on TabMWP (Tabular Math Word Problems) by 17% (AIE p.280)

## Examples
- [[dalle]]

## Related
- [[tool-inventory]]  (part-of: capability extension is one of three tool categories)
- [[gpt-4]]  (example-of: Chameleon's underlying model, boosted by 13 tools)
- [[prompt-attacks]]  (boundary: code interpreter use carries code-injection risk, addressed via defensive prompt engineering)

## Provenance
- [[sources/ch06-tools]]
