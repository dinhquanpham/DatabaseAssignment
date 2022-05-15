from pydantic import BaseModel

class PaymentSchema(BaseModel):
    paymentID: int
    patientID: int
    cost: int
    description: str

    class Config:
        orm_mode = True

class PaymentCreateSchema(BaseModel):
    paymentID: int
    patientID: int
    cost: int
    description: str

class PaymentUpdateSchema(BaseModel):
    paymentID: int
    patientID: int
    cost: int
    description: str