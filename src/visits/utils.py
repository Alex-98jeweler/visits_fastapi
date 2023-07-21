from datetime import datetime
from typing import Any, List
from uuid import uuid4

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


def prepare_list(links: List[str], src: List):
    for link in links:
        src.append(
            {
                'id': uuid4().__str__(),
                'link': link.__str__(),
                'visited_at': datetime.now().timestamp()
            }
        )


def filter_list(links_list: list, from_, to):
    buf = links_list[::]
    for link in links_list:
        if from_ and link['visited_at'] < from_:
            links_list.remove(link)
        elif to and link['visited_at'] > to:
            links_list.remove(link)
    return links_list
