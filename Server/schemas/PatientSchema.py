from pydantic import BaseModel

class PatientSchema(BaseModel):
    patientID: int
    name: str
    age: int
    gender: str
    address: str
    disease: str
    patientStatus: str

    class Config:
        orm_mode = True

class PatientCreateSchema(BaseModel):
    patientID: int
    name: str
    age: int
    gender: str
    address: str
    disease: str
    patientStatus: str

class PatientUpdateSchema(BaseModel):
    patientID: int
    name: str
    age: int
    gender: str
    address: str
    disease: str
    patientStatus: str