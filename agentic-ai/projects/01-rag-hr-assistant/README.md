# PROJECT: RAG (HR ASSISTANT)

## GOAL

Build an internal HR chatbot that answers employee questions about company policies.
If it doesn't know the answer from the policy documents, it must say "I don't know".

## DATA SOURCE

- 50+ pages of HR policy PDFs
- (اكيد مينفعش اديكو داتا الشركة اللي انا فيها فهحاول ادورلكم عالنت بس حاليا شوفو اي داتا واشتغلو بيها حتى لو قلتلو لاي ai يعملها اشطا بردو)
- Topics: vacation policy, benefits, code of conduct, remote work policy
- Must handle: tables, bullet points, numbered lists

## TECH STACK

الحاجات ديه اوبشنال استخدم اللي انت عايزه بس ديه اقتراحات

- LLM: Gemini API (free tier)
- لو دخلت على جوجل ستوديو هتاخد key ببلاش وهيمشيلك الدنيا كتجربة وكده
- Vector DB: ChromaDB (local) او اي حاجة
- Frontend: Streamlit لو حابب تعمله رياكت وتودي براحتك
- بعض الناس هتقولي ليه اعمل فرونت وبتاع بس فعليا فالشغل بيكون مطلوب فالاخر سيستم كامل ومش دايما فيه حد بتاع فرونت فحتى لو هتفايب كود بس عشان تكون جاهز للمستقبل
- Backend: Fastapi (Python) - LangGraph/chain - pydantic
- Deployment: Docker مهم جدا تتعلمه

## WHAT YOU MUST BUILD

انا مقسمها ليفلز لو انت عندك خلفية فاللفل ده خش عاللي بعده
اول ليفل ده اللي هتلاقي كل واحد بيعمله لكن لفل 3 ده اللي بجد بقا ولو حطيته فالسي فيه هينفعك جدا

### LEVEL 1 (FOUNDATION)

- [ ] Load PDFs, chunk them (500-1000 char chunks with 100-200 overlap)
- [ ] Generate embeddings using local model (qwen,bge, ...) or api بس خليك لوكال احسن
- [ ] Store embeddings in any vector db
- [ ] Retrieve top-k chunks and generate answer
- [ ] Simple UI with chat interface
- [ ] Streaming tokens word-by-word مهمة بردو
- [ ] Show citations (e.g., [source: policy.pdf, page 5])
- [ ] If no relevant chunks found: respond "I don't have information about that."
- [ ] Dockerfile + docker-compose.yml for local deployment

### LEVEL 2 (INTERMEDIATE)

- [ ] Multi-Query: Generate 3 rephrased questions, retrieve for all, combine results
- [ ] Explore different chunking techniques and see whats better for this usecase
- [ ] Hybrid Search: Combine vector search + keyword search (BM25) ودور بردو عن طرق السيرش المختلفة
- [ ] Add memory: Handle follow-up questions in the same session
- [ ] Confidence scoring: Show confidence percentage with each answer
- [ ] Docker: Multi-container setup (API + Frontend + Vector DB)

### LEVEL 3 (EXPERT)

- [ ] Self-Correction: Agent critiques its own answer
- اول نقطتين دول اوفر كيل شويه على الcase ديه بس للتعلم
- [ ] Reflection loop: Answer → Critique → Improve → Repeat (max 2 iterations)
- [ ] Implement "I don't know" detection using similarity thresholds
- [ ] Add logging: Save all Q&A pairs to a local SQLite database
- او استخدم langsmith
- [ ] Docker: Optimized image (under 500MB) with health checks لو معرفتش توصلها تحت ال500 عادي بس تكون حاولت وعرفت ازاي ت اوبتميز حاجة زي كده

## EVALUATION

نقطة مهمة اوي وناس كتير مش بتعملها فمشاريعها وديه اللي بتوري ان المشروع شغال كويس اصلا

- [ ] Create a test set of 50 question-answer pairs (20 should be out-of-scope)
- [ ] Use RAGAS framework to measure:
    - Faithfulness (Is the answer grounded in the docs?) → Target: > 0.90
    - Answer Relevancy (Is it on-topic?) → Target: > 0.85
- [ ] Measure "I don't know" accuracy:
    - Should say "I don't know" for 90%+ of out-of-scope questions
    - Should NOT say "I don't know" for in-scope questions (< 5% false negatives)

## ⚠️ Notes

- Do not tune chunking, top-k, or thresholds on the hidden test set.
- Keep Arabic notes in Arabic when extending this brief.
- Never commit API keys or private HR PDFs; use environment variables and local fixtures.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
