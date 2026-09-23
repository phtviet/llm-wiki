---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Evaluation

Evaluation is about mitigating risks and uncovering opportunities; it is needed throughout the whole [[model-adaptation]] process — to select models, benchmark progress, decide deployment readiness, and detect issues and opportunities in production (AIE p.44). It has always mattered in ML engineering but matters even more with foundation models, chiefly because of their open-ended nature and expanded capabilities: close-ended tasks like fraud detection have expected ground truths to compare against, but open-ended tasks like chatbot responses have too many possible valid outputs to curate an exhaustive comparison set (AIE p.44).

The existence of many adaptation techniques compounds the difficulty, since a system's apparent performance depends heavily on which technique was used to evaluate it. When Google launched Gemini in December 2023, it claimed Gemini beat ChatGPT on the MMLU benchmark, but the comparison used a prompt-engineering technique (CoT@32, 32 shown examples) favoring Gemini against ChatGPT's 5-shot prompting; under a matched 5-shot comparison, ChatGPT performed better (AIE p.44).

## Key figures
None. (Model-specific benchmark figures live on [[prompt-engineering]], where the Gemini/ChatGPT MMLU comparison is drawn.)

## Related
- [[application-development]]  (part-of: one of application development's three responsibilities)
- [[prompt-engineering]]  (boundary: evaluation results can shift dramatically depending on the prompting technique used, complicating fair comparison)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
