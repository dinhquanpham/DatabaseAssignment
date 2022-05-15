from pydantic import BaseModel

class PrescriptionSchema(BaseModel):
    prescriptionID: int
    appointmentID: int
    medicineCode: int
    paymentID: int
    dose: str

    class Config:
        orm_mode = True

class PrescriptionCreateSchema(BaseModel):
    prescriptionID: int
    appointmentID: int
    medicineCode: int
    paymentID: int
    dose: str

class PrescriptionUpdateSchema(BaseModel):
    prescriptionID: int
    appointmentID: int
    medicineCode: int
    paymentID: int
    dose: str