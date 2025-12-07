import os
import shutil
from datetime import datetime
from typing import List

from backend.src.models.models import SourceContent, DocusaurusProject
from backend.src.utils.logging import logger, BackendException

# LOGIC FIX: Dynamic Path Resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", "..", ".."))
DEFAULT_TEMPLATE_PATH = os.path.join(PROJECT_ROOT, "frontend", "docusaurus")

# Use Env Var if set, otherwise use calculated default
DOCUSAURUS_TEMPLATE_PATH = os.getenv("DOCUSAURUS_TEMPLATE_PATH", DEFAULT_TEMPLATE_PATH)

def initialize_docusaurus_project(output_directory: str):
    """
    Smart Initialization:
    - If project exists: Only clears the 'docs' folder (Incremental Update).
    - If project missing: Copies the full template (Full Gen).
    """
    
    # Normalize paths for Windows comparison
    abs_output = os.path.abspath(output_directory)
    abs_template = os.path.abspath(DOCUSAURUS_TEMPLATE_PATH)

    # Check if the output directory looks like a valid Docusaurus project
    config_exists = os.path.exists(os.path.join(abs_output, "docusaurus.config.js"))
    
    if os.path.exists(abs_output) and config_exists:
        logger.info(f"Existing Docusaurus project detected at {output_directory}. Switch to INCREMENTAL UPDATE.")
        
        # Sirf 'docs' folder ko saaf karein, poore project ko nahi
        docs_path = os.path.join(abs_output, "docs")
        if os.path.exists(docs_path):
            try:
                # Remove all files in docs folder
                for filename in os.listdir(docs_path):
                    file_path = os.path.join(docs_path, filename)
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                logger.info("Cleaned existing 'docs' directory.")
            except Exception as e:
                logger.warning(f"Could not fully clean docs folder: {e}")
        else:
            os.makedirs(docs_path, exist_ok=True)
            
        return  # Yahan se wapas chale jao, Template Copy karne ki zaroorat nahi hai.

    # --- FULL GENERATION (New Project) ---
    if not os.path.exists(DOCUSAURUS_TEMPLATE_PATH):
        error_msg = f"Docusaurus template not found at: {DOCUSAURUS_TEMPLATE_PATH}"
        logger.error(error_msg)
        raise BackendException(error_msg, status_code=500)

    if os.path.exists(output_directory):
        logger.info(f"Removing existing directory for fresh install: {output_directory}")
        try:
            shutil.rmtree(output_directory)
        except Exception as e:
            # Agar delete fail ho (e.g. node_modules locked), to error mat throw karo, bas warn karo
            logger.warning(f"Could not delete existing directory (likely locked): {e}. Attempting to overwrite.")

    logger.info(
        f"Copying Docusaurus template from {DOCUSAURUS_TEMPLATE_PATH} to {output_directory}"
    )
    # Ignore node_modules when copying template (just in case)
    shutil.copytree(
        DOCUSAURUS_TEMPLATE_PATH, 
        output_directory, 
        dirs_exist_ok=True, 
        ignore=shutil.ignore_patterns('node_modules', '.docusaurus', '.git')
    )
    logger.info(f"Docusaurus project initialized at {output_directory}")


def write_content_to_docusaurus_docs(project_path: str, contents: List[SourceContent]):
    """Writes processed SourceContent into the Docusaurus docs directory."""
    docs_path = os.path.join(project_path, "docs")
    os.makedirs(docs_path, exist_ok=True)

    for content in contents:
        safe_filename = os.path.basename(content.file_path)
        doc_file_path = os.path.join(docs_path, safe_filename)
        
        logger.info(f"Writing content for {safe_filename} to {doc_file_path}")
        try:
            with open(doc_file_path, "w", encoding="utf-8") as f:
                f.write(content.processed_content)
        except Exception as e:
            logger.error(f"Failed to write file {doc_file_path}: {e}")
            raise BackendException(f"File write error: {str(e)}", status_code=500)


def generate_docusaurus_project(
    contents: List[SourceContent], output_directory: str
) -> DocusaurusProject:
    """Generates a complete Docusaurus project from processed source contents."""
    try:
        initialize_docusaurus_project(output_directory)
        write_content_to_docusaurus_docs(output_directory, contents)

        config_files = [
            os.path.join(output_directory, "docusaurus.config.js"),
            os.path.join(output_directory, "sidebar.js"),
        ]
        content_files = [
            os.path.join(output_directory, "docs", os.path.basename(c.file_path)) for c in contents
        ]

        project = DocusaurusProject(
            id=os.path.basename(output_directory),
            project_path=output_directory,
            config_files=config_files,
            content_files=content_files,
            creation_timestamp=datetime.now(),
        )
        logger.info(
            f"Docusaurus project '{project.id}' generated successfully at {project.project_path}"
        )
        return project
    except BackendException as be:
        raise be
    except Exception as e:
        logger.error(f"Error generating Docusaurus project: {e}")
        raise BackendException(f"Failed to generate Docusaurus project: {str(e)}", status_code=500)