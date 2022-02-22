from typing import Optional
from beanie import Document
from pydantic import BaseModel


class Hero(Document):
    name: str
    title: str
    weapons: list[str]


class HeroUpdate(BaseModel):
    name: Optional[str]
    title: Optional[str]
    weapons: Optional[str]