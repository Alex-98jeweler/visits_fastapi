from datetime import datetime


from sqlalchemy import select

def from_timestamp_to_datetime(
    timestamp: int
) -> datetime:
    if not timestamp:
        return None
    return datetime.fromtimestamp(timestamp)
