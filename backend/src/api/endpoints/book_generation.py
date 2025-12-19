# backend/src/api/endpoints/book_generation.py
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import List, Optional
import os
import shutil
import zipfile
import tempfile
from datetime import datetime

from backend.src.models.models import DocusaurusProject, SourceContent
from backend.src.utils.logging import handle_error, logger, BackendException
from backend.src.services.content_parser import parse_content
from backend.src.services.docusaurus_converter import convert_to_docusaurus_format
from backend.src.services.docusaurus_generator import generate_docusaurus_project

router = APIRouter()

# --- SMART PATH DISCOVERY ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", ".."))
DEFAULT_DOCUSAURUS_PATH = os.path.join(PROJECT_ROOT, "frontend", "docusaurus")

@router.post("/upload-and-generate", response_model=DocusaurusProject)
async def upload_and_generate(
    book_content_zip: UploadFile = File(..., description="ZIP containing .md, images, and pdfs"),
    output_directory: Optional[str] = Form(None, description="Path to Docusaurus project"),
    overwrite: bool = Form(True, description="If false, fails if files already exist.")
):
    temp_dir = None
    target_path = output_directory
    if not target_path or target_path == "string" or target_path == "":
        target_path = DEFAULT_DOCUSAURUS_PATH
    
    target_path = os.path.abspath(target_path)
    docs_output_path = os.path.join(target_path, "docs")
    
    conflicts = []
    valid_assets = [] 

    try:
        logger.info(f"🚀 Advanced Multi-Asset Generation Started. Target: {target_path}")

        # 1. ZIP Extraction to Temp
        temp_dir = tempfile.mkdtemp()
        zip_path = os.path.join(temp_dir, "upload.zip")
        
        with open(zip_path, "wb") as buffer:
            shutil.copyfileobj(book_content_zip.file, buffer)

        # ZIP Validation
        if not zipfile.is_zipfile(zip_path):
            raise BackendException("The uploaded file is not a valid ZIP archive.", status_code=400)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # 2. Advanced Scan & Filter (MD + Images + PDF)
        allowed_extensions = {'.md', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf'}
        
        for root, _, files in os.walk(temp_dir):
            for file_name in files:
                # FIX: os.path.splitext returns a tuple, we need the index [1] for extension
                ext = os.path.splitext(file_name)[1].lower()
                source_file = os.path.join(root, file_name)
                rel_path = os.path.relpath(source_file, temp_dir)
                dest_file = os.path.join(docs_output_path, rel_path)

                if ext in allowed_extensions:
                    if os.path.exists(dest_file):
                        conflicts.append(rel_path)
                    valid_assets.append((source_file, rel_path, ext))
                else:
                    logger.warning(f"🚫 File blocked: {rel_path}. Format {ext} not allowed.")

        # 3. Conflict Handling
        if conflicts and not overwrite:
            error_msg = f"CONFLICT: Assets {conflicts} already exist. Set overwrite=true to sync."
            logger.error(error_msg)
            raise BackendException(error_msg, status_code=409)

        # 4. Processing Assets
        parsed_contents = []
        for src, rel_id, ext in valid_assets:
            if ext == '.md':
                content = parse_content(src)
                content.id = rel_id 
                converted = convert_to_docusaurus_format(content)
                parsed_contents.append(converted)
            else:
                binary_asset = SourceContent(
                    id=rel_id,
                    file_path=src, 
                    content_type="binary", 
                    raw_content="", 
                    processed_content="",
                    last_modified=datetime.now()
                )
                parsed_contents.append(binary_asset)

        # 5. Smart Merge Generation
        project = generate_docusaurus_project(parsed_contents, target_path)

        logger.info(f"✅ Successfully Synced {len(parsed_contents)} assets (MD, Images, PDFs).")
        return project

    except BackendException as be:
        raise HTTPException(status_code=be.status_code, detail=be.message)
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)