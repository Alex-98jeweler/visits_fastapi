from datetime import datetime


def from_timestamp_to_datetime(
    timestamp: int
) -> datetime:
    if not timestamp:
        return None
    return datetime.fromtimestamp(timestamp)
