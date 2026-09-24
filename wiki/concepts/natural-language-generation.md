---
type: concept
sources: [ch04-generation-capability]
---
# Natural Language Generation (NLG)

NLG is the NLP subfield that studies open-ended text generation, predating generative AI; early 2010s NLG tasks included translation, summarization, and paraphrasing (AIE p.163). Early NLG evaluation centered on fluency (grammatical correctness and natural-soundingness) and coherence (whether the whole text follows a logical structure), since generated text at the time was often ungrammatical and awkward (AIE p.163). Some tasks used their own metrics: faithfulness for translation (how faithful the translation is to the source) and relevance for summarization (whether the summary focuses on the most important source content) (Li et al., 2022) (AIE p.164).

As generation quality improved, AI-generated text became nearly indistinguishable from human text, so fluency and coherence became less important as general metrics, though they remain useful for weaker models or for creative writing and low-resource languages (AIE p.164). Fluency and coherence can be evaluated using [[ai-as-a-judge]] or using [[perplexity]] (AIE p.164). Some early metrics, including faithfulness and relevance, have been repurposed with significant modification to evaluate foundation model outputs (AIE p.164).

## Key figures
None.

## Examples
- [[gpt-2]]  (its fluency/coherence gains over prior language models drove 2019 buzz)

## Related
- [[factual-consistency]]  (contrast: a newer evaluation concern that superseded fluency/coherence as the pressing issue for generative models)
- [[perplexity]]  (see-also: an alternative, automatic way to gauge fluency-like quality)
- [[ai-as-a-judge]]  (see-also: practical method for scoring fluency and coherence)

## Provenance
- [[sources/ch04-generation-capability]]
