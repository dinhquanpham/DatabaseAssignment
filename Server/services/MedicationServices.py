from sqlalchemy.orm import Session
from models import Medication
from schemas.MedicationSchema import MedicationCreateSchema, MedicationUpdateSchema
from fastapi import HTTPException

def read_medications(db: Session):
    return db.query(Medication).all()

def create_medication(db: Session, medication_create: MedicationCreateSchema):
    new_medication = Medication(medicineCode = medication_create.medicineCode, 
                                medicineName = medication_create.medicineName,
                                medicineCost = medication_create.medicineCost,
                                medicineDescription = medication_create.medicineDescription)
    db.add(new_medication)
    db.commit()
    db.refresh(new_medication)
    return new_medication
    
def update_medication(db: Session, id: int, update_medication_info: MedicationUpdateSchema):
    medication_update = db.query(Medication).filter(Medication.medicineCode == id).first()
    if (not medication_update):
         raise HTTPException(status_code=404, detail="medication not found")
    medication_data = update_medication_info.dict(exclude_unset=True)
    for key, value in medication_data.items():
        setattr(medication_update, key, value)
    db.add(medication_update)
    db.commit()
    db.refresh(medication_update)
    return(medication_update)

def delete_medication(db: Session, id: int):
    medication_delete = db.query(Medication).filter(Medication.medicineCode == id).first()
    if (not medication_delete):
        raise HTTPException(status_code=404, detail="medication not found")
    db.delete(medication_delete)
    db.commit()
    return {
        'message': 'Successfully'
    }
