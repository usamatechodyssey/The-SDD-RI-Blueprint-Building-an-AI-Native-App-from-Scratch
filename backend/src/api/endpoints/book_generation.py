from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field  # Import Field
from typing import List
from datetime import datetime
import os

from backend.src.models.models import DocusaurusProject
from backend.src.utils.logging import handle_error, logger, BackendException
from backend.src.services.content_parser import parse_content
from backend.src.services.docusaurus_converter import convert_to_docusaurus_format
from backend.src.services.docusaurus_generator import generate_docusaurus_project

router = APIRouter()

class GenerateBookRequest(BaseModel):
    # Fix: min_length=1 add kiya taake empty list par 422 error aaye
    source_content_paths: List[str] = Field(..., min_length=1, description="List of file paths to process. Must not be empty.")
    output_directory: str

@router.post("/generate-book", response_model=DocusaurusProject)
async def generate_book(
    request: GenerateBookRequest,
):
    try:
        logger.info(f"Received request to generate book. Sources: {len(request.source_content_paths)}")

        # 1. Parse Source Content
        parsed_contents = []
        for path in request.source_content_paths:
            if not os.path.exists(path):
                # Specific check for missing files
                raise BackendException(f"Source file not found: {path}", status_code=400)
            
            content = parse_content(path)
            
            # 2. Convert to Docusaurus Format
            converted = convert_to_docusaurus_format(content)
            parsed_contents.append(converted)

        # 3. Generate Project Structure
        project = generate_docusaurus_project(parsed_contents, request.output_directory)

        logger.info(f"Successfully generated Docusaurus project: {project.id}")
        return project

    except BackendException as e:
        logger.error(f"Backend error during book generation: {e.message}")
        raise HTTPException(status_code=e.status_code, detail=e.message)
    except Exception as e:
        handle_error(e)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")