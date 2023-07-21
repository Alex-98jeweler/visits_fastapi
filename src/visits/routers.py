from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from aioredis.client import Redis

from . import crud_db
from src.redis_instance import get_redis_conn
from src.database import get_async_session
from . import storage
from .schemas import CommonResponses, VisitedLinks
from .utils import from_timestamp_to_datetime, build_response_body


router = APIRouter()


@router.post('/visited_links', response_model=CommonResponses)
async def visited_links(
    visited_links: VisitedLinks,
    redis: AsyncSession = Depends(get_redis_conn)
):
    try:
        await storage.add_links(redis, visited_links)
        response = build_response_body(is_success=True, message ='success')
    except Exception as e:
        message = str(e)
        return build_response_body(False, message)
    return response


@router.get('/visited_domains', response_model=CommonResponses)
async def visited_domains(
    from_: float = None,
    to: float = None,
    redis: Redis = Depends(get_redis_conn)
):
    try:
        domains = await storage.get_domains(redis, from_, to)
        response = build_response_body(is_success=True, message='success', data=domains)
    except Exception as e:
        message = str(e)
        return build_response_body(False, message)
    return response
