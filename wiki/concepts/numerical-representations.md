---
type: concept
sources: [ch07-numerical-representations]
---
# Numerical Representations

Numerical values in neural networks are traditionally represented as floating point numbers. Reducing the number of bytes used to represent each value directly reduces a model's memory footprint: halving the per-value memory halves the memory needed for the model's weights (AIE p.325). The most common floating-point formats follow the IEEE 754 standard, and numbers can also be represented as integers, a less common but increasingly popular alternative (AIE p.325-326).

Each float format devotes 1 bit to sign, and splits the rest between range bits (how wide a range of values the format can represent) and precision bits (how precisely a number can be represented). More range bits means a wider representable range, similar to having more digits; fewer precision bits means a number is represented less exactly, e.g. 10.1234 rounded to two decimal digits becomes 10.12 (AIE p.326). Formats with more total bits are considered higher precision, and converting a number from a high-precision format to a low-precision one (e.g. FP32 to FP16) reduces its precision and can introduce errors (AIE p.326-327).

BF16 and FP16 use the same number of bits but allocate them differently: BF16 has more range bits and fewer precision bits than FP16, letting it represent larger values that would be out-of-bound for FP16, at the cost of being less precise. For example, 1234.56789 converts to 1235.0 in FP16 (a 0.035% change) but 1232.0 in BF16 (a 0.208% change) (AIE p.327). Loading a model in the wrong numerical format from the one it was trained/released in can significantly degrade quality; Llama 2 shipped with BF16 weights, and teams that loaded it in FP16 instead found quality much worse than advertised (AIE p.328). The right format to use depends on the distribution of a workload's numerical values, how sensitive the workload is to small numerical changes, and the underlying hardware (AIE p.328).

## Key figures
- FP32: 32 bits (4 bytes), single precision (AIE p.325)
- FP64: 64 bits (8 bytes), double precision (AIE p.325)
- FP16: 16 bits (2 bytes), half precision (AIE p.325)
- Example conversions from FP32: 1234.56789 -> 1235.0 in FP16 (0.035% change) vs. 1232.0 in BF16 (0.208% change) (AIE p.327)

## Examples
- [[fp32]]
- [[fp16]]
- [[bf16]]
- [[tf32]]
- [[int8-int4]]

## Related
- [[quantization]]  (prerequisite: quantization reduces bits per weight by converting between these numerical formats)
- [[memory-bottleneck]]  (part-of: numerical representation choice is one driver of a model's memory footprint, alongside parameter count and trainable parameters)
- [[llama-2]]  (example-of: shipped in BF16, illustrating the cost of loading a model in the wrong format)

## Provenance
- [[sources/ch07-numerical-representations]]
