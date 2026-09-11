# PROJECT: DEEP RESEARCH AGENT (MARKET OPPORTUNITIES)

## GOAL

Build an AI research assistant that helps a company identify new business opportunities
in a specific domain. Given a company description and a target domain, the agent
researches market trends, competitors, gaps, and emerging technologies, then produces
a strategic opportunities report.

### EXAMPLE USE CASES

- "We are a small AI consulting firm. Find opportunities in the healthcare sector."
- "We manufacture electric vehicle batteries. Find opportunities in Southeast Asia."
- "We are a fintech startup. Find opportunities in the African mobile payments market."

اختار يوز كيس معينة بلاش تخليه جينرال (مش هيشتغل كويس وفيه مواقع بتعمل كده بالفعل)
ممكن كمان يتدمج مع الراج بحيث انه معاه معلومات الشركة فيعرف يشوف الفرص المناسبة خصيصا لهذه الشركة

## DATA SOURCE

- Firecrawl API (free tier) for web search and scraping
- ArXiv API (free) for academic papers on emerging tech
- Wikipedia API (free) for industry background
- غالبا firecrawl كفاية

## TECH STACK

نفس الكلام فاللي الاتنين اللي فاتو

Suggested: LLM Gemini API (free tier), Vector DB ChromaDB for caching,
Frontend Streamlit (or React), Backend FastAPI + LangGraph/Chain + Pydantic,
Deployment Docker.

## WHAT YOU MUST BUILD

### LEVEL 1 (FOUNDATION) - MANDATORY

- [ ] User inputs: Company name, description, target domain, geography (optional)
- ممكن تخلي الشركة ثابتة او يقدر يجيب معلومات عنها بالفعل عن طريق راج او حاجة
- [ ] Search web using Firecrawl for:
    - Market size and growth projections
    - Key competitors in the domain
    - Current trends and technologies
    - Regulatory environment
- [ ] Scrape top 5 results using Firecrawl extract
- [ ] Generate a summary covering:
    - Market overview
    - Key players
    - Emerging trends
- [ ] Simple UI with input form
- [ ] Show sources/URLs at the bottom

### LEVEL 2 (INTERMEDIATE) - STRETCH

- [ ] Reflexion Loop: Agent writes draft, identifies gaps, generates follow-up questions
    - "What are the unmet needs in this market?"
    - "What are competitors NOT doing well?"
    - "What technologies are disrupting this space?"
- [ ] Search again with follow-up questions (max 3 iterations)
- [ ] Generate structured report with sections:
    - Executive Summary
    - Market Overview (size, growth, trends)
    - Competitive Landscape (top 5 players, SWOT analysis)
    - Gap Analysis (what's missing / underserved)
    - Technology Trends (emerging tech that could disrupt)
    - Regulatory & Risks
    - Recommended Opportunities (3-5 specific recommendations)
    - Action Plan (next steps)
- [ ] Left sidebar: Stream internal monologue (real-time thinking)
- [ ] Main panel: Stream final report markdown
- [ ] Show confidence scores per section
- او اي شكل ui يعجبك بس زي ما قلت قبل كده متهملوش عشان ديه اكتر حاجة اليوزر مهتم بيها

### LEVEL 3 (EXPERT) - ADVANCED

- [ ] Competitor Deep Dive: For each top competitor, extract:
    - Revenue/growth (if available)
    - Product offerings
    - Recent funding/partnerships
    - Customer reviews/sentiment
- [ ] Build a knowledge graph showing:
    - Companies (nodes)
    - Technologies (nodes)
    - Markets (nodes)
    - Relationships: competes_with, supplies_to, operates_in, uses_tech
- [ ] Render graph in frontend using NetworkX + PyVis
- [ ] SWOT Analysis: Generate a proper SWOT matrix (Strengths, Weaknesses, Opportunities, Threats)
- [ ] Opportunity Scoring: Rank recommendations by:
    - Market size
    - Competitive intensity
    - Ease of entry
    - Potential ROI
- [ ] Export report as PDF or DOCX
- [ ] Caching: Store search results in ChromaDB (او اي حاجة) to avoid re-searching

## EVALUATION

- [ ] Test with 3 company-domain pairs (provided by instructor)
- [ ] Use G-Eval (LLM-as-Judge) to grade:
    - Market Coverage (did it miss major players/trends?) → Target: > 8/10
    - Opportunity Relevance (are recommendations relevant to the company?) → Target: > 8/10
    - Actionability (are recommendations specific enough to act on?) → Target: > 7/10
    - Citation Verifiability (do sources exist?) → Target: 95% accuracy
- [ ] Auto-check: All citations must be clickable and point to real URLs
- [ ] Research time: Must complete in < 5 minutes per company-domain pair
- اخر نقطة ديه قاسية شويه وغالبا حاجة زي بتكون scheduled كنت هقولكم ممكن تستخدمو celery (سيرش عنها) بس محتاجة سيرفر وحوارت

## General project notes

المشاريع ديه مش هتخلص بسرعة اطلاقا وممكن تاخد بالشهور بس لو اتحطت فالسي في هتبقا تقيلة جدا خاصة لو بتقدم على شغل فيه اجينتك وكده
ممكن تقابلك بعض الصعوبات فحتة الapis وكده وتلاقي الليمت خلص وانت طبعا كحيان مش هتدفع فلوس 😂
بس صرف نفسك بقا اعمل اكونتات كتير وهكذا يعني
زي ما قلت فالنص في حاجات كتير ملهاش علاقة بالai وسوفتوير اكتر بس ديه طبيعة الشغل حاليا فالسوق
ولازم تكون قوي فيهم ياما ايه اللي يفرقك عن اي حد من برا اتعلم langchain ولا بيستخدم n8n حتى
في حاجات كتير مجرد اقتراحات براحتك لو عايز تبدع وتجرب وتعمل حاجات مختلفة
وكل يوم اصلا فيه حاجات جديدة بتطلع بالذات فحتة الاجينتك

## ⚠️ Notes

- Keep the use case specific; do not build a general researcher.
- Cache aggressively to survive free-tier limits.
- Keep Arabic notes in Arabic when extending this brief.

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
