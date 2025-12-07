#backend/src/models/models.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class SourceContent(BaseModel):
    id: str
    file_path: str
    content_type: str
    raw_content: str  # Can be bytes, but for simplicity we'll use string for now
    processed_content: str
    last_modified: datetime


class DocusaurusProject(BaseModel):
    id: str
    project_path: str
    config_files: List[str]
    content_files: List[str]
    creation_timestamp: datetime


class GeneratedBook(BaseModel):
    id: str
    output_path: str
    deployment_url: Optional[str] = None
    build_timestamp: datetime
    deployment_timestamp: Optional[datetime] = None
