---
type: concept
sources: [ch03-the-future-of-comparative-evaluation]
---
# Comparative Evaluation

Comparative evaluation ranks models by pairwise comparison of their outputs rather than scoring each output independently. It faces challenges of scalability, standardization, and the fact that relative performance does not equal absolute performance.

Despite these limitations, the technique has a durable future. First, it is easier for human evaluators to judge which of two outputs is better than to assign each a concrete score, and as models surpass human performance this may become the only viable form of human judgment: the Llama 2 paper reports that even when a model's writing exceeds the ability of the best human annotators, humans can still meaningfully compare two answers (Touvron et al., 2023) (AIE p.155). Second, comparative evaluation targets the quality that actually matters -- human preference -- which relieves the pressure to keep inventing new benchmarks to keep pace with expanding AI capability. Unlike benchmarks, which become useless once a model saturates them, comparative evaluation never saturates as long as newer, stronger models keep being introduced (AIE p.155). Third, it is relatively hard to game, since there is no easy way to cheat it the way one can train a model on reference data to inflate a benchmark score; this is why many trust public comparative leaderboards more than other public leaderboards (AIE p.155). Comparative evaluation can also surface discriminating signals unavailable elsewhere: for offline evaluation it complements evaluation benchmarks, and for online evaluation it complements A/B testing (AIE p.156).

## Key figures
None.

## Examples
- [[lmsys-chatbot-arena]]  (crowdsourced public comparative leaderboard)

## Related
- [[benchmark-saturation]]  (contrast: benchmarks saturate at a perfect score, while comparative evaluation never saturates as long as stronger models keep appearing)
- [[pointwise-evaluation]]  (contrast: scores each model independently vs. ranking by pairwise comparison)
- [[lmsys-chatbot-arena]]  (example-of: crowdsourced public leaderboard built on comparative evaluation)
- [[preference-model]]  (see-also: both aim to capture human preference between outputs)

## Provenance
- [[sources/ch03-the-future-of-comparative-evaluation]]
