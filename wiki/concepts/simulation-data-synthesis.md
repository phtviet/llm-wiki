---
type: concept
sources: [ch08-traditional-data-synthesis-techniques]
---
# Simulation (Data Synthesis)

Simulation generates training data by running experiments in a virtual environment instead of the real world, where real experiments can be expensive or dangerous (AIE p.385). A canonical example: rather than releasing an actual horse onto a highway to test a self-driving car's reaction, the scenario is simulated. Self-driving simulation engines include CARLA, Waymo's SimulationCity, and Tesla's simulation of San Francisco (AIE p.385).

Simulation is also common for robotics, where multiple simulated joint-movement scenarios are run and only the successful outcomes (e.g., successfully pouring coffee) are kept as training data. It is valuable for generating data on rare events—an IPO, a bankruptcy, a material defect, or an extreme weather scenario—since real examples are scarce (AIE p.386). Simulation is also used to generate tool-use data for AI agents: given a query, different action sequences are simulated, executed, and validated, and the most efficient sequence becomes the annotated response, since human-generated actions are not always optimal (AIE p.386).

A simulated model that works virtually may not work in the real world, but a model that fails in simulation will likely also fail in reality; simulations remain simplifications of the real world. Sim2Real is the subfield focused on adapting simulation-trained algorithms to real-world deployment (AIE p.386).

## Key figures
None.

## Related
- [[data-synthesis]]  (part-of: a traditional precursor technique to AI-powered data synthesis)
- [[rule-based-data-synthesis]]  (contrast: generates data via simulated environments vs. predefined templates)
- [[tool-use-data]]  (example-of: simulation is one method for generating tool-use training data)

## Provenance
- [[sources/ch08-traditional-data-synthesis-techniques]]
