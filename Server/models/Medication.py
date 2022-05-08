
from xmlrpc.client import DateTime
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Medication(Base):
    __tablename__ = "Medication"

    medicineCode = Column(Integer, primary_key=True, index=True)
    medicineName = Column(Text, index=True)
    medicineCost = Column(Integer, index=True)
    medicineDescription = Column(Text, index = True)
    # owner = relationship("User", back_populates="items")
