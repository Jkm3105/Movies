from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    description: str
    poster_url: str

class MovieResponse(BaseModel):
    id: str
    title: str
    description: str
    poster_url: str

    class Config:
        from_attributes = True  