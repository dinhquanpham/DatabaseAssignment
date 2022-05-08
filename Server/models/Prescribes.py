
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Prescribes(Base):
    __tablename__ = "Prescribes"

    appointmentID = Column(Integer, primary_key=True, index=True)
    medicineCode = Column(Integer, index = True)
    paymentID = Column(Integer)
    dose = Column(Text)
    # owner = relationship("User", back_populates="items")
