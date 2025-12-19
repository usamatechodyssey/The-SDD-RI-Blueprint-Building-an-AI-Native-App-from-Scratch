# backend/tests/unit/test_deployment_services.py
import pytest
import subprocess
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

# Absolute imports
from backend.src.services.docusaurus_builder import build_docusaurus_project
from backend.src.services.github_deployer import deploy_to_github_pages
from backend.src.utils.logging import BackendException

@pytest.fixture
def mock_subprocess_run():
    with patch('subprocess.run') as mock_run:
        yield mock_run

@pytest.fixture
def dummy_docusaurus_project(tmp_path):
    project_path = tmp_path / "my-docusaurus-app"
    project_path.mkdir()
    (project_path / "package.json").write_text('{ "name": "test-app", "version": "1.0.0", "scripts": { "build": "echo build-success" } }', encoding="utf-8")
    (project_path / "docusaurus.config.js").write_text('module.exports = {};', encoding="utf-8")
    return str(project_path)

@pytest.fixture
def built_docusaurus_project(dummy_docusaurus_project):
    base_path = Path(dummy_docusaurus_project)
    build_dir = base_path / "build"
    build_dir.mkdir(exist_ok=True)
    (build_dir / "index.html").write_text("<html><body>Hello</body></html>", encoding="utf-8")
    return dummy_docusaurus_project

# --- Docusaurus Builder Tests (These were passing) ---
def test_build_docusaurus_project_success(mock_subprocess_run, dummy_docusaurus_project):
    mock_subprocess_run.return_value = MagicMock(stdout="output", stderr="", returncode=0)
    build_path = build_docusaurus_project(dummy_docusaurus_project)
    assert mock_subprocess_run.call_count == 2
    assert "build" in build_path

def test_build_docusaurus_project_npm_install_failure(mock_subprocess_run, dummy_docusaurus_project):
    mock_subprocess_run.side_effect = [
        subprocess.CalledProcessError(1, cmd="npm install", output="", stderr="npm install failed")
    ]
    with pytest.raises(BackendException, match="npm install failed"):
        build_docusaurus_project(dummy_docusaurus_project)

def test_build_docusaurus_project_build_failure(mock_subprocess_run, dummy_docusaurus_project):
    mock_subprocess_run.side_effect = [
        MagicMock(stdout="npm install success", stderr="", returncode=0),
        subprocess.CalledProcessError(1, cmd="npm run build", output="", stderr="docusaurus build failed")
    ]
    with pytest.raises(BackendException, match="docusaurus build failed"):
        build_docusaurus_project(dummy_docusaurus_project)

def test_build_docusaurus_project_npm_not_found(mock_subprocess_run, dummy_docusaurus_project):
    mock_subprocess_run.side_effect = FileNotFoundError("npm not found")
    with pytest.raises(BackendException, match="Build prerequisite missing"):
        build_docusaurus_project(dummy_docusaurus_project)

# --- GitHub Deployer Tests (FIXED) ---
def test_deploy_to_github_pages_success(mock_subprocess_run, built_docusaurus_project):
    # FIX: Logic for new repo is: Init -> Remote Add -> Add -> Commit -> Push (5 steps)
    # The 'git config get' step is SKIPPED because it's in the 'else' block.
    mock_subprocess_run.side_effect = [
        MagicMock(stdout="git init success", stderr="", returncode=0),       # 1. Init
        MagicMock(stdout="git remote add success", stderr="", returncode=0), # 2. Remote Add
        # REMOVED: MagicMock for 'git config get'
        MagicMock(stdout="git add success", stderr="", returncode=0),        # 3. Add
        MagicMock(stdout="git commit success", stderr="", returncode=0),     # 4. Commit
        MagicMock(stdout="git subtree push success", stderr="", returncode=0), # 5. Push
    ]
    repo_url = "https://github.com/user/repo.git"
    deployment_url = deploy_to_github_pages(built_docusaurus_project, repo_url)

    assert "https://github.com/user/repo/tree/gh-pages" in deployment_url
    assert mock_subprocess_run.call_count == 5 # Logic confirmed as 5 calls

def test_deploy_to_github_pages_git_not_found(mock_subprocess_run, built_docusaurus_project):
    mock_subprocess_run.side_effect = FileNotFoundError("git not found")
    repo_url = "https://github.com/user/repo.git"
    with pytest.raises(BackendException, match="Deployment prerequisite missing"):
        deploy_to_github_pages(built_docusaurus_project, repo_url)

def test_deploy_to_github_pages_push_failure(mock_subprocess_run, built_docusaurus_project):
    # FIX: Aligned mock sequence with 5-step logic
    mock_subprocess_run.side_effect = [
        MagicMock(stdout="git init success", stderr="", returncode=0),       # 1. Init
        MagicMock(stdout="git remote add success", stderr="", returncode=0), # 2. Remote Add
        # REMOVED: MagicMock for 'git config get'
        MagicMock(stdout="git add success", stderr="", returncode=0),        # 3. Add
        MagicMock(stdout="git commit success", stderr="", returncode=0),     # 4. Commit
        subprocess.CalledProcessError(1, cmd="git subtree push", output="", stderr="push failed") # 5. Push (FAIL)
    ]
    repo_url = "https://github.com/user/repo.git"
    with pytest.raises(BackendException, match="GitHub Pages deployment failed"):
        deploy_to_github_pages(built_docusaurus_project, repo_url)

def test_deploy_to_github_pages_no_build_directory(mock_subprocess_run, dummy_docusaurus_project):
    repo_url = "https://github.com/user/repo.git"
    with pytest.raises(BackendException, match="Docusaurus build output not found"):
        deploy_to_github_pages(dummy_docusaurus_project, repo_url)