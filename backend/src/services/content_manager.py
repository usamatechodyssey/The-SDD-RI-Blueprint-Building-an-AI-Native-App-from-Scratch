import os
import shutil
from typing import List, Dict
from backend.src.utils.logging import logger, BackendException

def list_docs_tree(docs_path: str) -> List[str]:
    """Docs folder ke andar maujood tamam files ki relative paths nikalta hai."""
    file_list = []
    if not os.path.exists(docs_path):
        return file_list

    for root, _, files in os.walk(docs_path):
        for file in files:
            if file.lower().endswith('.md'):
                rel_path = os.path.relpath(os.path.join(root, file), docs_path)
                file_list.append(rel_path.replace("\\", "/"))
    return sorted(file_list)

def delete_path(docs_path: str, relative_path: str):
    """File ya poora Folder delete karne ka skill."""
    full_path = os.path.abspath(os.path.join(docs_path, relative_path))
    
    # Security: Check ke kahin docs folder se bahar na nikal jaye
    if not full_path.startswith(os.path.abspath(docs_path)):
        raise BackendException("Security Alert: Access Denied to this path.", status_code=403)

    if not os.path.exists(full_path):
        raise BackendException(f"Path not found: {relative_path}", status_code=404)

    try:
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
            logger.info(f"🗑️ Folder Deleted: {relative_path}")
        else:
            os.remove(full_path)
            logger.info(f"🗑️ File Deleted: {relative_path}")
    except Exception as e:
        raise BackendException(f"Deletion failed: {str(e)}", status_code=500)