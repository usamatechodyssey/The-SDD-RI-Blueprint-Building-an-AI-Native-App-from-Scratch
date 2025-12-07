import pytest
from unittest.mock import patch

@pytest.fixture
def mock_subprocess_run():
    """Mocks subprocess.run globally for integration tests to avoid real shell commands."""
    with patch("subprocess.run") as mock_run:
        yield mock_run