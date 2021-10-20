"""Pytest fixtures module"""
import pytest

from app import create_app


@pytest.fixture
def client():
    """Pytest Flask test client fixture

    Yields:
        class: Instance of FlaskClient
    """
    app = create_app("testing")
    with app.test_client() as test_client:
        yield test_client
