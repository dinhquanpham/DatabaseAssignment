from fastapi import APIRouter, Depends
from services.AppointmentServices import create_appointment, delete_appointment, read_appointments, update_appointment, delete_appointment
from schemas.AppointmentSchema import AppointmentSchema, AppointmentCreateSchema, AppointmentUpdateSchema
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get('', response_model=List[AppointmentSchema])
def get_appointmentss(db: Session = Depends(get_db)): 
    return read_appointments(db)

@router.post('', response_model=AppointmentSchema)
def post_appointment(appointment_create: AppointmentCreateSchema, db: Session = Depends(get_db)): 
    print(1)
    print(appointment_create)
    return create_appointment(db, appointment_create)

@router.put('/{id}', response_model=AppointmentSchema)
def put(id: int, appointment_update_info: AppointmentUpdateSchema, db: Session = Depends(get_db)):
    return update_appointment(db, id, appointment_update_info)

@router.delete('/{id}')
def get_one(id: int, db: Session = Depends(get_db)): 
    return delete_appointment(db, id)
    