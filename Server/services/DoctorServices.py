from sqlalchemy.orm import Session
from models import Doctor
from schemas.DoctorSchema import DoctorCreateSchema, DoctorUpdateSchema
from fastapi import HTTPException

def read_doctors(db: Session):
    return db.query(Doctor).all()

def create_doctor(db: Session, doctor_create: DoctorCreateSchema):
    new_doctor = Doctor(doctorID = doctor_create.doctorID, 
                        departmentID = doctor_create.departmentID,
                        name = doctor_create.name,
                        age = doctor_create.age,
                        gender = doctor_create.gender)
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor
    
def update_doctor(db: Session, id: int, update_doctor_info: DoctorUpdateSchema):
    doctor_update = db.query(Doctor).filter(Doctor.doctorID == id).first()
    if (not doctor_update):
         raise HTTPException(status_code=404, detail="doctor not found")
    doctor_data = update_doctor_info.dict(exclude_unset=True)
    for key, value in doctor_data.items():
        setattr(doctor_update, key, value)
    db.add(doctor_update)
    db.commit()
    db.refresh(doctor_update)
    return(doctor_update)

def delete_doctor(db: Session, id: int):
    doctor_delete = db.query(Doctor).filter(Doctor.doctorID == id).first()
    if (not doctor_delete):
        raise HTTPException(status_code=404, detail="doctor not found")
    db.delete(doctor_delete)
    db.commit()
    return {
        'message': 'Successfully'
    }
