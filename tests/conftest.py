import pytest
from app import create_app
from app.model import db
from dynaconf import settings


@pytest.fixture(scope="session", name="app")
def fixture_app():
    app = create_app()
    with app.app_context():
        db.create_all()
    return app

@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
