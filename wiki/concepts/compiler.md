---
type: concept
sources: [ch09-model-optimization]
---
# Compiler (ML)

A model script specifies a series of operations to execute a model. Running that code on hardware such as a GPU requires converting it into a language compatible with that hardware, a process called lowering. A tool that lowers code for specific hardware is called a compiler, bridging ML models and the hardware they run on; during lowering, operations are converted into specialized kernels where possible to run faster on the target hardware (AIE p.438-439).

Compilers can be standalone tools, such as Apache TVM and MLIR (Multi-Level Intermediate Representation), or integrated into ML/inference frameworks, such as torch.compile (PyTorch), XLA (originally from TensorFlow, with an open source version OpenXLA), and the compiler built into TensorRT (optimized for NVIDIA GPUs). AI companies may build their own compilers with proprietary kernels to speed up their own workloads (AIE p.439).

## Key figures
None.

## Related
- [[kernel]]  (prerequisite: compilers produce or invoke kernels during the lowering process)

## Provenance
- [[sources/ch09-model-optimization]]
