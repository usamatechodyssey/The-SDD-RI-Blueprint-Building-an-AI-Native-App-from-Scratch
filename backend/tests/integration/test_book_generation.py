# backend/tests/integration/test_book_generation.py
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import os
import shutil

# Correct Absolute Import
from backend.src.api.main import app

client = TestClient(app)

@pytest.fixture
def setup_temp_output_dir(tmp_path):
    output_dir = tmp_path / "docusaurus_output"
    output_dir.mkdir()
    return str(output_dir)

@pytest.fixture
def dummy_source_file(tmp_path):
    file_path = tmp_path / "source.md"
    file_path.write_text("# Test Source\nThis is a dummy source file.", encoding="utf-8")
    return str(file_path)

@patch("backend.src.services.docusaurus_generator.initialize_docusaurus_project")
def test_generate_book_success(mock_init_project, setup_temp_output_dir, dummy_source_file):
    print("\n[TEST] Running Success Scenario...")
    mock_init_project.return_value = None
    
    response = client.post(
        "/generate-book",
        json={
            "source_content_paths": [dummy_source_file],
            "output_directory": setup_temp_output_dir
        }
    )
    print(f"[TEST] Success Response: {response.status_code}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["project_path"] == setup_temp_output_dir

def test_generate_book_empty_list(setup_temp_output_dir):
    """Test 422 Validation Error for empty list"""
    print("\n[TEST] Running Empty List Validation...")
    response = client.post(
        "/generate-book",
        json={
            "source_content_paths": [], 
            "output_directory": setup_temp_output_dir
        }
    )
    print(f"[TEST] Empty List Response: {response.status_code}")
    assert response.status_code == 422

@patch("os.path.exists")
def test_generate_book_missing_file(mock_exists, setup_temp_output_dir):
    """Test 400 Error for missing file (Mocked to avoid FS hang)"""
    print("\n[TEST] Running Missing File Check...")
    
    # Simulate file not found
    mock_exists.return_value = False
    
    response = client.post(
        "/generate-book",
        json={
            "source_content_paths": ["F:/fake/path/file.md"],
            "output_directory": setup_temp_output_dir
        }
    )
    print(f"[TEST] Missing File Response: {response.status_code}")
    
    # Check for 400 (BackendException) or 500 depending on handler
    # We expect 400 based on our code logic
    assert response.status_code == 400
    assert "Source file not found" in response.json()["detail"]