import asyncio
from typing import AsyncGenerator

import pytest
import aioredis
from aioredis.client import Redis
from httpx import AsyncClient
from fastapi.testclient import TestClient

from src.main import app
from src.redis_instance import get_redis_conn
from src.config import REDIS_URL_TEST


redis = aioredis.from_url(REDIS_URL_TEST)


async def get_redis_conn_test() -> AsyncGenerator[Redis, None]:
    async with redis.client() as conn:
        yield conn


app.dependency_overrides[get_redis_conn] = get_redis_conn_test


@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
