# PROJECT: ANALYSIS AGENT (DATA INSIGHTS)

## GOAL

Build a "ChatBI" tool that connects to a database, runs SQL queries, and provides
statistical analysis + visualizations based on natural language questions.

## DATA SOURCE

- PostgreSQL or SQLite database
- Pre-loaded with a dataset (10,000+ rows)
- Must have: missing values, inconsistent data, duplicate entries
- دور على اي داتا سيت مش حوار بس يفضل تكون مبيعات مثلا وطبعا هتحولها لداتا بيز فهتحتاج تعمل erd الاول وتديزاين كويس
- DB Must include:
    - Views (e.g., monthly_sales_view, top_customers_view)
    - Stored procedures (e.g., calculate_commission, update_inventory)
    - Functions (e.g., get_fiscal_quarter, days_between_orders)
    - Triggers (optional, but nice to have)
    - Complex joins (3+ tables)
- هتقولي انا مالي بالdb هقولك نفس الكلام فالاغلب بيكون مطلوب منك كل حاجة وعموما جزء ال agentic صعوبته مش فالai صعوبته فالحاجات اللي حواليه

## TECH STACK

نفس الكلام اللي كان فالrag يعتبر وبردو براحتك لو عايز تستخدم حاجات مختلفة

Suggested: LLM Gemini API (free tier), Vector DB ChromaDB where needed,
Frontend Streamlit (or React for interactive charts), Backend FastAPI +
LangGraph/Chain + Pydantic, Deployment Docker.

## WHAT YOU MUST BUILD

### LEVEL 1 (FOUNDATION)

- [ ] Connect to database and show schema preview (tables, columns, sample rows)
- [ ] Generate SQL queries from natural language
- [ ] Execute SQL safely (read-only connection)
- [ ] Show results as a table
- [ ] Basic UI with query input
- [ ] Generate simple charts (bar, line) from query results
- [ ] Dockerfile + docker-compose.yml for local deployment

### LEVEL 2 (INTERMEDIATE) - STRETCH

- [ ] Complex SQL: Handle JOINs (3+ tables), subqueries, CTEs, window functions
- [ ] Smart query generation: Understand which views to use for common questions
- [ ] Query optimization: Explain plan analysis, suggest indexes
- [ ] Handle ambiguous queries: Ask clarifying questions to the user
- [ ] Interactive charts (zoom, hover, drill-down) غالبا هتحتاج رياكت او اي فرونت محترم شويه
- [ ] Show streaming: SQL being generated → then results → then chart
- [ ] Caching
- ممكن تدور على حاجة اسمها semantic caching بس حوار شويه

### LEVEL 3 (EXPERT) - ADVANCED

- [ ] Call stored procedures: Agent recognizes when to call a proc vs. write SQL
- [ ] Agent breaks analysis into subtasks (SQL Agent, Analysis Agent, Narrator Agent)
- [ ] Discover hidden correlations and suggest business insights
- [ ] Generate a complete business report with narrative
- [ ] Export report as HTML or PDF
- [ ] Add logging: Save all Q&A pairs to a local SQLite database
- او استخدم langsmith

## EVALUATION

- [ ] 20 hidden test queries covering:
    - Simple SELECT with WHERE
    - JOINs (2-4 tables)
    - Aggregations (GROUP BY, HAVING)
    - Window functions
    - Subqueries and CTEs
    - View queries
    - Stored procedure calls
- [ ] Measure:
    - SQL execution success rate → Target: 95% on first try
    - Query accuracy: Results match ground truth (provided by instructor)
    - Query efficiency: Uses indexes, no full table scans where avoidable
- [ ] LLM-as-Judge to grade:
    - SQL readability → Score > 8/10
    - Chart appropriateness → Score > 8/10
- [ ] Query latency: Response time < 10 seconds for 90% of queries

## ⚠️ Notes

- Always use a read-only connection for generated SQL.
- Design the ERD and DB objects before adding agents; that is where most
  difficulty lives.
- Keep Arabic notes in Arabic when extending this brief.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
