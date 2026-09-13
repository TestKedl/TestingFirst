from datetime import datetime

from pydantic import BaseModel, Field, field_validator

ALLOWED_GENRES = ["fiction", "non-fiction", "sci-fi", "biography"]

class BookCreate(BaseModel):
    title:str = Field(min_length=2)
    author:str = Field(min_length=2)
    pages:int = Field(gt=0)
    genre: str

    @field_validator('genre')
    @classmethod
    def only_fromlist(cls,v):
        if v not in ALLOWED_GENRES:
            raise ValueError("Not acceptable")
        return v

    @field_validator("author")
    @classmethod
    def check_strip(cls,v):
        if not v.strip():
            raise ValueError("Can't be with _")
        return v

class BookResponse(BookCreate):
    id:int
    added_at:datetime
    age:int