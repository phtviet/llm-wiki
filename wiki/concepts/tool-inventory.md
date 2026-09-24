---
type: concept
sources: [ch06-tools]
---
# Tool Inventory

A system does not need external tools to be an [[agent]], but without them its capabilities are limited: by itself, a model can typically perform only one action, such as generating text or generating images. External tools make an agent vastly more capable by helping it both perceive its environment (read-only actions) and act upon it (write actions). The set of tools an agent has access to is called its tool inventory (AIE p.278).

More tools give an agent more capabilities, but the more tools there are, the more challenging it is for the agent to understand and utilize them well. Deciding what and how many tools to give an agent requires experimentation to find the right set (AIE p.278). Three categories of tools are worth considering: [[knowledge-augmentation]], [[capability-extension]], and tools that let an agent act upon its environment via [[write-actions]] (AIE p.278).

## Key figures
None.

## Examples
- [[knowledge-augmentation]]
- [[capability-extension]]
- [[write-actions]]

## Related
- [[agent]]  (prerequisite: an agent's capabilities depend on its tool inventory and planner)
- [[tool-selection]]  (prerequisite: choosing the right tool inventory requires experimentation)
- [[function-calling]]  (see-also: model-provider feature for invoking tools from a tool inventory)

## Provenance
- [[sources/ch06-tools]]
