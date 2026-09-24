---
type: entity
sources: [ch08-data-quality]
---
# LIMA (Less Is More for Alignment)

LIMA is a study (Zhou et al., 2023) demonstrating that a 65B-parameter Llama model finetuned on a small set of carefully curated prompts and responses can rival a much larger, more heavily trained model on output quality. It is the book's central evidence that data quality can substitute for [[data-quantity]] in finetuning (AIE p.368).

The downside observed is that LIMA is not as robust as product-grade models, since so few examples cannot cover the range of behaviors a production system needs (AIE p.368).

## Key figures
- Finetuned with 1,000 carefully curated prompts and responses (AIE p.368)
- Produces answers equivalent to or strictly preferred over [[gpt-4|GPT-4]] in 43% of cases, as judged by human annotators (AIE p.368)

## Related
- [[data-quality]]  (example-of: demonstrates that curated data quality can outperform data volume)
- [[yi-model-family]]  (see-also: another case of small curated instruction sets outperforming larger noisy ones)
- [[data-quantity]]  (see-also: mentioned in this page's text)
- [[gpt-4]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch08-data-quality]]
