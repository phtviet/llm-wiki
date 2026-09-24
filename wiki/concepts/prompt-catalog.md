---
type: concept
sources: [ch05-organize-and-version-prompts]
---
# Prompt Catalog

A prompt catalog is a separate system that explicitly versions each prompt, so that different applications depending on a shared prompt can use different versions of it rather than being forced onto whatever version is committed in git alongside application code. A prompt catalog also provides each prompt with relevant metadata and supports prompt search, and a well-implemented one can track which applications depend on a given prompt and notify their owners when newer versions become available (AIE p.234-235).

## Key figures
None.

## Related
- [[prompt-organization-and-versioning]]  (part-of: the catalog is the recommended way to version prompts separately from code)
- [[prompt-engineering]]  (prerequisite: builds on the broader practice of separating prompts from code)

## Provenance
- [[sources/ch05-organize-and-version-prompts]]
