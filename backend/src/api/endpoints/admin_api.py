from fastapi import APIRouter, HTTPException, Query, Form
from typing import List, Optional
import os
from backend.src.services.content_manager import list_docs_tree, delete_path
from backend.src.services.content_parser import parse_content
from backend.src.services.docusaurus_generator import generate_docusaurus_project
from backend.src.utils.logging import logger
    # backend/src/api/endpoints/admin_api.py
from pydantic import BaseModel # <--- Yeh zaroori hai

router = APIRouter(prefix="/admin", tags=["Admin Content Manager"])

# Path detection logic
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", ".."))
DEFAULT_DOCS_PATH = os.path.join(PROJECT_ROOT, "frontend", "docusaurus", "docs")
DEFAULT_PROJECT_PATH = os.path.join(PROJECT_ROOT, "frontend", "docusaurus")

@router.get("/list-content")
async def get_book_content():
    """Book mein maujood sari files ki list dikhata hai."""
    files = list_docs_tree(DEFAULT_DOCS_PATH)
    return {"total_files": len(files), "files": files}

@router.delete("/delete-content")
async def remove_content(path: str = Query(..., description="Relative path of file or folder to delete")):
    """Koi bhi file ya folder delete karein."""
    delete_path(DEFAULT_DOCS_PATH, path)
    return {"message": f"Successfully deleted: {path}. Please run /rebuild-book to update sidebar."}

@router.post("/rebuild-book")
async def rebuild_book():
    """Delete karne ke baad sidebar aur project ko refresh karne ke liye."""
    try:
        # 1. Scan current docs folder
        all_files = list_docs_tree(DEFAULT_DOCS_PATH)
        parsed_contents = []
        
        for rel_path in all_files:
            full_path = os.path.join(DEFAULT_DOCS_PATH, rel_path)
            content = parse_content(full_path)
            content.id = rel_path # Path barkarar rakhein
            parsed_contents.append(content)
        
        # 2. Re-generate project (Refresh sidebar and structure)
        generate_docusaurus_project(parsed_contents, DEFAULT_PROJECT_PATH)
        
        return {"message": "Book structure and sidebar refreshed successfully!"}
    except Exception as e:
        logger.error(f"Rebuild failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    


# 1. Aik Model banayein jo bataye ke data kaisa dikhega
class ChatbotConfigResponse(BaseModel):
    apiUrl: str
    apiKey: str
    botName: str
    botTagline: str

# 2. Endpoint mein 'response_model' add karein
@router.get("/chatbot-config", response_model=ChatbotConfigResponse)
async def get_chatbot_config():
    """
    Frontend ko dynamic chatbot details dene ke liye.
    """
    return {
        "apiUrl": os.getenv("CHATBOT_API_URL", "https://your-chatbot.up.railway.app"),
        "apiKey": os.getenv("CHATBOT_API_KEY", "omni_default_key"),
        "botName": os.getenv("BOT_NAME", "Architect AI"),
        "botTagline": os.getenv("BOT_TAGLINE", "Secure Agent")
    }