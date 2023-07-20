from typing import List
from pydantic import BaseModel, field_validator, HttpUrl


class VisitedLinks(BaseModel):
    links: List[HttpUrl]