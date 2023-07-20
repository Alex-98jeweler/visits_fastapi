from typing import List
from pydantic import BaseModel, HttpUrl


class VisitedLinks(BaseModel):
    links: List[HttpUrl]
