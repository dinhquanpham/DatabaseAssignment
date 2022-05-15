from sqlalchemy.orm import Session
from models import Prescription
from schemas.PrescriptionSchema import PrescriptionCreateSchema, PrescriptionUpdateSchema
from fastapi import HTTPException

def read_prescriptions(db: Session):
    return db.query(Prescription).all()

def create_prescription(db: Session, prescription_create: PrescriptionCreateSchema):
    new_prescription = Prescription(prescriptionID = prescription_create.prescriptionID,
                                    appointmentID = prescription_create.appointmentID, 
                                    medicineCode = prescription_create.medicineCode,
                                    paymentID = prescription_create.paymentID,
                                    dose = prescription_create.dose)
    db.add(new_prescription)
    db.commit()
    db.refresh(new_prescription)
    return new_prescription
    
def update_prescription(db: Session, id: int, update_prescription_info: PrescriptionUpdateSchema):
    prescription_update = db.query(Prescription).filter(Prescription.prescriptionID ==id).first()
    if (not prescription_update):
         raise HTTPException(status_code=404, detail="prescription not found")
    prescription_data = update_prescription_info.dict(exclude_unset=True)
    for key, value in prescription_data.items():
        setattr(prescription_update, key, value)
    db.add(prescription_update)
    db.commit()
    db.refresh(prescription_update)
    return(prescription_update)

def delete_prescription(db: Session, id: int):
    prescription_delete = db.query(Prescription).filter(Prescription.prescriptionID == id).first()
    if (not prescription_delete):
        raise HTTPException(status_code=404, detail="prescription not found")
    db.delete(prescription_delete)
    db.commit()
    return {
        'message': 'Successfully'
    }
