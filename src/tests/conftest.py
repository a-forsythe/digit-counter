import os
import pytest
import redis

from app import app as flask_app


@pytest.fixture
def client():
    return flask_app.test_client()


@pytest.fixture(scope="module")
def redis_client():
    return redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)
