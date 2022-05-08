from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from models.Base import Base
from models.Patient import Patient
from sqlalchemy.orm import backref

class Appointment(Base):
    __tablename__ = "appointments"

    appointmentID = Column(Integer, primary_key=True, index=True)
    doctorID = Column(Integer, ForeignKey("doctors.doctorID"), index=True)
    patientID = Column(Integer , ForeignKey("patients.patientID"))
    roomNumber = Column(Integer, ForeignKey("rooms.roomNumber"), index = True)
    start_time = Column(DateTime,index = True)
    end_time = Column(DateTime, index = True)
    
    
    #patient <> apointment (patientID)
    # owner = relationship("User", back_populates="items")
