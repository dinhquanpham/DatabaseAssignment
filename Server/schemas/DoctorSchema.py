from pydantic import BaseModel

class DoctorSchema(BaseModel):
    doctorID: int
    departmentID: int
    name: str
    age: int
    gender: str

    class Config:
        orm_mode = True

class DoctorCreateSchema(BaseModel):
    doctorID: int
    departmentID: int
    name: str
    age: int
    gender: str

class DoctorUpdateSchema(BaseModel):
    doctorID: int
    departmentID: int
    name: str
    age: int
    gender: str