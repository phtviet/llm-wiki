---
type: concept
sources: [ch02-the-probabilistic-nature-of-ai]
---
# Hallucination

Hallucination is when a model gives a response that isn't grounded in facts (AIE p.106). Unlike [[inconsistency]], hallucination isn't sufficiently explained by sampling randomness alone; a model can output something believed never seen in its training data, and the deeper cause is more nuanced (AIE p.107). Hallucination predates the terms "foundation model" and "transformer," having been discussed in text generation research as early as 2016 (Goyal et al., 2016), with detection and measurement a staple of natural language generation research since (Lee et al., 2018; Nie et al., 2019; Zhou et al., 2020) (AIE p.107).

Two hypotheses explain why hallucination occurs. The first, from Ortega et al. at DeepMind (2021), holds that a model can't differentiate between data it's given and data it generates: once it produces an out-of-the-ordinary statement, later tokens are conditioned on that statement as if it were fact, a phenomenon Ortega et al. call self-delusion (AIE p.108). Zhang et al. (2023) term the resulting cascade "snowballing hallucinations," where an initial wrong assumption causes the model to keep hallucinating to justify it, sometimes causing errors on questions the model could otherwise answer correctly (AIE p.108). The DeepMind paper suggests two mitigations: a reinforcement-learning technique that trains the model to differentiate user-provided prompts (observations) from its own generated tokens (actions), and a supervised-learning technique that includes factual and counterfactual signals in training data (AIE p.109).

The second hypothesis, argued by OpenAI researcher Leo Gao and echoed by OpenAI co-founder John Schulman in an April 2023 UC Berkeley talk, is that hallucination comes from a mismatch between the model's internal knowledge and the labeler's internal knowledge: during [[supervised-finetuning]], models are trained to mimic labeler-written responses that may use knowledge the model itself doesn't have, effectively teaching it to hallucinate (AIE p.109). Schulman believes LLMs know if they know something, and proposed two fixes: verification, where the model is asked to retrieve the sources behind a response, and reinforcement learning with a reward function that punishes fabrication more heavily, since the [[reward-model]] is normally trained only on pairwise comparisons without an explanation of why one response is better (AIE p.109). Schulman noted OpenAI found [[rlhf]] helps reduce hallucination, but the [[instructgpt]] paper actually showed RLHF made hallucination worse compared to supervised finetuning alone, even though human labelers still preferred the RLHF model overall (AIE p.109).

Prompt-based mitigations include instructing the model to answer truthfully and admit uncertainty, and asking for concise responses, since fewer generated tokens give the model less room to fabricate (AIE p.110).

## Key figures
None. The InstructGPT RLHF-vs-SFT hallucination comparison is qualitative (Figure 2-26), without a specific load-bearing number (AIE p.109).

## Examples
- [[instructgpt]]  (RLHF version hallucinates more than the SFT-only version, per Ouyang et al., 2022)

## Related
- [[probabilistic-nature-of-ai]]  (part-of: hallucination is one consequence of a model's probabilistic generation, though not explained by sampling randomness alone)
- [[inconsistency]]  (contrast: inconsistency arises from sampling randomness, hallucination from deeper causes)
- [[supervised-finetuning]]  (boundary: SFT on labeler knowledge the model lacks can teach the model to hallucinate)
- [[rlhf]]  (boundary: expected to reduce hallucination, but shown to worsen it for InstructGPT)
- [[reward-model]]  (boundary: trained only on pairwise comparisons without explanations, limiting its ability to penalize fabrication)
- [[instructgpt]]  (example-of: the book's worked example showing RLHF increases hallucination versus SFT alone)

## Provenance
- [[sources/ch02-the-probabilistic-nature-of-ai]]
