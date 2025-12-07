<!-- my-reserch-paper/specs/001-book-creation/data-model.md -->
## Data Model: AI-Generated Docusaurus Book

### 1. SourceContent

- **Description**: Represents the raw input files provided by the user for book generation. These can be various document types like Markdown or PDFs.
- **Attributes**:
  - `id`: (string) Unique identifier for the content item.
  - `file_path`: (string) Absolute path to the original source file.
  - `content_type`: (string) Type of the content (e.g., 'markdown', 'pdf', 'text').
  - `raw_content`: (string/bytes) The original content of the file.
  - `processed_content`: (string) The content after extraction and conversion to a Docusaurus-compatible format (e.e.g, Markdown).
  - `last_modified`: (timestamp) Timestamp of the last modification of the source file.
- **Relationships**: A `SourceContent` item is processed to contribute to a `DocusaurusProject`.

### 2. DocusaurusProject

- **Description**: Represents the generated Docusaurus site structure and its constituent files before building. This includes configuration, static assets, and content pages derived from `SourceContent`.
- **Attributes**:
  - `id`: (string) Unique identifier for the Docusaurus project instance.
  - `project_path`: (string) Absolute path to the root directory of the generated Docusaurus project.
  - `config_files`: (list of strings) Paths to Docusaurus configuration files (e.g., `docusaurus.config.js`).
  - `content_files`: (list of strings) Paths to the Markdown or MDX files that form the book's content.
  - `creation_timestamp`: (timestamp) When the project structure was first generated.
- **Relationships**: Generated from processed `SourceContent`. Built to produce a `GeneratedBook`.

### 3. GeneratedBook

- **Description**: Represents the compiled, deployable output of the Docusaurus project, ready for hosting.
- **Attributes**:
  - `id`: (string) Unique identifier for the generated book instance.
  - `output_path`: (string) Absolute path to the static build output directory (e.g., `build/`).
  - `deployment_url`: (string, optional) The public URL where the book is deployed (e.g., GitHub Pages URL). Populated after successful deployment.
  - `build_timestamp`: (timestamp) When the book was last successfully built.
  - `deployment_timestamp`: (timestamp, optional) When the book was last successfully deployed.
- **Relationships**: Produced by the build process of a `DocusaurusProject`.
