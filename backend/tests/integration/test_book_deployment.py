# backend/tests/integration/test_book_deployment.py
import pytest
from fastapi.testclient import TestClient
from datetime import datetime
import os
import shutil
import subprocess  # Fixed: Imported directly, not from unittest.mock
from unittest.mock import MagicMock

# Ensure imports are correct based on project structure
from backend.src.api.main import app

client = TestClient(app)

@pytest.fixture
def setup_temp_project_and_output_dir(tmp_path):
    project_path = tmp_path / "temp_docusaurus_project"
    project_path.mkdir()
    # Create necessary files for the builder to pass checks
    (project_path / "package.json").write_text('{ "name": "test-app", "version": "1.0.0", "scripts": { "build": "echo build-success" } }', encoding="utf-8")
    (project_path / "docusaurus.config.js").write_text('module.exports = {};', encoding="utf-8")
    
    # Create build dir simulated
    build_dir = project_path / "build"
    build_dir.mkdir()
    (build_dir / "index.html").write_text("<html><body>Hello</body></html>", encoding="utf-8")

    yield str(project_path)
    
    if os.path.exists(project_path):
        shutil.rmtree(project_path)

def test_deploy_book_success(mock_subprocess_run, setup_temp_project_and_output_dir):
    # Setup Mocks for: npm install, npm build, git init, remote add, add, commit, push
    # Note: 7 calls expected based on current logic (skipping config check for new repo)
    mock_subprocess_run.side_effect = [
        MagicMock(stdout="npm install success", stderr="", returncode=0),
        MagicMock(stdout="build success", stderr="", returncode=0),
        MagicMock(stdout="git init success", stderr="", returncode=0),
        MagicMock(stdout="git remote add success", stderr="", returncode=0),
        # MagicMock(stdout="", stderr="", returncode=1), # Removed config check mock
        MagicMock(stdout="git add success", stderr="", returncode=0),
        MagicMock(stdout="git commit success", stderr="", returncode=0),
        MagicMock(stdout="git subtree push success", stderr="", returncode=0),
    ]

    repo_url = "https://github.com/testuser/testrepo.git"
    response = client.post(
        "/deploy-book",
        json={
            "project_path": setup_temp_project_and_output_dir,
            "github_repo_url": repo_url,
            "branch": "gh-pages"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert "https://github.com/testuser/testrepo/tree/gh-pages" in data["deployment_url"]

def test_deploy_book_build_failure(mock_subprocess_run, setup_temp_project_and_output_dir):
    # Simulate npm install failure
    mock_subprocess_run.side_effect = [
        subprocess.CalledProcessError(1, cmd="npm install", output="", stderr="npm install failed")
    ]
    response = client.post(
        "/deploy-book",
        json={
            "project_path": setup_temp_project_and_output_dir,
            "github_repo_url": "https://github.com/testuser/testrepo.git"
        }
    )
    assert response.status_code == 500
    assert "Docusaurus build failed" in response.json()["detail"]