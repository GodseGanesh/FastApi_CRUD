from pydantic import BaseModel
from typing import List, Optional

class ReviewBase(BaseModel):
    content: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int
    class Config:
        from_attributes = True

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int
    reviews: List[ReviewOut] = []

    class Config:
        from_attributes = True
