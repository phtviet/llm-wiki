---
type: entity
sources: [ch03-ranking-models-with-comparative-evaluation]
---
# LMSYS Chatbot Arena

LMSYS's Chatbot Arena is a crowdsourced public leaderboard that ranks models using scores computed from pairwise model comparisons contributed by the community, an instance of [[comparative-evaluation]] (AIE p.149).

Chatbot Arena originally used the Elo rating algorithm to compute model rankings, then switched to the Bradley-Terry algorithm after finding Elo too sensitive to the order in which evaluators and prompts arrived. Even after switching, its developers for a time continued calling the ratings 'Elo scores': each Bradley-Terry score is multiplied by 400 (the Elo scale) and added to 1,000 (the initial Elo score), then rescaled so that Llama-13b has a score of 800 (AIE p.150).

The book's own analysis of Chatbot Arena's ranking finds it good at predicting future match outcomes, at least for model pairs with sufficient matches (AIE p.151).

## Key figures
- Bradley-Terry scores rescaled by multiplying by 400 and adding 1,000, then rescaled so Llama-13b scores 800 (AIE p.150)

## Related
- [[comparative-evaluation]]  (example-of: public leaderboard built on comparative evaluation and win rates)

## Provenance
- [[sources/ch03-ranking-models-with-comparative-evaluation]]
