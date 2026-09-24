---
type: concept
sources: [ch05-evaluate-prompt-engineering-tools]
---
# Prompt Engineering Tools

Because the number of possible prompts for a task is infinite and manual prompt engineering is time-consuming, many tools have been developed to aid and automate the process. Some tools automate the whole workflow: given input/output formats, evaluation metrics, and evaluation data, they automatically search for a prompt or chain of prompts that maximizes the metrics, functionally similar to autoML tools finding optimal hyperparameters for classical ML models (AIE p.230). A common approach is to use AI models themselves to write, critique, and improve prompts, or to generate in-context examples (AIE p.230). Other tools assist only part of the workflow, such as guiding models toward [[structured-outputs]], or perturbing a prompt (e.g. replacing a word with a synonym, or rewriting it) to test which variation performs best (AIE p.232).

Used well, these tools can meaningfully improve system performance, but they carry real risks. They often generate hidden [[model-api]] calls that can quickly exhaust an API budget: a tool testing ten prompt variations against 30 evaluation examples, at one call per variation, already produces 300 calls, and multiple calls per prompt (one to generate, one to validate format, one to score) multiply that further, especially if the tool is given free rein to build long prompt chains (AIE p.232). Tool developers can also make mistakes -- using the wrong template for a given model, concatenating tokens instead of raw text, or leaving typos in default prompt templates -- and any tool's default prompts can change without warning as the tool evolves, adding system complexity and error surface as more tools are stacked together (AIE p.232). Following a keep-it-simple principle, the book suggests starting with hand-written prompts (no tool) to build a better understanding of the model and the task's requirements, and, when a tool is used, always inspecting its generated prompts and tracking its API call volume (AIE p.233).

## Key figures
- Example: 30 evaluation examples x 10 prompt variations = 300 API calls at one call per variation, before accounting for additional generate/validate/score calls per prompt (AIE p.232)

## Examples
- [[promptbreeder]]  (evolutionary-strategy prompt optimizer)
- OpenPrompt (Ding et al., 2021) and DSPy (Khattab et al., 2023) -- full-workflow prompt optimization tools
- TextGrad (Yuksekgonul et al., 2024) -- Stanford AI-powered prompt optimization tool
- Guidance, Outlines, Instructor -- tools guiding models toward [[structured-outputs]]
- LangChain -- general tool whose default critique prompt was found to contain typos

## Related
- [[prompt-engineering]]  (part-of: these tools automate or assist manual prompt engineering)
- [[structured-outputs]]  (see-also: some prompt engineering tools exist specifically to guide models toward structured outputs)
- [[promptbreeder]]  (example-of: an AI-powered prompt optimization tool)
- [[model-api]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch05-evaluate-prompt-engineering-tools]]
