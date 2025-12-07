#backend/src/services/docusaurus_builder.py
import subprocess
import os
from backend.src.utils.logging import logger, BackendException


def build_docusaurus_project(project_path: str, output_dir: str = "build"):
    """Builds the Docusaurus project located at project_path."""
    logger.info(f"Starting Docusaurus build for project: {project_path}")
    try:
                # Pre-check for package.json
        package_json_path = os.path.join(project_path, 'package.json')
        if not os.path.exists(package_json_path):
            raise BackendException(f"Invalid Docusaurus project: package.json not found in {project_path}", status_code=400)

        # Ensure npm dependencies are installed (assuming they are not installed during generation)
        install_result = subprocess.run(
            ["npm", "install"], cwd=project_path, check=True, capture_output=True, text=True
        )
        logger.info(f"npm install completed for {project_path}")
        logger.debug(f"npm install output:\n{install_result.stdout}")

        # Run Docusaurus build command
        result = subprocess.run(
            ["npm", "run", "build"], cwd=project_path, check=True, capture_output=True, text=True
        )
        logger.info(f"Docusaurus build successful for {project_path}")
        logger.debug(f"Build output:\n{result.stdout}")
        return os.path.join(project_path, output_dir)  # Docusaurus build output directory
    except subprocess.CalledProcessError as e:
        logger.error(
            f"Docusaurus build failed for {project_path}. Stdout: {e.stdout}, Stderr: {e.stderr}"
        )
        raise BackendException(f"Docusaurus build failed: {e.stderr}", status_code=500)
    except FileNotFoundError as e:
        logger.error(
            f"npm or docusaurus command not found. Ensure Node.js and Docusaurus are installed and in PATH. Error: {e}"
        )
        raise BackendException(
            f"Build prerequisite missing: {e}. Is Node.js installed?", status_code=500
        )
    except Exception as e:
        logger.error(f"An unexpected error occurred during Docusaurus build: {e}")
        raise BackendException(f"Unexpected error during build: {str(e)}", status_code=500)
