---
type: concept
sources: [ch05-organize-and-version-prompts]
---
# Prompt Organization and Versioning

Separating prompts from application code -- for example putting prompts in a dedicated `prompts.py` file and importing them into application logic -- is good practice. It yields four benefits: reusability across multiple applications, the ability to test code and prompts separately, improved readability, and easier collaboration, since subject matter experts can help write prompts without being distracted by code (AIE p.233).

When an application accumulates many prompts, each prompt benefits from metadata (model name, creation date, application, creator) so prompts can be searched by model or use case, for example by wrapping each prompt in a typed object. A prompt template can also carry the model endpoint URL, ideal sampling parameters (temperature, top-p), the input schema, and the expected output schema for structured outputs (AIE p.234).

If prompt files live in a git repository, they can be versioned with git, but this couples all applications sharing a prompt to whatever version is committed: when the prompt is updated, every dependent application is forced onto the new version, making it hard for one team to stay on an older version. Many teams instead use a separate prompt catalog that explicitly versions each prompt, letting different applications pin different versions, provides metadata and search, and can track which applications depend on a prompt to notify owners of newer versions (AIE p.234-235).

## Key figures
None.

## Examples
- [[dotprompt]]  (Google Firebase's .prompt file format)

## Related
- [[prompt-engineering]]  (part-of: organizing and versioning prompts is a prompt-engineering best practice)
- [[structured-outputs]]  (see-also: prompt templates can declare the expected output schema for structured outputs)
- [[prompt-catalog]]  (part-of: the prompt catalog is the recommended alternative to git-versioning prompts alongside code)

## Provenance
- [[sources/ch05-organize-and-version-prompts]]
