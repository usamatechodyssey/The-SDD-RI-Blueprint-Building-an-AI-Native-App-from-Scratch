# Chapter 3: Building the Brain (Backend)

We chose **FastAPI** because it is fast, modern, and works great with AI.

## The Directory Structure
We set up a clean structure:
-   `src/api`: Where the endpoints live.
-   `src/services`: Where the actual logic (Skills) lives.
-   `src/models`: Where Pydantic data validation happens.

## Key Skills Implemented
1.  **Content Parser:** Reads Markdown/PDFs.
2.  **Docusaurus Generator:** Creates the folder structure dynamically.
3.  **Deployment Service:** Handles Git operations automatically.

## Testing
We didn't just hope it works. We wrote **Pytest** units (`tests/unit/`) to verify every single function before connecting it to the API.