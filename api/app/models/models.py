from pydantic import BaseModel
from datetime import date

class PostBase(BaseModel):
    title: str
    content: str
    author: str


class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    id: int


class Post(PostBase):
    id: int
    date_created: date

