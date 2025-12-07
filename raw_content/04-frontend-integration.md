# Chapter 4: The Interface (Frontend)

We used **Docusaurus** (by Meta) because it is the best tool for documentation.

## Why Docusaurus?
-   It's React-based (Modern).
-   It supports Markdown out of the box.
-   It is fast and SEO-friendly.

## The Integration
Our Backend API talks to Docusaurus.
1.  User sends files to API.
2.  API writes them into `frontend/docusaurus/docs`.
3.  We run `npm run build` programmatically.

This automation turns a manual process (copy-pasting files) into a 1-click magic button.