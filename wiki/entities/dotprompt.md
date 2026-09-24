---
type: entity
sources: [ch05-organize-and-version-prompts]
---
# Dotprompt

Dotprompt is Google Firebase's special `.prompt` file format for storing prompts, one of several such formats proposed by tools alongside Humanloop, Continue Dev, and Promptfile. A Dotprompt file declares the model (e.g. `vertexai/gemini-1.5-flash`), an input schema, an output format and schema, and the prompt template text itself, for example a template that generates a themed restaurant menu item from a `{{theme}}` input variable (AIE p.234).

## Key figures
None.

## Related
- [[prompt-organization-and-versioning]]  (example-of: a concrete .prompt file format for organizing prompts)
- [[structured-outputs]]  (see-also: Dotprompt files declare a JSON output schema for structured outputs)

## Provenance
- [[sources/ch05-organize-and-version-prompts]]
