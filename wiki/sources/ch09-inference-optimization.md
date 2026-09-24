---
type: source
label: AIE
title: AI Engineering
author: Chip Huyen
publisher: O'Reilly
year: 2024
pages: printed book pages
---
# AIE -- AI Engineering (Chip Huyen, O'Reilly, 2024)

Immutable source. Citation label **AIE**. Cite as (AIE p.NNN) using printed book pages.
Covered by this ingest: Chapter 9 introduction, 'Inference Optimization', book pp.405-406.

This chapter-opening section introduces inference optimization as the discipline of making trained models faster and cheaper to run, distinct from earlier chapters' focus on making models better. It frames optimization as occurring at three levels -- model, hardware, and service -- and notes the field is interdisciplinary, spanning model researchers, application developers, system engineers, compiler designers, hardware architects, and data center operators. It previews that the chapter will focus mostly on model- and service-level optimization plus an overview of AI accelerators, and will cover performance metrics and trade-offs, including cases where a single technique (e.g. reduced precision) improves both speed and cost, versus cases requiring a trade-off between the two (e.g. faster but pricier hardware). A footnote distinguishes inference (forward pass only) from training (forward and backward passes), and sketches a break-even relationship between total training cost, per-inference charge, and number of inference calls sold, noting it does not apply to third-party API providers reselling open source model inference.
