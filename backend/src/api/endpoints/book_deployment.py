# backend/src/api/endpoints/book_deployment.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os

from backend.src.models.models import GeneratedBook
from backend.src.services.docusaurus_builder import build_docusaurus_project 
# REAL IMPORT
from backend.src.services.github_deployer import deploy_to_github_pages
from backend.src.utils.logging import logger, handle_error, BackendException

router = APIRouter()


class DeployBookRequest(BaseModel):
    project_path: str
    github_repo_url: str
    branch: str = "gh-pages"


@router.post("/deploy-book", response_model=GeneratedBook)
async def deploy_book(
    request: DeployBookRequest,
):
    try:
        logger.info(f"Received deployment request for: {request.project_path}")

        # 1. Build Docusaurus project
        build_output_path = build_docusaurus_project(request.project_path) 

        # 2. Deploy to GitHub Pages (REAL LOGIC ENABLED)
        deployment_url = deploy_to_github_pages(
            request.project_path, 
            request.github_repo_url, 
            request.branch
        )

        generated_book = GeneratedBook(
            id=os.path.basename(request.project_path),
            output_path=build_output_path,
            deployment_url=deployment_url,
            build_timestamp=datetime.now(),
            deployment_timestamp=datetime.now(),
        )

        logger.info(f"Book deployed successfully: {generated_book.deployment_url}")
        return generated_book

    except BackendException as e:
        logger.error(f"Backend error during book deployment: {e.message}")
        raise HTTPException(status_code=e.status_code, detail=e.message)
    except Exception as e:
        handle_error(e)
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )