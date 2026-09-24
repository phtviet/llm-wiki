---
type: concept
sources: [ch07-quantization]
---
# Quantization

Quantization reduces the number of bits used to represent a model's values, cutting its memory footprint. A 10B-parameter model in 32-bit format requires 40 GB for its weights, but the same model in 16-bit format requires only 20 GB (AIE p.328). It is cheap, effective, straightforward, and generalizes across tasks and architectures; 'low precision' generally refers to any format with fewer bits than standard FP32 (AIE p.328). Strictly, quantization means converting to an integer format, but the term is commonly used, and used in the book, to refer to any precision-reduction technique (AIE p.328).

Two decisions define a quantization approach: what to quantize, and when. Weights and activations are the major memory contributors during inference; weight quantization is more common than activation quantization since it has a more stable impact on performance with less accuracy loss (AIE p.328). On timing, quantization can happen post-training or during training. Post-training quantization (PTQ) -- quantizing a model after it is fully trained -- is by far the most common approach and the one most relevant to application developers who do not train models themselves (AIE p.328).

Reduced precision also speeds up computation: it allows larger batch sizes and faster arithmetic, which lowers both inference latency and training time, though format-conversion overhead can offset this gain (AIE p.329-330). The downside is accuracy loss -- each precision conversion causes a small value change, many of which can compound into a large performance change, and out-of-range values can convert to infinity or an arbitrary value (AIE p.330). Inference in lower precision is now standard practice: a model is trained in a higher-precision format to maximize performance, then quantized for inference, with PTQ offered for free by major frameworks such as PyTorch, TensorFlow, and Hugging Face transformers, as well as on-device frameworks like TensorFlow Lite and PyTorch Mobile (AIE p.330).

Training-time quantization is less common than PTQ but gaining traction, pursued for two distinct goals: producing a model that performs well in low precision at inference, or reducing training time and cost by training on cheaper hardware or training a larger model on the same hardware (AIE p.331). [[quantization-aware-training]] addresses the first goal; training directly in lower precision, often via [[mixed-precision-training]], can address both goals but is harder since backpropagation is more sensitive to lower precision (AIE p.331). Quantization has a floor: values cannot use fewer than 1 bit, though 1-bit approaches have been attempted, such as BinaryConnect, Xnor-Net, and BitNet (AIE p.329).

## Key figures
- 10B-parameter model: 40 GB in FP32 vs. 20 GB in 16-bit format (AIE p.328)
- Adding two numbers bit by bit takes 32t nanoseconds at 32 bits vs. 16t nanoseconds at 16 bits, for per-bit time t (AIE p.329)
- Apple's 2024 on-device quantization scheme mixes 2-bit and 4-bit formats, averaging 3.5 bits-per-weight (AIE p.329)

## Examples
- [[bitnet-b1-58]]  (1.58-bit transformer language model, comparable to 16-bit Llama 2 up to 3.9B parameters)

## Related
- [[mixed-precision-training]]  (part-of: mixed precision is one route to training-time quantization, keeping some values in higher precision and others lower)
- [[quantization-aware-training]]  (part-of: QAT is one training-time quantization technique, aimed at inference quality rather than training speed)
- [[numerical-representations]]  (prerequisite: quantization moves values between the formats this concept defines)
- [[memory-bottleneck]]  (see-also: quantization is a primary technique for addressing the memory bottleneck)
- [[qlora]]  (example-of: QLoRA applies 4-bit quantization -- via Dettmers et al.'s NF4 -- to enable large-model finetuning on limited hardware)

## Provenance
- [[sources/ch07-quantization]]
