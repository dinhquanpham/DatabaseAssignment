
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Patient(Base):    
    __tablename__ = "Patient"

    patientID = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(45), index=True)
    age = Column(Integer, index=True)
    gender = Column(VARCHAR(20))
    address = Column(VARCHAR(45))
    disease = Column(VARCHAR(45))
    patientStatus = Column(Text)
    # owner = relationship("User", back_populates="items")
