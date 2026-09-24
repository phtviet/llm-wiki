---
type: concept
sources: [ch04-domain-specific-capability]
---
# Domain-Specific Capability

A model's domain-specific capabilities are the abilities required for a particular application domain, such as coding or understanding a specific language pair, as opposed to general capabilities. They are constrained by a model's configuration (architecture, size) and its training data: a model that never saw Latin during training cannot understand Latin (AIE p.161).

Domain-specific capabilities are evaluated using domain-specific benchmarks, public or private, covering areas such as code generation, code debugging, grade school math, science knowledge, common sense, reasoning, legal knowledge, tool use, and game playing. They are commonly evaluated using [[exact-evaluation]]. Coding capabilities are typically evaluated via [[functional-correctness]], but correctness alone may not capture efficiency, cost, or readability -- efficiency can be exactly evaluated by measuring runtime or memory, while readability has no obvious exact evaluation and often relies on subjective evaluation such as [[ai-as-a-judge]] (AIE p.161-162).

Non-coding domain capabilities are commonly evaluated with close-ended tasks such as multiple-choice questions, because close-ended outputs are easier to verify and reproduce than open-ended generation (AIE p.162). See [[multiple-choice-evaluation]] for how this works and its limitations.

## Key figures
None. This section's load-bearing figures belong to [[multiple-choice-evaluation]] and [[bird-sql]].

## Examples
- [[bird-sql]]  (efficiency-aware text-to-SQL benchmark)
- [[mmlu]]  (multiple-choice benchmark testing domain knowledge)

## Related
- [[exact-evaluation]]  (part-of: domain-specific capability is commonly evaluated via exact evaluation methods)
- [[functional-correctness]]  (example-of: coding-related domain capability is typically evaluated via functional correctness)
- [[multiple-choice-evaluation]]  (part-of: non-coding domain capabilities are commonly evaluated with close-ended multiple-choice tasks)
- [[generation-capability]]  (contrast: domain-specific capability measures understanding of a domain, generation capability measures coherence/faithfulness of output)

## Provenance
- [[sources/ch04-domain-specific-capability]]
