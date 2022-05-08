from xmlrpc.client import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Department(Base):
    __tablename__ = "Department"

    departmentID = Column(Integer, primary_key=True, index=True)
    departmentName = Column(Text, index=True)

    # owner = relationship("User", back_populates="items")
