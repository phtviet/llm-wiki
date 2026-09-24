---
type: concept
sources: [ch01-ai-engineering-versus-ml-engineering]
---
# Application Development

Application development is the [[ai-engineering]] stack layer where differentiation is gained when many teams use the same [[foundation-model]], unlike traditional ML engineering where proprietary models themselves were the differentiator (AIE p.44). It consists of three responsibilities: [[evaluation]], [[prompt-engineering]], and AI interface (AIE p.44).

AI interface means building an interface for end users to interact with an AI application. Before foundation models, only organizations with resources to develop AI models could build AI applications, and these were usually embedded into existing products (e.g., fraud detection in Stripe, Venmo, PayPal; recommenders in Netflix, TikTok, Spotify). With foundation models, anyone can build AI applications, either as standalone products (ChatGPT, Perplexity) or embedded into other products ([[github-copilot]] as a VSCode plug-in, Grammarly as a browser extension, Midjourney via web app or Discord) (AIE p.45). Popular interface forms include standalone web/desktop/mobile apps, browser extensions, chatbots inside chat apps like Slack or Discord, and APIs letting other products integrate AI as plug-ins; interfaces can also be voice-based or embodied in AR/VR. New interfaces also change how [[user-feedback]] is collected: conversational interfaces make giving feedback easier for users but harder to extract systematically (AIE p.45-46).

## Key figures
None.

## Related
- [[model-development]]  (contrast: the other main layer of the AI engineering stack, focused on the model rather than the application)
- [[evaluation]]  (part-of: one of its three responsibilities)
- [[prompt-engineering]]  (part-of: one of its three responsibilities)
- [[foundation-model]]  (see-also: mentioned in this page's text)
- [[ai-engineering]]  (see-also: mentioned in this page's text)
- [[github-copilot]]  (see-also: mentioned in this page's text)
- [[user-feedback]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch01-ai-engineering-versus-ml-engineering]]
