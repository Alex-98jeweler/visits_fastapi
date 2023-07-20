from datetime import datetime
from typing import Any
from .schemas import CommonResponses, Statuses

def from_timestamp_to_datetime(
    timestamp: int
) -> datetime:
    if not timestamp:
        return None
    return datetime.fromtimestamp(timestamp)

def build_response_body(
    is_success: bool,
    message: str = '',
    data: Any = []
) -> CommonResponses:
    response_dict = {}
    if is_success:
        response_dict['status'] = Statuses.success
    else:
        response_dict['status'] = Statuses.error
    response_dict['message'] = message
    response_dict['data'] = data
    response = CommonResponses.parse_obj(response_dict)
    return response

