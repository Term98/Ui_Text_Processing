from typing import List
from pydantic import BaseModel


class NamedUrl(BaseModel):
    name: str
    url: str


class inputInfo(BaseModel):
    input: str
