
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Room(Base):
    __tablename__ = "Room"

    roomNumber = Column(Integer, primary_key=True, index=True)
    roomType = Column(VARCHAR(45), index = True)
    status = Column(VARCHAR(20))
    # owner = relationship("User", back_populates="items")
