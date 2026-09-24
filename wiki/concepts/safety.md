---
type: concept
sources: [ch04-generation-capability]
---
# Safety (AI Output Safety)

Safety is an umbrella term covering the ways a model's outputs can cause harm to users and society, including toxicity and biases (AIE p.164). Different safety solutions categorize harms differently (e.g. OpenAI's content moderation endpoint, Meta's Llama Guard paper by Inan et al., 2023), but unsafe content generally falls into these categories (AIE p.170):

1. Inappropriate language, including profanity and explicit content.
2. Harmful recommendations and tutorials (e.g. instructions to rob a bank, or encouragement of self-destructive behavior).
3. Hate speech, including racist, sexist, homophobic, and other discriminatory speech.
4. Violence, including threats and graphic detail.
5. Stereotypes (e.g. defaulting to female names for nurses or male names for CEOs).
6. Political or religious ideological bias, which can skew a model toward supporting one ideology; studies (Feng et al., 2023; Motoki et al., 2023; Hartman et al., 2023) found models can carry political biases, with GPT-4 shown as more left-leaning/libertarian and Llama more authoritarian-leaning (AIE p.171).

General-purpose [[ai-as-a-judge]] models (GPTs, Claude, Gemini) can detect many harmful outputs when prompted properly, and model providers also expose dedicated moderation tools (AIE p.171). Smaller specialized toxicity-detection models (much smaller, faster, and cheaper than general-purpose judges) trained on human-generated toxic text can also be applied to AI-generated text, including models for specific languages such as Danish and Vietnamese (AIE p.171).

Factual inconsistency is technically a safety issue too, given its potential for harm, but is treated separately in the book due to its scope (see [[factual-consistency]]) (AIE p.164).

## Key figures
None.

## Examples
- [[realtoxicityprompts]]  (benchmark of prompts likely to elicit toxic generations)
- [[bold-benchmark]]  (benchmark measuring bias in open-ended generation)

## Related
- [[factual-consistency]]  (part-of: factual inconsistency is technically a safety concern, broken out separately due to scope)
- [[ai-as-a-judge]]  (part-of: general-purpose AI judges are a common way to detect unsafe outputs)

## Provenance
- [[sources/ch04-generation-capability]]
