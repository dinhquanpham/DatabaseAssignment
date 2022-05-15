from datetime import datetime
from pydantic import BaseModel

class AppointmentSchema(BaseModel):
    appointmentID: int
    doctorID: int
    patientID: int
    roomNumber: int
    start_time: datetime
    end_time: datetime

    class Config:
        orm_mode = True

class AppointmentCreateSchema(BaseModel):
    appointmentID: int
    doctorID: int
    patientID: int
    roomNumber: int
    start_time: datetime
    end_time: datetime

class AppointmentUpdateSchema(BaseModel):
    appointmentID: int
    doctorID: int
    patientID: int
    roomNumber: int
    start_time: datetime
    end_time: datetime