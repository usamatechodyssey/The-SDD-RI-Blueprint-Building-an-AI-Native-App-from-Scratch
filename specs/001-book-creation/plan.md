<!-- my-reserch-paper/specs/001-book-creation/plan.md -->
# Implementation Plan: AI-Generated Docusaurus Book

**Branch**: `001-book-creation` | **Date**: 2025-12-05 | **Spec**: specs/001-book-creation/spec.md
**Input**: Feature specification from `/specs/001-book-creation/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

The primary requirement is to automatically generate a complete Docusaurus book project from provided source content and deploy it to GitHub Pages. The technical approach involves a Python backend (FastAPI/LangChain/ChatKit) for RAG and LLM orchestration, Docusaurus (React/TypeScript) for frontend generation and serving, and Qdrant Cloud Free Tier for vector embeddings, utilizing Gemini Flash via Claude Router.

## Technical Context

**Language/Version**: Python 3.12+, Node.js (for Docusaurus utilities)
**Primary Dependencies**: FastAPI, LangChain/ChatKit, Docusaurus, Qdrant client libraries
**Storage**: Qdrant Cloud Free Tier (vector embeddings), local JSON/SQLite (project configuration and metadata)
**Testing**: Pytest (Python backend), Jest/React Testing Library (Docusaurus components/utilities), Playwright/Cypress (end-to-end for book navigation and chatbot interaction)
**Target Platform**: Linux server (for Python backend/API), GitHub Pages (for Docusaurus book deployment)
**Project Type**: Web application (Python Backend + Docusaurus Frontend)
**Performance Goals**:
- **SC-001**: Complete Docusaurus book generation from typical research paper collection (e.g., 100 Markdown files, each ~2MB) within 5 minutes.
- **SC-002**: Deployable to GitHub Pages with a single command, becoming publicly accessible within 3 minutes of successful deployment.
- **SC-003**: 95% of valid source content types (Markdown, basic PDF text) correctly processed and integrated.
- **SC-004**: Generated book structure intuitive and easy to navigate (target > 80% satisfaction).
**Constraints**:
- Mandatory API rate limiting on all public API endpoints (especially RAG chat).
- Strict Pydantic validation for all FastAPI inputs.
- Use environment variables (`.env`) for all API keys (OpenAI, Qdrant); secrets MUST NEVER be committed to GitHub or exposed on Docusaurus frontend.
- All LLM calls must minimize token usage (e.g., maximizing context compression, using `gemini-flash`).
- No incremental support for book generation; always full regeneration and redeployment.
**Scale/Scope**:
- Typical research paper collection (e.g., 100 Markdown files, each ~2MB) for book generation.
- Publicly accessible RAG chatbot.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **1. Architecture Stack (Backend, Frontend, Data)**: Compliant (Python/FastAPI/LangChain, Docusaurus/React/TypeScript, Qdrant/JSON/SQLite, Gemini Flash).
- **2. Quality & Testing Standards**: Partially Compliant (Unit, Integration, Code Quality, Documentation, Commit History - ongoing linting and documentation efforts).
- **3. Security & Rate Limiting (Cost Management)**: Compliant (Rate Limiting, Input Validation, Secrets Management, Cost/Token Management).
- **4. Reusable Intelligence (RI) Mandates**: Compliant (RI First, Traceability (ADR), Skill Documentation (P+Q+P)).

## Project Structure

### Documentation (this feature)

```text
specs/001-book-creation/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── api/             # FastAPI endpoints for RAG and book generation
│   ├── services/        # Business logic for content processing, RAG, LLM orchestration
│   └── models/          # Pydantic models for request/response, data structures
└── tests/
    ├── unit/
    └── integration/

frontend/
├── docusaurus/          # Docusaurus project root
│   ├── src/             # Custom Docusaurus components, pages, styling
│   └── docs/            # Generated documentation pages
└── chatbot-ui/          # Custom React components for the RAG chatbot interface

scripts/                 # Helper scripts for build, deploy, content processing
```

**Structure Decision**: A monorepo-like structure with `backend/` for the Python API, `frontend/` for the Docusaurus project and chatbot UI, and `scripts/` for utilities. This aligns with the web application project type and separation of concerns.

## Complexity Tracking

(No constitution check violations to justify.)
