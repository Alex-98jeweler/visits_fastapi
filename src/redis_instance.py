import aioredis

from src.config import REDIS_URL


redis = aioredis.from_url(REDIS_URL)


async def get_redis_conn():
    async with redis.client() as conn:
        yield conn

