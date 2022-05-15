from fastapi import APIRouter, Depends
from services.PrescriptionServices import create_prescription, delete_prescription, read_prescriptions, update_prescription
from schemas.PrescriptionSchema import PrescriptionSchema, PrescriptionCreateSchema, PrescriptionUpdateSchema
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get('', response_model=List[PrescriptionSchema])
def get_prescriptionss(db: Session = Depends(get_db)): 
    return read_prescriptions(db)

@router.post('', response_model=PrescriptionSchema)
def post_prescription(prescription_create: PrescriptionCreateSchema, db: Session = Depends(get_db)): 
    print(1)
    print(prescription_create)
    return create_prescription(db, prescription_create)

@router.put('/{id}', response_model=PrescriptionSchema)
def put(id: int, prescription_update_info: PrescriptionUpdateSchema, db: Session = Depends(get_db)):
    return update_prescription(db, id, prescription_update_info)

@router.delete('/{id}')
def get_one(id: int, db: Session = Depends(get_db)): 
    return delete_prescription(db, id)
    