from datetime import datetime
from typing import List
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from .models import visit
from .schemas import HttpUrl


async def get_domains(
    session: AsyncSession,
    from_: datetime = None,
    to: datetime = None
):

    query = select(visit)
    if from_:
        query = query.where(visit.c.visited_at >= from_)
    if to:
        query = query.where(visit.c.visited_at <= to)
    result = await session.execute(query.distinct())
    return result.fetchall()


async def create_visit(
    links: List[HttpUrl],
    session: AsyncSession
):
    for link in links:
        query = insert(visit).values(link=link.__str__())
        await session.execute(query)
    await session.commit()
