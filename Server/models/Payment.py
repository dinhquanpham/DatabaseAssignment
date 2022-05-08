
from sqlalchemy import VARCHAR, Boolean, Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import relationship

from models.Base import Base

class Payment(Base):
    __tablename__ = "Payment"

    paymentID = Column(Integer, primary_key=True, index=True)
    patientID = Column(Integer, index = True)
    cost = Column(Integer)
    description = Column(Text)
    # owner = relationship("User", back_populates="items")
