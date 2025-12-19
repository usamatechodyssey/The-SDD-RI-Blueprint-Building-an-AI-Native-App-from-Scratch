# Implementation Plan: AI-Native Book CMS & Generator

**Branch**: `001-book-creation` | **Last Updated**: 2025-12-18 | **Spec**: specs/001-book-creation/spec.md
**Input**: Advanced Content Management System with Tree Structure support.

## Summary

The primary requirement has evolved from a simple generator to a full-scale **AI-Native Book CMS**. The system now supports bulk ingestion via ZIP files, preserves complex folder hierarchies (Tree Structure), and allows incremental content merging. The technical approach utilizes a FastAPI backend for hierarchical file orchestration and an Admin API for granular content control (List/Delete).

## Technical Context

**Language/Version**: Python 3.12+, Node.js 18+
**Primary Dependencies**: 
- **Backend**: `FastAPI`, `Uvicorn`, `python-multipart` (for ZIP uploads), `zipfile`, `shutil`, `tempfile`.
- **Frontend**: `Docusaurus` (React/TypeScript).
**Storage**: Recursive Local File System (The `docs` directory acts as the primary hierarchical data store).
**Testing**: 
- **Backend**: `Pytest` (Unit tests for parser, builder, and admin services).
- **E2E**: `Playwright` (for book navigation and sidebar validation).
**Target Platform**: Linux/Windows Server (Backend), GitHub Pages (Deployment).
**Project Type**: AI-Native CMS (Content Management System).

**Performance Goals**:
- **SC-001**: Bulk ingestion and tree generation of 100+ files within 60 seconds.
- **SC-002**: Incremental sync (adding 1-5 files to an existing book) in under 5 seconds.
- **SC-003**: 100% fidelity in preserving nested folder structures from ZIP to Docusaurus sidebar.

**Constraints**:
- **Incremental Support**: MUST support recursive merging (adding/updating files without wiping the existing library).
- **Security**: Mandatory path validation in Admin API to prevent directory traversal.
- **Strict Format**: Only `.md` files are allowed in the automated pipeline.
- **Auto-Discovery**: System must automatically resolve internal paths if no `output_directory` is provided.

## Constitution Check

- **1. Architecture Stack**: Compliant (Added `python-multipart` for professional ingestion).
- **2. Quality & Testing**: Compliant (Added Admin API integration tests).
- **3. Security & Rate Limiting**: Compliant (Added path-level security for Deletion API).
- **4. Reusable Intelligence (RI)**: Compliant (Implemented `ContentManager` and `SidebarGenerator` as reusable skills).

## Project Structure

### Documentation & Source
```text
specs/001-book-creation/
├── plan.md              # This file (Updated for CMS Phase)
├── contracts/           # OpenAPI v3 spec for CMS Endpoints
└── tasks.md             # Task list (T001 - T035)

backend/
├── src/
│   ├── api/             
│   │   ├── endpoints/
│   │   │   ├── book_generation.py  # ZIP & Tree Logic
│   │   │   ├── admin_api.py        # List/Delete/Rebuild Logic
│   │   │   └── book_deployment.py  # GitHub Pages Logic
│   │   └── middleware/
│   │       └── rate_limiter.py
│   ├── services/        
│   │   ├── content_manager.py      # CMS Skill (Tree/Delete)
│   │   ├── docusaurus_generator.py # Smart Merge Logic
│   │   └── github_deployer.py      # Deployment Skill
│   └── models/          
│       └── models.py               # Pydantic Schemas