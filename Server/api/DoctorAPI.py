from fastapi import APIRouter, Depends
from services.DoctorServices import create_doctor, delete_doctor, read_doctors, update_doctor, delete_doctor
from schemas.DoctorSchema import DoctorSchema, DoctorCreateSchema, DoctorUpdateSchema
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get('', response_model=List[DoctorSchema])
def get_doctorss(db: Session = Depends(get_db)): 
    return read_doctors(db)

@router.post('', response_model=DoctorSchema)
def post_doctor(doctor_create: DoctorCreateSchema, db: Session = Depends(get_db)): 
    print(1)
    print(doctor_create)
    return create_doctor(db, doctor_create)

@router.put('/{id}', response_model=DoctorSchema)
def put(id: int, doctor_update_info: DoctorUpdateSchema, db: Session = Depends(get_db)):
    print(1)
    return update_doctor(db, id, doctor_update_info)

@router.delete('/{id}')
def get_one(id: int, db: Session = Depends(get_db)): 
    return delete_doctor(db, id)
    