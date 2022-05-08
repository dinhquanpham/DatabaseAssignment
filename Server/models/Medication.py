
from xmlrpc.client import DateTime
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Medication(Base):
    __tablename__ = "medications"

    medicineCode = Column(Integer, primary_key=True, index=True)
    medicineName = Column(Text)
    medicineCost = Column(Integer, index=True)
    medicineDescription = Column(Text)
    # owner = relationship("User", back_populates="items")
