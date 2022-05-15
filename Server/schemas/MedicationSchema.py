from pydantic import BaseModel

class MedicationSchema(BaseModel):
    medicineCode: int
    medicineName: str
    medicineCost: int
    medicineDescription: str
    class Config:
        orm_mode = True

class MedicationCreateSchema(BaseModel):
    medicineCode: int
    medicineName: str
    medicineCost: int
    medicineDescription: str

class MedicationUpdateSchema(BaseModel):
    medicineCode: int
    medicineName: str
    medicineCost: int
    medicineDescription: str