from pydantic import BaseModel

class TheatreCreate(BaseModel):
    name: str
    location: str

class TheatreResponse(BaseModel):
    id: str
    name: str
    location: str
    
    class Config:
        from_attributes = True