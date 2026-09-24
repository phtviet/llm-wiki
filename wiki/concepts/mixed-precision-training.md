---
type: concept
sources: [ch07-memory-bottlenecks]
---
# Mixed-Precision Training

Mixed-precision training is a training approach in which some operations are done in higher numerical precision (e.g., 32-bit) and others in lower precision (e.g., 16-bit or 8-bit). It exists because training is more sensitive to numerical precision than inference, making it harder to train a model uniformly in low precision (AIE p.320).

## Key figures
None beyond the precision levels named above (16-bit/8-bit vs. 32-bit), which are illustrative rather than load-bearing.

## Examples
None named in this section.

## Related
- [[quantization]]  (contrast: quantization uniformly lowers precision for storage/inference, while mixed precision combines precision levels during training)
- [[memory-bottleneck]]  (part-of: how training addresses its heightened sensitivity to numerical precision relative to inference)

## Provenance
- [[sources/ch07-memory-bottlenecks]]
