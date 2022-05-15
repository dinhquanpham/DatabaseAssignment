from sqlalchemy.orm import Session
from models import Appointment
from schemas.AppointmentSchema import AppointmentCreateSchema, AppointmentUpdateSchema
from fastapi import HTTPException

def read_appointments(db: Session):
    return db.query(Appointment).all()

def create_appointment(db: Session, appointment_create: AppointmentCreateSchema):
    new_appointment = Appointment(appointmentID = appointment_create.appointmentID, 
                                  doctorID = appointment_create.doctorID,
                                  patientID = appointment_create.patientID,
                                  roomNumber = appointment_create.roomNumber,
                                  start_time = appointment_create.start_time,
                                  end_time = appointment_create.end_time)
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment
    
def update_appointment(db: Session, id: int, update_appointment_info: AppointmentUpdateSchema):
    appointment_update = db.query(Appointment).filter(Appointment.appointmentID == id).first()
    if (not appointment_update):
         raise HTTPException(status_code=404, detail="appointment not found")
    appointment_data = update_appointment_info.dict(exclude_unset=True)
    for key, value in appointment_data.items():
        setattr(appointment_update, key, value)
    db.add(appointment_update)
    db.commit()
    db.refresh(appointment_update)
    return(appointment_update)

def delete_appointment(db: Session, id: int):
    appointment_delete = db.query(Appointment).filter(Appointment.appointmentID == id).first()
    if (not appointment_delete):
        raise HTTPException(status_code=404, detail="appointment not found")
    db.delete(appointment_delete)
    db.commit()
    return {
        'message': 'Successfully'
    }
