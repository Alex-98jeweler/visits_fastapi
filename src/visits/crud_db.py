from datetime import datetime
from typing import List
from sqlalchemy import select, insert, Column, String
from sqlalchemy.ext.asyncio import AsyncSession

from .utils import get_urls_list
from .models import visit
from .schemas import HttpUrl


async def get_domains(
    session: AsyncSession,
    from_: datetime = None,
    to: datetime = None
) -> List[str]:

    query = select(visit.c.link)
    if from_:
        query = query.where(visit.c.visited_at >= from_)
    if to:
        query = query.where(visit.c.visited_at <= to)
    result = await session.execute(query.distinct('link'))
    urls_list = get_urls_list(result.fetchall())
    return urls_list


async def create_visit(
    links: List[HttpUrl],
    session: AsyncSession
):
    for link in links:
        query = insert(visit).values(link=link.__str__())
        await session.execute(query)
    await session.commit()
