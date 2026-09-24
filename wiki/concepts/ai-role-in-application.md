---
type: concept
sources: [ch01-use-case-evaluation]
---
# AI Role in Application

How AI functions within a product shapes its development and requirements. The book (citing an Apple framework) identifies three dimensions along which an AI feature's role can be classified (AIE p.30).

**Critical or complementary**: if the app still works without AI, AI is complementary (e.g., Gmail's Smart Compose); if it cannot, AI is critical (e.g., Face ID). The more critical AI is, the higher the accuracy and reliability bar, since users tolerate mistakes less when AI is core to the product (AIE p.30).

**Reactive or proactive**: a reactive feature responds to a user's request or action (e.g., a chatbot), while a proactive feature surfaces output when an opportunity arises (e.g., traffic alerts). Reactive features usually need low latency since they occur in response to events; proactive features can be precomputed and shown opportunistically, so latency matters less, but because users didn't ask for them, they carry a higher quality bar to avoid feeling intrusive (AIE p.30).

**Dynamic or static**: dynamic features update continually with [[user-feedback]] (e.g., Face ID adapting as a face changes, or per-user finetuning and memory features like ChatGPT's), while static features update only periodically, such as when a shared model is upgraded (e.g., object detection in [[google-photos]]) (AIE p.30).

## Key figures
None.

## Examples
- [[customer-support-chatbot]]  (reactive feature; AI role can range from suggesting responses to fully automating them)

## Related
- [[human-in-the-loop]]  (see-also: both concern how much AI acts independently of humans in a product)
- [[customer-support-chatbot]]  (example-of: the book's running example showing AI responses ranging from suggestion to full automation)
- [[user-feedback]]  (see-also: mentioned in this page's text)
- [[google-photos]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch01-use-case-evaluation]]
