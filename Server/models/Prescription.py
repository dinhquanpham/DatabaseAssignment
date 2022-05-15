
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Prescription(Base):
    __tablename__ = "prescriptions"

    prescriptionID = Column(Integer, primary_key=True, index=True)
    appointmentID = Column(Integer,  ForeignKey("appointments.appointmentID"), index = True)
    medicineCode = Column(Integer, ForeignKey("medications.medicineCode"), index = True)
    paymentID = Column(Integer, ForeignKey("payments.paymentID"), index = True)
    dose = Column(Text)
    # owner = relationship("User", back_populates="items")
