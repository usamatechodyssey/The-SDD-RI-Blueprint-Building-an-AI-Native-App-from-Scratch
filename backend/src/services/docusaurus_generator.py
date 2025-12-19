import os
import shutil
import json # <--- Naya import indices generate karne ke liye
from datetime import datetime
from typing import List
from backend.src.models.models import SourceContent, DocusaurusProject
from backend.src.utils.logging import logger, BackendException

# Path Discovery
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", "..", ".."))
DEFAULT_TEMPLATE_PATH = os.path.join(PROJECT_ROOT, "frontend", "docusaurus")
DOCUSAURUS_TEMPLATE_PATH = os.getenv("DOCUSAURUS_TEMPLATE_PATH", DEFAULT_TEMPLATE_PATH)

def initialize_docusaurus_project(output_directory: str):
    """Initializes or checks for existing Docusaurus project."""
    abs_output = os.path.abspath(output_directory)
    config_exists = os.path.exists(os.path.join(abs_output, "docusaurus.config.js"))

    if os.path.exists(abs_output) and config_exists:
        logger.info(f"Merge Mode: Project exists at {output_directory}")
        os.makedirs(os.path.join(abs_output, "docs"), exist_ok=True)
        return 

    if not os.path.exists(DOCUSAURUS_TEMPLATE_PATH):
        raise BackendException(f"Template not found at: {DOCUSAURUS_TEMPLATE_PATH}", status_code=500)

    logger.info(f"Fresh Setup: Copying template to {output_directory}")
    shutil.copytree(
        DOCUSAURUS_TEMPLATE_PATH, 
        output_directory, 
        dirs_exist_ok=True, 
        ignore=shutil.ignore_patterns('node_modules', '.docusaurus', '.git')
    )

# --- NEW: AUTO-INDEX GENERATOR SKILL 🤖 ---
def generate_category_indices(docs_path: str):
    """
    Har folder ko scan karta hai aur missing _category_.json generate karta hai.
    Taake 'Category Index Pages' automatically kaam karein.
    """
    for root, dirs, files in os.walk(docs_path):
        # Skip the main 'docs' root itself
        if root == docs_path:
            continue
            
        category_json_path = os.path.join(root, "_category_.json")
        
        # Agar pehle se maujood hai toh touch nahi karenge
        if not os.path.exists(category_json_path):
            folder_name = os.path.basename(root)
            
            # Khubsurat label banayein (e.g. '01-Vision' -> 'Vision')
            # Hum sirf hyphen '-' ke baad wala part le sakte hain agar numbers hain
            label = folder_name.split('-')[-1] if '-' in folder_name else folder_name
            
            config_data = {
                "label": label,
                "link": {
                    "type": "generated-index",
                    "description": f"Explore documentation and research related to {label}."
                }
            }
            
            try:
                with open(category_json_path, 'w', encoding='utf-8') as f:
                    json.dump(config_data, f, indent=2)
                logger.info(f"✨ Auto-generated Category Index for: {folder_name}")
            except Exception as e:
                logger.error(f"Failed to generate index for {folder_name}: {e}")

def write_content_to_docusaurus_docs(project_path: str, contents: List[SourceContent]):
    """Writes Markdown and copies Binary Assets (Images/PDFs) to docs."""
    docs_path = os.path.join(project_path, "docs")
    os.makedirs(docs_path, exist_ok=True)

    for content in contents:
        doc_file_path = os.path.join(docs_path, content.id)
        os.makedirs(os.path.dirname(doc_file_path), exist_ok=True)
        
        try:
            if content.content_type == "binary":
                shutil.copy2(content.file_path, doc_file_path)
                logger.info(f"🖼️ Asset Synced: {content.id}")
            else:
                with open(doc_file_path, "w", encoding="utf-8") as f:
                    f.write(content.processed_content)
                logger.info(f"📂 Doc Synced: {content.id}")
        except Exception as e:
            logger.error(f"Failed to handle {doc_file_path}: {e}")
            raise BackendException(f"Asset handling error: {str(e)}", status_code=500)

def generate_docusaurus_project(contents: List[SourceContent], output_directory: str) -> DocusaurusProject:
    try:
        # 1. Folder Setup
        initialize_docusaurus_project(output_directory)
        
        # 2. Content Sync
        write_content_to_docusaurus_docs(output_directory, contents)
        
        # 3. JADOO: Generate Category Indices for all folders 🪄
        docs_path = os.path.join(output_directory, "docs")
        generate_category_indices(docs_path)

        # 4. Meta Data
        project = DocusaurusProject(
            id=os.path.basename(output_directory),
            project_path=output_directory,
            config_files=[os.path.join(output_directory, "docusaurus.config.js")],
            content_files=[c.id for c in contents],
            creation_timestamp=datetime.now(),
        )
        return project
    except BackendException as be:
        raise be
    except Exception as e:
        logger.error(f"Generation error: {e}")
        raise BackendException(f"Failed to generate project: {str(e)}", status_code=500)