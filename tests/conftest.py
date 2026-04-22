from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities as app_activities
from src.app import app


INITIAL_ACTIVITIES = deepcopy(app_activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Restore the in-memory activities data before and after each test."""
    app_activities.clear()
    app_activities.update(deepcopy(INITIAL_ACTIVITIES))
    yield
    app_activities.clear()
    app_activities.update(deepcopy(INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
