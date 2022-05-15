from sqlalchemy.orm import Session
from models import Patient
from schemas.PatientSchema import PatientCreateSchema, PatientUpdateSchema
from fastapi import HTTPException

def read_patients(db: Session):
    return db.query(Patient).all()

def create_patient(db: Session, patient_create: PatientCreateSchema):
    new_patient = Patient(patientID = patient_create.patientID, 
                          name = patient_create.name,
                          age = patient_create.age,
                          gender = patient_create.gender,
                          address = patient_create.address,
                          disease = patient_create.disease,
                          patientStatus = patient_create.patientStatus)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient
    
def update_patient(db: Session, id: int, update_patient_info: PatientUpdateSchema):
    patient_update = db.query(Patient).filter(Patient.patientID == id).first()
    if (not patient_update):
         raise HTTPException(status_code=404, detail="patient not found")
    patient_data = update_patient_info.dict(exclude_unset=True)
    for key, value in patient_data.items():
        setattr(patient_update, key, value)
    db.add(patient_update)
    db.commit()
    db.refresh(patient_update)
    return(patient_update)

def delete_patient(db: Session, id: int):
    patient_delete = db.query(Patient).filter(Patient.patientID == id).first()
    if (not patient_delete):
        raise HTTPException(status_code=404, detail="patient not found")
    db.delete(patient_delete)
    db.commit()
    return {
        'message': 'Successfully'
    }
