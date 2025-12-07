# ADR-0001: Initial Architecture Stack

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-05
- **Feature:** 001-book-creation
- **Context:** The project aims to build an AI-Generated Docusaurus Book and an Integrated RAG Chatbot, following SDD-RI principles. This ADR documents the initial architectural stack decisions that define the core technologies for the backend, frontend, data storage, and LLM provider, as outlined in the project constitution.

## Decision

- **Backend**: Python 3.12+ (FastAPI for API endpoints, LangChain/ChatKit for RAG logic and LLM orchestration).
- **Frontend**: Docusaurus (for documentation generation, React/TypeScript-based) for the book deployment via GitHub Pages, with custom React components for the chatbot UI.
- **Data**: Qdrant Cloud Free Tier for vector embeddings. Project configuration and metadata using local JSON/SQLite.
- **LLM Provider**: Gemini Flash via the Claude Router setup for cost efficiency.

## Consequences

### Positive

- **Leverages strong Python ecosystem**: Access to mature AI/ML libraries (LangChain, FastAPI).
- **Efficient documentation generation**: Docusaurus provides a robust and well-supported framework for generating static documentation sites.
- **Scalable vector search**: Qdrant Cloud offers a managed solution for high-performance vector similarity search.
- **Cost-effective LLM interactions**: Utilizing Gemini Flash for thinking processes helps manage token usage and operational costs.
- **Clear separation of concerns**: Backend for logic, frontend for presentation, dedicated tools for data and LLM interaction.

### Negative

- **Learning curve for multiple technologies**: Requires expertise in Python, FastAPI, LangChain, Docusaurus, React, TypeScript, and Qdrant.
- **Integration complexity**: Orchestrating various components (FastAPI, LangChain, Docusaurus, Qdrant, Gemini Flash) requires careful design and implementation.
- **Dependency on cloud services**: Qdrant Cloud Free Tier and Claude Router introduce external dependencies.
- **Potential for tool fragmentation**: Managing multiple frameworks and libraries could lead to a fragmented development experience if not carefully managed.

## Alternatives Considered

- **Alternative Backend Frameworks**: Considered Flask or Django for Python backend, but FastAPI was chosen for its modern features, performance, and strong typing with Pydantic, which aligns with strict input validation requirements.
- **Alternative Frontend Frameworks**: Considered Next.js or other React frameworks, but Docusaurus was specifically chosen due to the requirement for an AI-Generated Docusaurus Book, making it the most direct and efficient solution for documentation generation and deployment.
- **Alternative Vector Databases**: Considered FAISS or ChromaDB for local vector storage, but Qdrant Cloud Free Tier was chosen for its managed service, scalability, and ease of deployment, specifically mandated by the project constitution.
- **Alternative LLM Providers**: While other LLMs exist, Gemini Flash via Claude Router was a constitutional mandate for cost efficiency.

## References

- Feature Spec: specs/001-book-creation/spec.md
- Implementation Plan: specs/001-book-creation/plan.md
- Related ADRs: null
- Evaluator Evidence: null
