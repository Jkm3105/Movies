from pydantic import BaseModel

class ScreenCreate(BaseModel):
    name: str
    theatre_id: str

class ScreenResponse(BaseModel):
    name: str
    id: str
    theatre_id: str
    
    class Config:
        from_attributes = True