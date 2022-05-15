from pydantic import BaseModel

class DepartmentSchema(BaseModel):
    departmentID: int
    departmentName: str

    class Config:
        orm_mode = True

class DepartmentCreateSchema(BaseModel):
    departmentID: int
    departmentName: str

class DepartmentUpdateSchema(BaseModel):
    departmentID: int
    departmentName: str