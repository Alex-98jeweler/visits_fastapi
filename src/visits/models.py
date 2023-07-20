from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func

metadata = MetaData()

visit = Table(
    'visit',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('link', String),
    Column('visited_at', DateTime, server_default=func.utcnow())
)