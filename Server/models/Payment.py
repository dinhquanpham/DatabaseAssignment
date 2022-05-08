
from ast import For
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

from models.Base import Base

class Payment(Base):
    __tablename__ = "payments"

    paymentID = Column(Integer, primary_key=True, index=True)
    patientID = Column(Integer, ForeignKey("patients.patientID"), index = True)
    cost = Column(Integer)
    description = Column(Text)
    patients = relationship("Patient", backref = backref("payments", uselist = False))
    # owner = relationship("User", back_populates="items")
