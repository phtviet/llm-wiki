---
type: concept
sources: [ch09-ai-accelerators]
---
# Power Consumption (Accelerators)

Chips compute via transistors switching on and off, which consumes energy and generates heat; efficient use of an accelerator's billions of transistors consumes substantial energy and requires cooling, which itself adds to a data center's overall energy consumption (AIE p.424). Chip energy consumption is a growing environmental concern, pressuring companies to invest in green data centers. Electricity supply is a bottleneck to scaling up compute, and is also a major factor (alongside network latency and geopolitics) in siting large GPU data centers (AIE p.423-424).

Accelerators specify power consumption via **maximum power draw** (peak power under full load) or the proxy metric **TDP** (thermal design power, the maximum heat a cooling system must dissipate under typical workloads). For CPUs and GPUs, maximum power draw is roughly 1.1 to 1.5 times TDP, though the exact relationship varies by architecture and workload (AIE p.425). Cloud provider customers do not need to manage cooling or electricity directly, but these figures remain useful for understanding environmental impact (AIE p.425).

## Key figures
- NVIDIA A100: 54 billion transistors; NVIDIA H100: 80 billion transistors (AIE p.424)
- NVIDIA H100 at peak for a year: ~7,000 kWh, vs. ~10,000 kWh average annual US household electricity consumption (AIE p.424)
- Maximum power draw is roughly 1.1-1.5x TDP for CPUs and GPUs (AIE p.425)

## Examples
- [[gpu]]  (A100/H100 transistor counts and H100 annual energy consumption)

## Related
- [[ai-accelerator]]  (part-of: power consumption is one of three characteristics used to evaluate an accelerator)
- [[gpu]]  (example-of: A100 and H100 transistor counts and energy use)
- [[scaling-bottlenecks]]  (see-also: electricity is identified as a bottleneck to scaling up compute)

## Provenance
- [[sources/ch09-ai-accelerators]]
