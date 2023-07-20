from datetime import datetime
from typing import Any, List
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

def get_urls_list(db_sequence) -> List[str]:
    result = []
    for row in db_sequence:
        result.append(row[-1])
    return result
