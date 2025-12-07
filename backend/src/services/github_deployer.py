# backend/src/services/github_deployer.py
import os
import subprocess
from datetime import datetime
from backend.src.utils.logging import logger, BackendException

def deploy_to_github_pages(
    project_path: str, github_repo_url: str, branch: str = "gh-pages"
) -> str:
    """Deploys the built Docusaurus project to GitHub Pages."""
    logger.info(
        f"Starting GitHub Pages deployment for project: {project_path} to {github_repo_url} on branch {branch}"
    )
    try:
        # Ensure it's a git repository and init if not
        git_dir = os.path.join(project_path, ".git")
        if not os.path.exists(git_dir):
            logger.info(f"Initializing git repository in {project_path}")
            subprocess.run(
                ["git", "init"], cwd=project_path, check=True, capture_output=True, text=True
            )
            subprocess.run(
                ["git", "remote", "add", "origin", github_repo_url],
                cwd=project_path, check=True, capture_output=True, text=True,
            )
        else:
            # Ensure remote matches
            current_remote_url = subprocess.run(
                ["git", "config", "--get", "remote.origin.url"],
                cwd=project_path, check=False, capture_output=True, text=True,
            ).stdout.strip()
            
            # Logic adjustment: Only set/update if URL is different and not empty
            if current_remote_url != github_repo_url:
                logger.info(f"Updating git remote origin URL to {github_repo_url}")
                # Handle case where origin might not exist cleanly
                cmd = ["git", "remote", "set-url", "origin", github_repo_url]
                if not current_remote_url:
                     cmd = ["git", "remote", "add", "origin", github_repo_url]
                
                subprocess.run(cmd, cwd=project_path, check=True, capture_output=True, text=True)

        # Add build output to git
        build_dir = os.path.join(project_path, "build")
        if not os.path.exists(build_dir):
            raise BackendException(
                f"Docusaurus build output not found: {build_dir}. Did the build succeed?",
                status_code=500,
            )

        subprocess.run(
            ["git", "add", "-f", "build"], cwd=project_path, check=True, capture_output=True, text=True,
        )

        commit_message = f"Deploy Docusaurus book via API on {datetime.now().isoformat()}"
        subprocess.run(
            ["git", "commit", "-m", commit_message], cwd=project_path, check=True, capture_output=True, text=True,
        )

        subprocess.run(
            ["git", "subtree", "push", "--prefix", "build", "origin", branch],
            cwd=project_path, check=True, capture_output=True, text=True,
        )

        deployment_url = f"{github_repo_url.replace('.git', '')}/tree/{branch}"
        logger.info(f"GitHub Pages deployment successful. URL: {deployment_url}")
        return deployment_url

    except BackendException as be:
        # FIX: Re-raise BackendException as-is, don't wrap it in unexpected error
        raise be
    except subprocess.CalledProcessError as e:
        logger.error(f"GitHub Pages deployment failed. Stdout: {e.stdout}, Stderr: {e.stderr}")
        raise BackendException(f"GitHub Pages deployment failed: {e.stderr}", status_code=500)
    except FileNotFoundError as e:
        logger.error(f"git command not found. Ensure Git is installed and in PATH. Error: {e}")
        raise BackendException(
            f"Deployment prerequisite missing: {e}. Is Git installed?", status_code=500
        )
    except Exception as e:
        logger.error(f"An unexpected error occurred during GitHub Pages deployment: {e}")
        raise BackendException(f"Unexpected error during deployment: {str(e)}", status_code=500)