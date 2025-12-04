# Hackathon 1 Project Constitution (SDD-RI)

## Intent
This project aims to build an AI-Generated Docusaurus Book and an Integrated RAG Chatbot. The core objective is to follow SDD-RI principles rigorously to maximize traceability, demonstrate reusable intelligence (Skills/Subagents), and secure all available bonus points.

## Required Sections

### 1. Architecture Stack (Backend, Frontend, Data)
- **Backend:** Python 3.12+ (Specifically **FastAPI** for API endpoints, **LangChain/ChatKit** for RAG logic and LLM orchestration).
- **Frontend:** **Docusaurus** (for documentation generation, React/TypeScript-based) for the book deployment via GitHub Pages.
- **Data:** Vector Database Must use **Qdrant Cloud Free Tier** for vector embeddings. Project configuration and metadata can use local JSON/SQLite.
- **LLM Provider:** Must use **Gemini Flash** via the Claude Router setup (as verified) for cost efficiency.

### 2. Quality & Testing Standards
- **Unit Tests:** Mandatory for all core logic, APIs, and utility functions (Pytest for Python).
- **Integration Tests:** Essential for verifying RAG pipeline functionality (from Qdrant retrieval to final LLM response).
- **Code Quality:** Enforced via linters (Black/Flake8 for Python, ESLint/Prettier for Docusaurus).
- **Documentation:** All public APIs, complex functions, and architectural decisions must be documented.
- **Commit History:** Commit messages must be clear, referencing the corresponding Task ID (TXXX) when applicable.

### 3. Security & Rate Limiting (Cost Management)
- **Rate Limiting:** Mandatory API rate limiting on all public API endpoints (especially RAG chat) to prevent DoS and manage free tier usage.
- **Input Validation:** Strict Pydantic validation for all FastAPI inputs to prevent injection attacks and ensure data integrity.
- **Secrets Management:** Use environment variables (`.env`) for all API keys (OpenAI, Qdrant). **Secrets MUST NEVER be committed to GitHub or exposed on Docusaurus frontend.**
- **Cost/Token Management:** All LLM calls must be designed to minimize token usage (e.g., maximizing context compression, using `gemini-flash` for thinking).

### 4. Reusable Intelligence (RI) Mandates
- **RI First:** All complex, repeatable logic (RAG pipeline setup, Docusaurus deployment script, chunking strategy) must be designed as a **Skill or Subagent** to demonstrate reusable intelligence.
- **Traceability:** Every major design decision (e.g., RAG chunk size, FastAPI framework choice) must be documented via an **ADR** (Architectural Decision Record).
- **Skill Documentation:** Every created Skill or Subagent must include **P+Q+P** (Persona + Questions + Principles) documentation.

## Non-Goals (Out of Scope for MVP Hackathon)
- User Authentication for the RAG Chatbot (Chatbot is public).
- Advanced UI features outside Docusaurus standard components.
- Complex database migration strategies (using simple JSON/SQLite metadata).

## Architectural Decision Records (ADR) - Intelligent Suggestion
📋 Architectural decision detected: Initial Architecture Stack. Document reasoning and tradeoffs? Run `/sp.adr Initial-Architecture-Stack`