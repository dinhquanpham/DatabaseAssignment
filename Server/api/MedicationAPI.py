from fastapi import APIRouter, Depends
from services.MedicationServices import create_medication, delete_medication, read_medications, update_medication, delete_medication
from schemas.MedicationSchema import MedicationSchema, MedicationCreateSchema, MedicationUpdateSchema
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get('', response_model=List[MedicationSchema])
def get_medicationss(db: Session = Depends(get_db)): 
    return read_medications(db)

@router.post('', response_model=MedicationSchema)
def post_medication(medication_create: MedicationCreateSchema, db: Session = Depends(get_db)): 
    print(1)
    print(medication_create)
    return create_medication(db, medication_create)

@router.put('/{id}', response_model=MedicationSchema)
def put(id: int, medication_update_info: MedicationUpdateSchema, db: Session = Depends(get_db)):
    return update_medication(db, id, medication_update_info)

@router.delete('/{id}')
def get_one(id: int, db: Session = Depends(get_db)): 
    return delete_medication(db, id)
    