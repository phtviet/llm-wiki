---
type: synthesis
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Gemini/ChatGPT MMLU Prompting Comparison

When Google launched Gemini in December 2023, it claimed Gemini outperformed ChatGPT on the MMLU benchmark (Hendrycks et al., 2020). The comparison used different prompting techniques for each model: Gemini was evaluated with CoT@32 (shown 32 examples), while ChatGPT was shown only 5 examples. When both were evaluated with five examples instead, ChatGPT performed better (AIE p.44).

The source draws this as a cross-cutting illustration that the choice of adaptation/prompting technique used during evaluation can itself determine which model looks better, complicating fair comparison between foundation models (AIE p.44-45).

## Key figures
- Gemini Ultra: 90.04% MMLU with CoT@32, versus 83.7% MMLU with 5-shot (AIE p.44-45)
- Gemini Pro: 79.13% MMLU with CoT@8 (AIE p.44)
- [[gpt-4|GPT-4]]: 87.29% MMLU CoT@32 (via API), versus 70% 5-shot (AIE p.44)
- GPT-3.5: 78.4% MMLU 5-shot fka(AIE p.44)

## Related
- [[evaluation]]  (example-of: illustrates how adaptation technique choice affects evaluation results)
- [[prompt-engineering]]  (example-of: illustrates prompt engineering's effect on measured model performance)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
