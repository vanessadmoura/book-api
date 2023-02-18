import pytest
from app import create_app


@pytest.fixture(scope="session", name="app")
def fixture_app():
    app = create_app()
    return app