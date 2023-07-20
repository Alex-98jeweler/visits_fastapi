from typing import AsyncGenerator

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

import src.config as conf


DNS = f'postgresql+asyncpg://{conf.DB_USER}:{conf.DB_PWD}@{conf.DB_HOST}:{conf.DB_PORT}/{conf.DB_NAME}'

engine = create_async_engine(DNS)

async_sessionmaker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False

)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker() as session:
        yield session
