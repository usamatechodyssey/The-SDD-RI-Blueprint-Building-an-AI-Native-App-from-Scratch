import pytest
from datetime import datetime
import os

# FIXED IMPORTS: 'src' ki jagah 'backend.src' use karein
from backend.src.services.content_parser import parse_content, parse_markdown_content, parse_pdf_content
from backend.src.services.docusaurus_converter import convert_to_docusaurus_format
from backend.src.models.models import SourceContent
from backend.src.utils.logging import BackendException

# Create dummy files for testing
@pytest.fixture
def dummy_markdown_file(tmp_path):
    file_path = tmp_path / "test_doc.md"
    file_path.write_text("# Hello World\n\nThis is a test markdown file.", encoding="utf-8")
    return file_path

@pytest.fixture
def dummy_pdf_file(tmp_path):
    file_path = tmp_path / "test_report.pdf"
    file_path.touch()
    return file_path

@pytest.fixture
def dummy_text_file(tmp_path):
    file_path = tmp_path / "plain_text.txt"
    file_path.write_text("Just some plain text.", encoding="utf-8")
    return file_path

# Unit tests for content_parser.py
def test_parse_markdown_content(dummy_markdown_file):
    content = parse_markdown_content(str(dummy_markdown_file))
    assert "# Hello World" in content
    assert "This is a test markdown file." in content

def test_parse_pdf_content(dummy_pdf_file):
    content = parse_pdf_content(str(dummy_pdf_file))
    assert "[Content from PDF file: test_report.pdf]" in content

def test_parse_text_content(dummy_text_file):
    content = parse_content(str(dummy_text_file))
    assert content.raw_content == "Just some plain text."
    assert content.content_type == "text"

def test_parse_content_markdown(dummy_markdown_file):
    source_content = parse_content(str(dummy_markdown_file))
    assert source_content.id == "test_doc.md"
    assert source_content.content_type == "markdown"
    assert "# Hello World" in source_content.raw_content
    assert source_content.processed_content == source_content.raw_content
    assert isinstance(source_content.last_modified, datetime)

def test_parse_content_pdf(dummy_pdf_file):
    source_content = parse_content(str(dummy_pdf_file))
    assert source_content.id == "test_report.pdf"
    assert source_content.content_type == "pdf"
    assert "[Content from PDF file: test_report.pdf]" in source_content.raw_content
    assert source_content.processed_content == source_content.raw_content

def test_parse_content_nonexistent_file():
    with pytest.raises(BackendException, match="Failed to read"): # Match string adjusted for generic check
        parse_content("non_existent.md")

# Unit tests for docusaurus_converter.py
def test_convert_markdown_to_docusaurus_format(dummy_markdown_file):
    source_content = parse_content(str(dummy_markdown_file))
    converted_content = convert_to_docusaurus_format(source_content)
    assert converted_content.processed_content == source_content.raw_content
    assert converted_content.content_type == "markdown"

def test_convert_pdf_to_docusaurus_format(dummy_pdf_file):
    source_content = parse_content(str(dummy_pdf_file))
    converted_content = convert_to_docusaurus_format(source_content)
    assert converted_content.processed_content == f"# {source_content.id}\n\n{source_content.raw_content}"
    assert converted_content.content_type == "pdf"