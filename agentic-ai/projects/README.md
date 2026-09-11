# Agentic AI Projects

This suite turns the concepts in [`../overview.md`](../overview.md) and
[`../workflow.md`](../workflow.md) into three leveled, evaluable projects.
Every brief keeps levels of difficulty as checkpoints for everyone.

## Projects

| Project | Main ideas | Starting point |
|---|---|---|
| [01-rag-hr-assistant](./01-rag-hr-assistant/) | PDF chunking, embeddings, vector search, citations, "I don't know" discipline | [README](./01-rag-hr-assistant/README.md) |
| [02-analysis-agent-chatbi](./02-analysis-agent-chatbi/) | NL-to-SQL, views/procedures/functions, safe execution, charts, business reports | [README](./02-analysis-agent-chatbi/README.md) |
| [03-deep-research-agent](./03-deep-research-agent/) | Firecrawl research, reflexion, knowledge graph, SWOT, opportunity scoring | [README](./03-deep-research-agent/README.md) |

## Suggested study order

1. Complete RAG Level 1 with local PDFs and ChromaDB before adding
   multi-query/hybrid search.
2. Build the ChatBI ERD and views first; SQL correctness comes before agents
   and charts.
3. Keep Deep Research use-case specific (one company + one domain), not
   general. Optionally merge with RAG so it knows company info.

Each project README includes goal, data source, tech stack, Level 1/2/3
checklists, evaluation targets, and production extensions. The checklists are
intentionally demanding and may take months — لو اتحطت فالسي في هتبقا تقيلة
جدا خاصة لو بتقدم على شغل فيه اجينتك وكده.

## Contributing

Keep examples deterministic, local-first, and free of secrets. Explain any
optional service or dependency in the relevant project README and preserve the
same public interfaces when extending an example.

📬 **Contributing:** Questions and improvements are welcome via
[GitHub](https://github.com/Yosef-Ibrahim).
