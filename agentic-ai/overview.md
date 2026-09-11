# Agentic AI Overview

## What agentic AI adds

An agentic system combines an LLM with tools, memory, retrieval, and a control
loop. The useful mental model is:

1. User task defines the goal, constraints, and success criteria.
2. Tools give the model actions (retrieval, SQL execution, web search/scrape,
   charting, export).
3. Memory and state carry context across turns and subtasks.
4. A loop (LangGraph / LangChain) plans, acts, observes, and reflects.
5. Logging and evaluation decide whether the agent is actually improving.

The three projects in this track isolate three loops: grounded answering (RAG),
database reasoning (ChatBI), and open-ended web research (Deep Research).

## Prerequisites

Be comfortable with Python, REST APIs, basic SQL, Docker and Docker Compose,
and train/validation/test discipline from `machine-learning/`. No private data
or paid services are needed for the baseline: use local PDFs, SQLite/Postgres
local, ChromaDB local, Streamlit, FastAPI, and free-tier APIs.

## Project map

| Project | What it demonstrates | Important reading note |
| --- | --- | --- |
| [`01-rag-hr-assistant`](projects/01-rag-hr-assistant/README.md) | Loads HR policy PDFs, chunks, embeds, retrieves top-k, generates cited answers, says "I don't know" when out-of-scope. | ⚠️ Level 1 is what everyone builds. Level 3 (self-correction, thresholds, logging, optimized Docker) is what makes it hireable. |
| [`02-analysis-agent-chatbi`](projects/02-analysis-agent-chatbi/README.md) | Connects to a database, generates safe read-only SQL, shows tables and charts, handles JOINs/views/procedures, writes business reports. | ⚠️ Agentic difficulty here is mostly DB design (ERD, views, procedures, functions, triggers) and frontend, not only the LLM call. |
| [`03-deep-research-agent`](projects/03-deep-research-agent/README.md) | Takes company + domain, searches/scrapes with Firecrawl, reflexion loop, structured report, knowledge graph, opportunity scoring. | ⚠️ Keep it use-case specific, not general. General research agents already exist and perform poorly without focus. |

Shared tech suggestions (optional, use what you want): LLM Gemini API free tier
via Google Studio, Vector DB ChromaDB local, Backend FastAPI + LangGraph/Chain
+ Pydantic, Frontend Streamlit (or React), Deployment Docker. The projects
explain why a frontend and Docker matter even if you prefer backend work: in
real jobs you usually deliver a complete system.

## ⚠️ Corrections to carry forward

- Do not fit, tune, or select prompts on the hidden test set.
- Do not report a demo score without citations, logging, and out-of-scope
  handling.
- A 0.5 similarity threshold, top-k value, or chunk size is a policy choice,
  not a universal truth. Measure it per use case.
- Free-tier APIs, Firecrawl, and model downloads require network access and
  quota management. Cache aggressively (ChromaDB, SQLite, semantic caching).
- What distinguishes you from any LangChain/n8n user is strength in the
  surrounding software: DB design, APIs, frontend, Docker, evaluation.

## Suggested order

Read this overview, then [`resources.md`](resources.md), run through
[`projects/01-rag-hr-assistant/README.md`](projects/01-rag-hr-assistant/README.md)
Level 1, then ChatBI Level 1, then Deep Research Level 1. Only after all three
baselines work, climb to Level 2 and Level 3 in the same order. Finish with
[`workflow.md`](workflow.md) to turn an experiment into a defensible artifact.

المشاريع ديه مش هتخلص بسرعة اطلاقا وممكن تاخد بالشهور بس لو اتحطت فالسي في هتبقا تقيلة جدا خاصة لو بتقدم على شغل فيه اجينتك وكده.

## Questions to ask while building an agent

- Which rows/documents are used for retrieval, and which questions are held out?
- Is "I don't know" triggered by a measured threshold or by wishful prompting?
- Does the SQL agent use read-only connections, views, and procedures correctly?
- Are citations clickable and verifiable against real URLs/documents?
- Are errors concentrated in retrieval, tool choice, prompting, or evaluation?

⚠️ A demo can be valuable as a record while still being unsafe as a template.
Rebuild quota-heavy, download-heavy, or unlogged cells from `workflow.md`
before applying them to a new project.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
