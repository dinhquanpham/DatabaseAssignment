from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from models.Base import Base

class Appointment(Base):
    __tablename__ = "appointments"

    appoIntegermentID = Column(Integer, primary_key=True, index=True)
    doctorID = Column(Integer, index=True)
    pationID = Column(Integer, index=True)
    roomNumber = Column(Integer, index = True)
    start_time = Column(DateTime,index = True)
    end_time = Column(DateTime, index = True)
    # owner = relationship("User", back_populates="items")
