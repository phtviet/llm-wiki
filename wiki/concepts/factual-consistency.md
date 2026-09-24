---
type: concept
sources: [ch04-generation-capability]
---
# Factual Consistency

Factual consistency measures whether a model's output is grounded in fact, and can be verified under two settings (AIE p.164):

- **Local factual consistency** — the output is evaluated against an explicitly given context; it is consistent if supported by that context (e.g. if given context says the sky is purple, an output of "the sky is purple" is locally consistent). This matters for scoped tasks like summarization, customer support chatbots, and business analysis (AIE p.164-165).
- **Global factual consistency** — the output is evaluated against open, commonly accepted knowledge, mattering for broad-scope tasks like general chatbots, fact-checking, and market research (AIE p.165).

Consistency is easier to verify against explicit context than against open knowledge, where the hardest part is often determining what the facts even are — trust in sources varies, misinformation is common, and the "absence of evidence" fallacy is a risk (AIE p.165). Wan et al. (2024) found models weigh a source's relevance to the query heavily while largely ignoring stylistic signals humans value, such as scientific references or neutral tone (AIE p.166).

When designing hallucination metrics, it helps to identify which query types a model tends to hallucinate on — e.g. niche-knowledge queries (the book gives VMO vs. IMO as an example) and queries asking about things that don't exist — and focus benchmarks on those (AIE p.165-166).

Factual consistency can be verified via [[ai-as-a-judge]] (general-purpose or specialized), via [[textual-entailment]] framing, or via trained classification scorers. Liu et al. (2023) and Luo et al. (2023) showed GPT-3.5 and GPT-4 outperform prior methods at measuring factual consistency (AIE p.166). More sophisticated AI-judge techniques include self-verification and knowledge-augmented verification (AIE p.167):

- **Self-verification** (e.g. SelfCheckGPT, Manakul et al., 2023) assumes that if a model's multiple generated outputs disagree with each other, the original output is likely hallucinated; it generates N new responses and measures consistency of the original response R against them, but requires many AI queries and can be expensive (AIE p.167).
- **Knowledge-augmented verification** (e.g. SAFE, Wei et al., 2024) uses search-engine results to verify a response in four steps: decompose the response into individual statements, revise each statement to be self-contained, propose fact-checking queries per statement, and use AI to check consistency against search results (AIE p.167).

Instead of general-purpose AI judges, specialized scorers can be trained as a classification task over (premise, hypothesis) pairs, predicting entailment, contradiction, or neutral — e.g. DeBERTa-v3-base-mnli-fever-anli (AIE p.168). Factual consistency is a crucial evaluation criterion for [[rag]] systems, where the generated response should be consistent with retrieved context (AIE p.169).

## Key figures
- GPT-judge, TruthfulQA's finetuned judge, predicts human-judged truthfulness with 90-96% accuracy (AIE p.166)
- DeBERTa-v3-base-mnli-fever-anli: 184-million-parameter model trained on 764,000 annotated (hypothesis, premise) pairs to predict entailment (AIE p.168)

## Examples
- [[truthfulqa]]  (benchmark for factual consistency, with its GPT-judge scorer)

## Related
- [[textual-entailment]]  (prerequisite: entailment/contradiction/neutral classification underlies specialized factual-consistency scorers)
- [[ai-as-a-judge]]  (part-of: general-purpose and specialized AI judges are a primary way factual consistency is verified)
- [[hallucination]]  (contrast: factual inconsistency is the negative outcome hallucination detection aims to catch)
- [[safety]]  (part-of: factual inconsistency is technically a safety concern, but is broken out separately given its scope)
- [[perplexity]]  (see-also: chapter 3's related metric for language-model output quality, referenced alongside evaluation criteria)

## Provenance
- [[sources/ch04-generation-capability]]
