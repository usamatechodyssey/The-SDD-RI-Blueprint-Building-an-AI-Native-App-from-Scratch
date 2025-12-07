<!-- my-reserch-paper/specs/001-book-creation/research.md -->
## Research Findings: AI-Generated Docusaurus Book

### 1. Architecture Stack Decisions

- **Decision**: Backend: Python 3.12+ (FastAPI, LangChain/ChatKit). Frontend: Docusaurus (React/TypeScript). Data: Qdrant Cloud Free Tier (vector embeddings), local JSON/SQLite (metadata). LLM: Gemini Flash via Claude Router.
- **Rationale**: This stack was chosen to align with the project's core intent of building an AI-Generated Docusaurus Book and an Integrated RAG Chatbot, as mandated by the project constitution. Python provides robust AI/ML capabilities, Docusaurus offers a flexible and scalable documentation framework, Qdrant provides efficient vector search, and Gemini Flash ensures cost-effective LLM interactions.
- **Alternatives considered**: No alternatives were considered for the core stack components as they were mandated by the project constitution.

### 2. Incremental Updates Policy

- **Decision**: No incremental support for Docusaurus book generation and deployment. The system will always fully regenerate and redeploy the entire Docusaurus book upon any update to the source content.
- **Rationale**: This decision was made to minimize implementation complexity for the MVP Hackathon scope, allowing the team to focus efforts on the core RAG integration, which is the primary goal.
- **Alternatives considered**: Full incremental support (detect and update only changed content and configuration), Content-only incremental support (only detect changes in source content files, rebuilding full Docusaurus configuration).
