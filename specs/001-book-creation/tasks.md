# Implementation Tasks: AI-Native Book CMS & Generator

**Feature Branch**: `001-book-creation` | **Last Updated**: 2025-12-18 | **Spec**: specs/001-book-creation/spec.md
**Plan**: specs/001-book-creation/plan.md

## Summary

This document outlines the detailed, actionable tasks required to implement the AI-Native Book CMS. Tasks are organized into phases, prioritizing foundational setup, followed by user stories, and concluding with the advanced Admin Content Management System (CMS).

## Task Generation Details

- **Total task count**: 35
- **Task count per user story**:
  - User Story 1 (Basic Gen): 6 tasks
  - User Story 2 (Deployment): 5 tasks
  - User Story 3 (Admin CMS): 9 tasks (New)
- **Status**: 100% Complete

## Phases

### Phase 1: Setup (Project Initialization)
- [x] T001 Initialize Python backend project structure in `backend/`
- [x] T002 Initialize Docusaurus frontend project structure in `frontend/docusaurus/`
- [x] T003 Configure basic FastAPI application in `backend/src/api/main.py`
- [x] T004 Install Python dependencies (`FastAPI`, `Uvicorn`, `python-multipart`) in `backend/`
- [x] T005 Install Node.js/Docusaurus dependencies in `frontend/docusaurus/`
- [x] T006 Set up `.env` file for environment variables in `backend/`

### Phase 2: Foundational (Blocking Prerequisites)
- [x] T007 Implement core Pydantic models (SourceContent, DocusaurusProject) in `backend/src/models/`
- [x] T010 Set up basic logging and error handling in `backend/src/utils/logging.py`

### Phase 3: User Story 1 - Basic Generation
- [x] T011 Create FastAPI endpoint for book generation in `backend/src/api/endpoints/book_generation.py`
- [x] T012 Implement content parsing service in `backend/src/services/content_parser.py`
- [x] T013 Implement Docusaurus converter in `backend/src/services/docusaurus_converter.py`
- [x] T014 Implement Docusaurus project creation logic in `backend/src/services/docusaurus_generator.py`
- [x] T015 Add unit tests for content services in `backend/tests/unit/`
- [x] T016 Add integration tests for generation endpoint in `backend/tests/integration/`

### Phase 4: User Story 2 - Deployment Logic
- [x] T017 Create book deployment endpoint in `backend/src/api/endpoints/book_deployment.py`
- [x] T018 Implement Docusaurus build service in `backend/src/services/docusaurus_builder.py`
- [x] T019 Implement GitHub Pages deployment logic in `backend/src/services/github_deployer.py`
- [x] T020 Add unit tests for deployment services in `backend/tests/unit/`
- [x] T021 Add integration tests for deployment endpoint in `backend/tests/integration/`

### Phase 5: Advanced Admin CMS (The Pivot) 🎯
**Goal**: Transform the generator into a production-grade CMS with Tree structure and Incremental merging.

- [x] T027 Implement **ZIP Archive Ingestion** logic in `book_generation.py`
- [x] T028 Implement **Recursive Tree Structure** preservation for nested folders.
- [x] T029 Implement **Smart Incremental Merging** (Merge new content without wiping `docs`).
- [x] T030 Implement **Dynamic Sidebar Generator** in `docusaurus_generator.py`.
- [x] T031 Create **Inventory API** (`/admin/list-content`) in `backend/src/api/endpoints/admin_api.py`.
- [x] T032 Create **Deletion API** (`/admin/delete-content`) with path-traversal security checks.
- [x] T033 Create **Global Rebuild Trigger** (`/admin/rebuild-book`) to refresh site hierarchy.
- [x] T034 Implement **Auto-Path Discovery** logic to remove manual path input requirements.
- [x] T035 Create **Content Manager Skill** in `backend/src/services/content_manager.py`.

### Final Phase: Polish & Cross-Cutting Concerns
- [x] T022 Implement mandatory API rate limiting in `backend/src/api/middleware/rate_limiter.py`
- [x] T023 Ensure strict Pydantic validation for all FastAPI inputs.
- [x] T025 Implement E2E tests for book navigation using Playwright in `frontend/tests/e2e/`
- [x] T026 Verify full compliance with project constitution for quality and security.

## Dependencies
1. Basic Setup (Phase 1 & 2)
2. Content Processing (Phase 3)
3. Advanced CMS & Merging (Phase 5)
4. Deployment (Phase 4)