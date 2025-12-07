#backend/src/services/content_parser.py
from backend.src.models.models import SourceContent
from backend.src.utils.logging import logger, BackendException
from datetime import datetime
import os


def parse_markdown_content(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        logger.error(f"Error reading markdown file {file_path}: {e}")
        raise BackendException(f"Failed to read markdown file: {file_path}", status_code=400)


def parse_pdf_content(file_path: str) -> str:
    # Placeholder for PDF parsing. Actual implementation would require libraries like PyPDF2 or pdfminer.six
    logger.warning(f"PDF parsing for {file_path} is a placeholder. Returning dummy content.")
    return f"[Content from PDF file: {os.path.basename(file_path)}]"


def parse_content(file_path: str) -> SourceContent:
    """Parses content from a given file path based on its extension."""
    file_extension = os.path.splitext(file_path)[1].lower()
    content_type = "unknown"
    raw_content = ""

    if file_extension == ".md":
        content_type = "markdown"
        raw_content = parse_markdown_content(file_path)
    elif file_extension == ".pdf":
        content_type = "pdf"
        raw_content = parse_pdf_content(file_path)
    else:
        logger.warning(f"Unsupported file type for parsing: {file_path}. Treating as plain text.")
        content_type = "text"
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                raw_content = f.read()
        except Exception as e:
            logger.error(f"Error reading plain text file {file_path}: {e}")
            raise BackendException(f"Failed to read file: {file_path}", status_code=400)

    # For parsing, processed content is initially the same as raw content.
    # Conversion service will handle further processing.
    return SourceContent(
        id=os.path.basename(file_path),
        file_path=file_path,
        content_type=content_type,
        raw_content=raw_content,
        processed_content=raw_content,  # Initial processed content
        last_modified=datetime.fromtimestamp(os.path.getmtime(file_path)),
    )
