#backend/src/services/docusaurus_converter.py

from backend.src.models.models import SourceContent
from backend.src.utils.logging import logger


def convert_to_docusaurus_format(source_content: SourceContent) -> SourceContent:
    """Converts source content into a Docusaurus-compatible format (primarily Markdown).

    This function takes a SourceContent object and processes its raw content
    into a format suitable for Docusaurus. Currently, it acts as a passthrough
    for markdown and text content. For PDF content, it formats a basic markdown
    output based on the extracted text.

    Args:
        source_content (SourceContent): An object containing the raw content,
                                        its type, and other metadata.

    Returns:
        SourceContent: The updated SourceContent object with the processed content
                       stored in the `processed_content` attribute.

    Raises:
        (No explicit exceptions raised, but logs a warning for unsupported content types.)
    """
    # For now, this is a simple passthrough. More complex logic would be needed
    # if source_content.content_type was something other than markdown/text
    # For example, converting HTML to Markdown, or enhancing plain text.

    if source_content.content_type == "markdown" or source_content.content_type == "text":
        # Markdown and plain text are already largely Docusaurus-compatible
        # We might add frontmatter here later if needed.
        processed_content = source_content.raw_content
    elif source_content.content_type == "pdf":
        # For PDF, the parsing already returned a dummy string. This conversion
        # would ideally format it better if full PDF parsing was done.
        processed_content = f"# {source_content.id}\n\n{source_content.raw_content}"
    else:
        logger.warning(
            f"Unsupported content type for Docusaurus conversion: {source_content.content_type}"
        )
        processed_content = source_content.raw_content

    source_content.processed_content = processed_content
    return source_content
