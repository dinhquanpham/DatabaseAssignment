from pydantic import BaseModel

class RoomSchema(BaseModel):
    roomNumber: int
    roomType: str
    status: str
    class Config:
        orm_mode = True

class RoomCreateSchema(BaseModel):
    roomNumber: int
    roomType: str
    status: str

class RoomUpdateSchema(BaseModel):
    roomNumber: int
    roomType: str
    status: str