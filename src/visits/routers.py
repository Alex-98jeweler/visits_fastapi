from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .utils import from_timestamp_to_datetime
from .schemas import VisitedLinks
from . import crud_db
from src.database import get_async_session



router = APIRouter()


@router.post('/visited_links')
async def visited_links(
    visited_links: VisitedLinks,
    session: AsyncSession = Depends(get_async_session)
):
    return {"Hi hi": "ha ha"}


@router.get('/visited_domains',)
async def visited_domains(
    from_: int = None,
    to: int = None,
    session: AsyncSession = Depends(get_async_session)
):
    from_dt = from_timestamp_to_datetime(from_)
    to_dt = from_timestamp_to_datetime(to)
    await crud_db.get_domains(session, from_dt, to_dt)
    return {}