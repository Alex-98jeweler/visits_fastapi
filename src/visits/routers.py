from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import VisitedLinks

from src.database import get_async_session


router = APIRouter()


@router.post('/visited_links')
async def visited_links(
    visited_links: VisitedLinks,
    session: AsyncSession = Depends(get_async_session)
):
    return {"Hi hi": "ha ha"}