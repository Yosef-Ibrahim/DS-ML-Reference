# Agentic AI Track

This directory is the home for Agentic AI material: LLM agents that use tools,
memory, retrieval, and evaluation loops to complete multi-step tasks. It covers
RAG assistants, data-analysis (ChatBI) agents, and deep-research agents, with a
practical Docker-first delivery workflow.

## Guides

- [Overview](overview.md): concepts, prerequisites, and a map of the three projects.
- [Resources](resources.md): Arabic video courses and references.
- [Practical workflow](workflow.md): a reproducible agent development process.
- [Projects](projects/README.md): requirements, difficulty levels, and evaluation for all three agents.

## Layout

```text
agentic-ai/
├── README.md
├── overview.md
├── resources.md
├── workflow.md
└── projects/
    ├── README.md
    ├── 01-rag-hr-assistant/
    │   └── README.md
    ├── 02-analysis-agent-chatbi/
    │   └── README.md
    └── 03-deep-research-agent/
        └── README.md
```

Project READMEs hold full requirements, tech stack, level checklists, and
evaluation criteria. No secrets, private company data, or paid API keys are
stored in this track.

## Study route

Begin with [`overview.md`](overview.md) to connect tools, retrieval, memory,
and evaluation. Read [`resources.md`](resources.md) to pick a video path, then
work through [`projects/README.md`](projects/README.md) in order:

1. RAG HR Assistant — retrieval + citations + "I don't know" discipline.
2. Analysis Agent (ChatBI) — NL-to-SQL, safe execution, charts, and reporting.
3. Deep Research Agent — web research, reflexion, knowledge graph, and scored opportunities.

For every agent, follow the same loop: define the task and user, fix the data
and tool contracts, establish a non-agentic baseline, add one capability at a
time, log all runs, and evaluate against a hidden test set before claiming the
agent works. A larger model or more tools is not evidence of a better agent.

## Environment and reproducibility

LLM APIs (e.g. Gemini free tier), vector DBs (e.g. ChromaDB local), Firecrawl,
and web search may require network access and free-tier keys. Never commit API
keys, credentials, private HR data, or downloaded datasets. Record model name
and version, embedding model, chunking policy, retrieval top-k, prompts,
random seeds, package versions, Docker image tags, and evaluation scores.
Prefer local-first components (SQLite, ChromaDB local, Docker Compose) so a
baseline remains reproducible without paid services.

Use free-tier quotas carefully: create separate test keys, cache search and
embedding results, and log usage. Quota exhaustion during evaluation is an
engineering failure, not a model failure.

## ⚠️ Correction notes

- Preserved project briefs are study requirements, not production code. Rebuild
  them with `workflow.md` before reuse.
- Do not treat a demo that answers 5 questions as an evaluated RAG system.
  Use the RAGAS, SQL-accuracy, and G-Eval targets in `projects/`.
- Do not skip Docker, logging (SQLite / LangSmith), citations, and "I don't
  know" handling to ship a faster demo.
- Agentic difficulty is mostly in the surrounding software (DB design with
  views/procedures/functions, frontend, Docker, caching), not only in the LLM
  call. Budget time for those parts.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
