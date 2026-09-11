# Practical Agentic AI Workflow

## 1. Define the task

Write down the user, goal, allowed tools, forbidden actions, success metric,
and data provenance before writing agent code. An agent is not a substitute
for a clear task or trustworthy tools.

## 2. Fix data and tool contracts

For RAG: collect PDFs, record chunking policy and embedding model. For ChatBI:
design the ERD first, then views, procedures, and functions. For Research:
fix Firecrawl/ArXiv/Wiki access and caching. Version every contract.

## 3. Establish a non-agentic baseline

Use a simple rule or single LLM call first. Then add retrieval, SQL execution,
or web search and record the same metrics. This distinguishes a useful loop
from a merely larger prompt.

## 4. Add one capability at a time

Follow project Levels 1 → 2 → 3. Example order for RAG: chunk/retrieve →
multi-query + hybrid search + memory → self-correction + thresholds + logging.
Log model, prompts, top-k, thresholds, SQL, URLs, seeds, and package versions.

## 5. Evaluate before tuning

Use the hidden test sets in `projects/`: RAGAS faithfulness/relevancy and
"I don't know" accuracy, SQL execution/accuracy/efficiency plus LLM-as-Judge,
G-Eval market coverage/relevance/actionability plus citation checks. Do not
tune prompts or thresholds on the test set.

## 6. Log everything

Save all Q&A pairs to local SQLite or LangSmith with timestamps, retrieved
chunks/SQL/URLs, confidence, latency, and user feedback. A run without logs
cannot be debugged or trusted.

## 7. Ship with Docker

Provide `Dockerfile` + `docker-compose.yml` for local deployment. Level 2
uses multi-container setup (API + Frontend + Vector DB). Level 3 optimizes
image size (aim under 500MB where feasible — لو معرفتش توصلها تحت ال500 عادي
بس تكون حاولت وعرفت ازاي ت اوبتميز حاجة زي كده) with health checks. Never
commit keys or private data; pass them via environment.

## 8. Diagnose before scaling

If faithfulness is low, check retrieval before rewriting prompts. If SQL fails,
check schema/views before adding agents. If research misses players, check
search queries before adding reflexion iterations. Inspect a fixed set of
failure examples after every material change.

## 9. Release and monitor

An agent artifact should include prompts, tool schemas, model versions, eval
scores, data window, and rollback image. Monitor input drift, quota usage,
latency, citation validity, and delayed labels; define retraining and rollback
triggers. Scheduled research (e.g. Celery — محتاجة سيرفر وحوارات) must be
explicit about infra cost.

These steps connect the three agentic projects to the same evaluation
discipline used in `machine-learning/iti/evaluation/`; they are not claims
that any demo already performs all of these checks.



## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
