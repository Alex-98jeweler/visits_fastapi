from datetime import datetime
from sqlalchemy import select, insert, and_
from sqlalchemy.ext.asyncio import AsyncSession

from .models import visit


async def get_domains(session: AsyncSession, from_: datetime = None, to: datetime = None):

    query = select(visit)
    if from_: query = query.where(visit.c.visited_at >= from_)
    if to: query = query.where(visit.c.visited_at <= to)
    print(query)
    result = await session.execute(query)
    return result.fetchall()
    