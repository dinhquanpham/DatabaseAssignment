from fastapi import APIRouter, Depends
from services.PatientServices import create_patient, delete_patient, read_patients, update_patient, delete_patient
from schemas.PatientSchema import PatientSchema, PatientCreateSchema, PatientUpdateSchema
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get('', response_model=List[PatientSchema])
def get_patientss(db: Session = Depends(get_db)): 
    return read_patients(db)

@router.post('', response_model=PatientSchema)
def post_patient(patient_create: PatientCreateSchema, db: Session = Depends(get_db)): 
    print(1)
    print(patient_create)
    return create_patient(db, patient_create)

@router.put('/{id}', response_model=PatientSchema)
def put(id: int, patient_update_info: PatientUpdateSchema, db: Session = Depends(get_db)):
    return update_patient(db, id, patient_update_info)

@router.delete('/{id}')
def get_one(id: int, db: Session = Depends(get_db)): 
    return delete_patient(db, id)
    