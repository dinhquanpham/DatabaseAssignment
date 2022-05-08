from xmlrpc.client import DateTime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Department(Base):
    __tablename__ = "departments"

    departmentID = Column(Integer, primary_key=True, index=True)
    departmentName = Column(Text)

    # owner = relationship("User", back_populates="items")
