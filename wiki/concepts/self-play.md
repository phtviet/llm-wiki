---
type: concept
sources: [ch08-ai-powered-data-synthesis]
---
# Self-Play

Self-play is a data-generation approach where an AI system generates training data by playing against itself, letting simulated matches run far faster than games between humans. OpenAI used a simulator so its Dota 2 bot could play roughly 180 years' worth of games every day, learning and refining strategies by playing against itself (OpenAI, 2019) (AIE p.387). DeepMind similarly used self-play to collect data from millions of Go games to train AlphaGo (Silver et al., 2016) (AIE p.387).

Self-play is not limited to game bots; it generalizes to agents. Two AI instances can negotiate against each other using different strategies to compare which works better, or one instance can play a customer with issues while another plays the support agent (AIE p.387).

## Key figures
- OpenAI's Dota 2 self-play simulator generated approximately 180 years' worth of games per day (AIE p.387)

## Examples
- [[alphafold]]

## Related
- [[data-synthesis]] (part-of: self-play is one technique for generating simulated training data)

## Provenance
- [[sources/ch08-ai-powered-data-synthesis]]
