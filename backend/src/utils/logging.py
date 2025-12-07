#backend/src/utils/logging.py
import logging

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG for more verbose output
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


class BackendException(Exception):
    """Custom exception for backend errors."""

    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


def handle_error(e: Exception, logger: logging.Logger = logger):
    """Generic error handler that logs the exception."""
    if isinstance(e, BackendException):
        logger.error(f"Backend Exception: {e.status_code} - {e.message}")
    else:
        logger.exception(f"An unexpected error occurred: {e}")
