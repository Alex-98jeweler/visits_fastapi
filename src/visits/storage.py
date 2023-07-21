from datetime import datetime
import json
import random
from uuid import uuid4

from fastapi import Depends
from aioredis.client import Redis

from src.redis_instance import get_redis_conn
from src.visits.utils import filter_list, prepare_list
from .schemas import VisitedLinks


async def add_links(
    redis_client: Redis, 
    visited_links: VisitedLinks
):
    links = visited_links.links
    link_objs = []
    prepare_list(links, link_objs)
    for link_obj in link_objs:
        await redis_client.lpush('links', json.dumps(link_obj))


async def get_domains(
    redis_client: Redis,
    from_: float = None,
    to: float = None
):
    length = await redis_client.llen('links')
    links = await redis_client.lrange('links', 0, length)
    links = list(map(json.loads, links))
    links.sort(reverse=True, key=lambda x: x['visited_at'])
    buf = filter_list(links, from_, to)
    result = [link['link'] for link in buf]
    return result
    