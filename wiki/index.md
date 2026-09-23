## Model compression
- [[model-distillation]] -- trains a small student model to mimic a larger teacher
- [[distilbert]] -- BERT distilled from scratch into a smaller, faster model
- [[alpaca]] -- Llama-7B finetuned on text-davinci-003 outputs to mimic it
- [[nemotron-4]] -- NVIDIA model trained on synthetic teacher data that surpassed its teacher

- [[inference-optimization]] -- making models faster and cheaper, including quantization, distillation, and parallelism
- [[ai-product-maintenance]] -- planning for how an AI product must evolve as the fast-moving foundation model landscape changes
- [[intelligent-data-processing]] -- using AI to extract structured information from unstructured data, e.g. contracts and receipts
## Prompt engineering
- [[ai-engineering-vs-full-stack-engineering]] -- how foundation models shift app-development priorities toward AI interfaces, prompt engineering, and evaluation
- [[model-adaptation]] -- umbrella term for adapting a pretrained model, split into prompt-based techniques and finetuning
- [[finetuning]] -- continuing training from a pretrained model's weights to adapt it

- [[application-development]] -- AI engineering stack layer covering evaluation, prompt engineering, and AI interface
- [[ai-engineering-vs-ml-engineering]] -- how foundation models shift priorities from model development toward adaptation and evaluation
- [[ai-coding-tools]] -- coding as the most popular generative AI use case, spanning general and task-specialized tools
- [[ai-engineering]] -- building applications on top of foundation models, and why the term supplanted ML engineering/MLOps
- [[prompt-engineering]] -- crafting detailed instructions and examples to steer a foundation model's output
- [[retrieval-augmented-generation]] -- supplementing model instructions with a retrieved external database
- [[information-aggregation]] -- using AI to filter, digest, and summarize overwhelming information like emails and news
- [[conversational-bots]] -- AI systems for finding information, companionship, customer support, and game NPCs, across text, voice, and 3D interfaces
- [[model-as-a-service]] -- organizations offering large trained models to others as a service, lowering the barrier to building AI applications
- [[use-case-evaluation]] -- deciding why and how to build an AI application, weighing risk, buy-vs-build, AI's role, and defensibility
- [[human-in-the-loop]] -- involving humans in AI decision-making, from mandatory oversight to full automation
- [[ai-product-defensibility]] -- what moat protects an AI product given the low barrier to building on foundation models
- [[ai-writing]] -- using foundation models to draft, edit, and rewrite text across consumer, creative, and enterprise use cases
## Training fundamentals
- [[pre-training]] -- training a model from scratch with randomly initialized weights
- [[post-training]] -- training after pre-training, conceptually the same as finetuning
- [[dataset-engineering]] -- curating, generating, and annotating data for training and adaptation
- [[model-development]] -- AI engineering stack layer covering modeling/training, dataset engineering, and inference optimization

- [[language-model]] -- encodes statistical information about language; completion-based, split into masked and autoregressive types
- [[token]] -- basic unit a language model operates on; characters, words, or word-pieces
- [[masked-language-model]] -- predicts missing tokens using both preceding and following context, e.g. BERT
- [[autoregressive-language-model]] -- predicts the next token from preceding context; today's dominant generative approach
- [[self-supervision]] -- infers labels from input data itself, overcoming the data-labeling bottleneck to scale training
- [[foundation-model]] -- large-scale, general-purpose model built on many modalities, adaptable to a wide range of downstream tasks
- [[multimodal-model]] -- model that conditions generation on more than one data modality, e.g. text and images
- [[usefulness-threshold]] -- the quality/latency/cost/fairness bar an AI product must clear before shipping to customers
- [[milestone-planning]] -- planning how to reach a product's goals, accounting for the last-mile challenge from demo to product
- [[competitive-advantage]] -- technology, data, and distribution as the three sources of competitive advantage in AI, and how startups can out-compete incumbents
- [[success-metrics]] -- defining business-impact metrics to measure whether an AI application succeeds
- [[ai-engineering-stack]] -- the three layers of any AI application stack: application development, model development, and infrastructure
- [[infrastructure]] -- bottom layer of the AI stack, covering model serving, data/compute management, and monitoring
## Evaluation
- [[evaluation]] -- assessing models and applications, harder for foundation models' open-ended outputs

## People and tools
- [[github-copilot]] -- code completion tool, one of the earliest production successes of foundation models
- [[clip]] -- OpenAI's embedding model trained on 400M image-text pairs via natural language supervision
- [[linkedin]] -- reported reaching 80% of desired AI product experience in one month, then underestimating the rest

- [[calendly]] -- example of a startup product that could have been a Google Calendar feature
- [[mailchimp]] -- example of a startup product that could have been a Gmail feature
- [[photoroom]] -- example of a startup product that could have been a Google Photos feature; author is an investor
- [[grammarly]] -- writing assistant app that finetunes a model for fluency, coherence, and clarity
## Sources
- [[sources/ch01-planning-ai-applications]] -- Chapter 1 closing section on AI use cases and planning applications, book p.28
- [[sources/ch01-setting-expectations]] -- Chapter 1 closing section on competitive advantage and setting success metrics, book p.32
- [[sources/ch01-summary]] -- Chapter 1 closing summary recapping the chapter and contrasting product-first vs. data-first workflows, book pp.47-48
- [[sources/ch01-three-layers-of-the-ai-stack]] -- Chapter 1 section on the three layers of the AI stack and a GitHub repository landscape analysis, book pp.37-38
- [[sources/ch01-use-case-evaluation]] -- Chapter 1 section on evaluating AI use cases: risk, buy-vs-build, AI's role, and defensibility, book pp.29-31
