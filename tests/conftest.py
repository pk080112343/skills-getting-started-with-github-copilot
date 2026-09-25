import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    original_state = copy.deepcopy(activities)
    test_client = TestClient(app)

    yield test_client

    activities.clear()
    activities.update(copy.deepcopy(original_state))
