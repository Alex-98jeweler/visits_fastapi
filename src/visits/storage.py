from fastapi import Depends
from aioredis.client import Redis

from src.redis_instance import get_redis_conn


async def test_redis(redis_client: Redis):
    await redis_client.set("test1", "test2")