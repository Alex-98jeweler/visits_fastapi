from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime


metadata = MetaData()

visit = Table(
    'visit',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('link', String),
    Column('visited_at', DateTime, default=datetime.utcnow)
)