import pytest
from config.settings import BASE_URL


@pytest.fixture(scope="session")
def base_url() -> str:
    """Provide the configured base URL for the test session."""
    return BASE_URL
