
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Prescribes(Base):
    __tablename__ = "prescribes"

    appointmentID = Column(Integer,  ForeignKey("appointments.appointmentID"), primary_key = True)
    medicineCode = Column(Integer, ForeignKey("medications.medicineCode"), primary_key = True)
    paymentID = Column(Integer, ForeignKey("payments.paymentID"))
    dose = Column(Text)
    # owner = relationship("User", back_populates="items")
