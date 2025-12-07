<!-- my-reserch-paper/specs/001-book-creation/quickstart.md -->
# Quickstart Guide: AI-Generated Docusaurus Book

This guide will help you quickly generate and deploy your Docusaurus book from source content.

## 1. Prepare Your Source Content

Place all your source content (Markdown files, PDFs, etc.) into a designated input directory. Ensure your content is well-structured for optimal Docusaurus integration.

```text
my-input-content/
├── chapter1.md
├── chapter2.pdf
└── images/
    └── image1.png
```

## 2. Generate the Docusaurus Book

Use the `generate-book` command (or script) to create the Docusaurus project structure from your source content. Specify your input directory and the desired output directory for the Docusaurus project.

```bash
# Example CLI command (exact command to be defined during implementation)
claude-code generate-book --input my-input-content --output my-docusaurus-book
```

This will create a `my-docusaurus-book` directory with a full Docusaurus project.

## 3. Build the Docusaurus Book

Navigate into your generated Docusaurus project directory and build the static site.

```bash
cd my-docusaurus-book
npm install # Install Docusaurus dependencies
npm run build # Build the static site
```

This will create a `build/` directory containing the static files for your book.

## 4. Deploy to GitHub Pages

Ensure your generated Docusaurus project is a Git repository and you have configured GitHub Pages. Then, use the Docusaurus deploy command.

```bash
cd my-docusaurus-book
# (Ensure your git remote is set up and pushed to GitHub)
npm run deploy # Deploy to GitHub Pages
```

After successful deployment, your book will be accessible at your GitHub Pages URL (e.g., `https://<username>.github.io/<repository-name>/`).
