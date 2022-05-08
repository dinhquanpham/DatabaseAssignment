from xmlrpc.client import DateTime
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Doctor(Base):
    __tablename__ = "Doctor"

    doctorID = Column(Integer, primary_key=True, index=True)
    departmentID = Column(Integer, index=True)
    name = Column(VARCHAR(45), index=True)
    age = Column(Integer, index = True)
    gender = Column(VARCHAR(20),index = True)
    # owner = relationship("User", back_populates="items")
