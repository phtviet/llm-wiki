---
type: concept
sources: [ch08-traditional-data-synthesis-techniques]
---
# Rule-Based Data Synthesis

Rule-based data synthesis generates data using predefined rules and templates, populated with the help of random generators (e.g., Faker). A transaction template with fields like transaction ID, date, amount, and merchant can be filled in randomly to produce synthetic credit card transactions; many fraud-detection models are first trained on such synthetic data to prove feasibility before being given access to real data (AIE p.383).

Templates are also used to generate structured documents (invoices, resumes, tax forms, contracts, configuration files) and data following a formal grammar, such as regular expressions or math equations. DeepMind trained its Olympiad-level geometry model, [[alphageometry]], using templated synthetic math problems (AIE p.384).

## Key figures
None. The technique carries no figure of its own; AlphaGeometry's example count is entity-specific and lives on its page.

## Examples
- [[alphageometry]]  (geometry model trained on template-generated synthetic problems)

## Related
- [[data-synthesis]]  (part-of: a traditional precursor technique to AI-powered data synthesis)
- [[simulation-data-synthesis]]  (contrast: generates data from predefined templates vs. from simulated environments)
- [[data-augmentation]]  (see-also: both traditional means of expanding training data, though augmentation transforms existing data rather than generating from templates)

## Provenance
- [[sources/ch08-traditional-data-synthesis-techniques]]
