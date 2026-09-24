---
type: concept
sources: [ch05-information-extraction, ch08-model-distillation]
---
# Information Extraction

Information extraction is a prompt attack that exploits a language model's conversational interface to pull out training data or context information it was not meant to reveal. Motivations include data theft (extracting training data to build a competitive model), privacy violation (exposing private data used in training or context, e.g. Gmail's autocomplete model trained on users' emails), and copyright infringement (getting the model to regurgitate copyrighted text) (AIE p.243).

A related niche research area, factual probing, studies what a model knows rather than attacking it: the LAMA benchmark (Petroni et al., 2019) probes relational knowledge of the form 'X [relation] Y' using fill-in-the-blank prompts such as 'Winston Churchill is a _ citizen' (AIE p.243). The same fill-in-the-blank technique can be repurposed to extract sensitive training data, on the assumption that models memorize training data and the right prompt can trigger that memorization, e.g. 'X's email address is _' (AIE p.244).

Carlini et al. (2020) and Huang et al. (2022) showed such extraction is technically possible on GPT-2 and GPT-3 but low-risk in practice, since an attacker generally needs to know the specific context an item appeared in during training (AIE p.244). Nasr et al. (2023) overturned that limit with a divergence attack: prompting ChatGPT (GPT-3.5-turbo) to repeat the word 'poem' forever caused it to repeat the word for a while and then diverge into nonsensical output, a small fraction of which was copied verbatim from training data -- demonstrating extraction without knowing the training data's context (AIE p.244). They estimated memorization rates of close to 1% for the models studied, higher when a model's training distribution is closer to the test corpus, and found a clear trend that larger models memorize more and are therefore more vulnerable (AIE p.245).

Extraction is not limited to text: Carlini et al. (2023) extracted over a thousand near-duplicate images, including trademarked logos, from the open source diffusion model Stable Diffusion, concluding diffusion models are less private than prior generative models like GANs (AIE p.245). Extracted data does not always contain PII -- much of it is common text like license boilerplate or song lyrics -- and PII risk can be mitigated with filters blocking PII-seeking requests and PII-containing responses (AIE p.245-246).

Models can also regurgitate copyrighted training data without any adversarial attack. Stanford's Holistic Evaluation of Language Models (2022) measured copyright regurgitation by prompting a model with a book's first paragraph and checking whether it generated the second paragraph verbatim, concluding verbatim regurgitation of long copyrighted sequences is uncommon but noticeable for popular books; the study excluded non-verbatim regurgitation (e.g. a reworded Lord of the Rings), which remains a nontrivial and harder-to-detect risk (AIE p.246-247).

## Key figures
- Estimated model memorization rate of close to 1% in Nasr et al.'s (2023) extraction study (AIE p.245)
- Over a thousand near-duplicate images extracted from Stable Diffusion, including trademarked logos (AIE p.245)

## Examples
- [[lama-benchmark]]  (factual-probing benchmark for relational knowledge)
- [[helm]]  (used to measure copyright regurgitation across foundation models)

## Related
- [[prompt-attacks]]  (part-of: information extraction is one category of prompt attack, alongside jailbreaking and prompt extraction)
- [[jailbreaking-and-prompt-injection]]  (contrast: bypasses constraints to make the model do harmful things, vs. extracts hidden data)
- [[prompt-extraction]]  (contrast: targets an application's system prompt specifically, vs. training data or context in general)
- [[prompt-attack-risks]]  (part-of: data theft, privacy violation, and copyright infringement are specific risk categories of prompt attacks)
- [[model-distillation]]  (boundary: distillation trains a student on a teacher's outputs by design, whereas information extraction pulls data the model was not meant to reveal)
- [[helm]]  (evaluates: HELM's copyright regurgitation measurement is a form of evaluating this risk)

## Provenance
- [[sources/ch05-information-extraction]]
