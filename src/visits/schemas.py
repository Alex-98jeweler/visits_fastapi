from typing import Any, List
from pydantic import BaseModel, HttpUrl
from enum import Enum


class VisitedLinks(BaseModel):
    links: List[HttpUrl]


class Statuses(str, Enum):
    success = 'success'
    error = 'error'


class CommonResponses(BaseModel):
    status: Statuses
    message: str
    data: Any