from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import Response
from fastapi import status
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
    links = visited_links.links
    try:
        await crud_db.create_visit(links, session)
    except Exception as e:
        return Response({
            'status': 'error', 
            'message': str(e)
            }, 
        status_code=status.HTTP_200_OK
        )
    return {"status": "success"}


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