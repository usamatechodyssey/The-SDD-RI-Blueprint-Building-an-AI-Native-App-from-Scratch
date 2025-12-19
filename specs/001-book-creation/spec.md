# Feature Specification: AI-Native Book CMS & Generator

**Feature Branch**: `001-book-creation`
**Last Updated**: 2025-12-18 (Phase X: Admin CMS Integration)
**Status**: Active / Refined
**Input**: AI-Native Book CMS with Tree Structure & Incremental Updates

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Smart Hierarchical Book Generation (Priority: P1)
As a user, I want to upload a **ZIP archive** containing my research folders and files so that the system generates a Docusaurus book that preserves my exact **folder tree structure**.

**Why this priority**: Essential for complex research where hierarchy (Chapters/Sub-chapters) matters.
**Independent Test**: Upload a ZIP with nested folders; verify that the Docusaurus sidebar reflects the same hierarchy and files are not flattened.

### User Story 2 - Admin Content Management (Priority: P2)
As an admin, I want to **list all existing book content** and **delete specific files/folders** via the API so that I can manage the book's lifecycle without manually touching the server files.

**Why this priority**: Necessary for long-term maintenance and production-grade content control.
**Independent Test**: Use `/admin/list-content` to see files, then `/admin/delete-content` to remove a file, and verify it is gone from the `docs` folder.

### User Story 3 - Incremental Merging & Overwrite Protection (Priority: P1)
As a user, I want to add new chapters to my existing book without losing old content, and I want to be warned if I am about to overwrite an existing file.

**Why this priority**: Prevents accidental data loss and allows the book to grow over time.
**Acceptance Scenarios**:
1. **Given** overwrite=false, **When** uploading a ZIP with an existing file name, **Then** return a `409 Conflict` error.
2. **Given** overwrite=true, **When** uploading, **Then** update only the matching files and keep others intact.

---

### Edge Cases
- **Non-Markdown Files**: The system MUST block or ignore non-`.md` files (e.g., `.exe`, `.bin`) inside ZIPs to ensure site stability.
- **Path Traversal Attacks**: The Admin API MUST validate paths to ensure users cannot delete system files outside the `docs` directory.
- **Auto-Path Discovery**: If `output_directory` is missing, the system MUST automatically fallback to the default internal project path.
- **Empty ZIPs**: Return a clear error if the uploaded ZIP contains no valid Markdown content.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST support **ZIP archive uploads** for bulk content ingestion.
- **FR-002**: The system MUST **preserve recursive directory structures** from the ZIP into the Docusaurus `docs` folder.
- **FR-003**: The system MUST perform **Incremental Updates** (merging new content with existing files instead of wiping the directory).
- **FR-004**: The system MUST provide an **Admin Inventory API** (`/list-content`) to return a JSON tree of all docs.
- **FR-005**: The system MUST provide a **Deletion API** (`/delete-content`) for granular file and folder removal.
- **FR-006**: The system MUST enforce **File Format Filtering** (strictly allowing only `.md` for book content).
- **FR-007**: The system MUST provide a **Manual Rebuild Trigger** (`/rebuild-book`) to refresh navigation/sidebars after manual deletions.

### Key Entities
- **ZIPSource**: A compressed archive containing the hierarchical research data.
- **ContentTree**: A JSON representation of the current book inventory.
- **DocusaurusProject**: The managed instance of the book.

## Success Criteria *(mandatory)*

### Measurable Outcomes
- **SC-001**: **100% Tree Fidelity**: The Docusaurus sidebar must exactly match the ZIP folder structure.
- **SC-002**: **Zero Data Loss**: Uploading new content MUST NOT delete existing content unless explicitly overwritten.
- **SC-003**: **Security Compliance**: 0% success rate for attempting to delete files outside the `docs` path or uploading restricted file formats.
- **SC-004**: **Sub-second Inventory**: The `/list-content` API must return the full book structure in less than 500ms for projects up to 500 files.