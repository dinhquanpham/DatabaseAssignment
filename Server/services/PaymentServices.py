from sqlalchemy.orm import Session
from models import Payment
from schemas.PaymentSchema import PaymentCreateSchema, PaymentUpdateSchema
from fastapi import HTTPException

def read_payments(db: Session):
    return db.query(Payment).all()

def create_payment(db: Session, payment_create: PaymentCreateSchema):
    new_payment = Payment(paymentID = payment_create.paymentID, 
                          patientID = payment_create.patientID,
                          cost = payment_create.cost,
                          description = payment_create.description)
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment
    
def update_payment(db: Session, id: int, update_payment_info: PaymentUpdateSchema):
    payment_update = db.query(Payment).filter(Payment.paymentID == id).first()
    if (not payment_update):
         raise HTTPException(status_code=404, detail="payment not found")
    payment_data = update_payment_info.dict(exclude_unset=True)
    for key, value in payment_data.items():
        setattr(payment_update, key, value)
    db.add(payment_update)
    db.commit()
    db.refresh(payment_update)
    return(payment_update)

def delete_payment(db: Session, id: int):
    payment_delete = db.query(Payment).filter(Payment.paymentID == id).first()
    if (not payment_delete):
        raise HTTPException(status_code=404, detail="payment not found")
    db.delete(payment_delete)
    db.commit()
    return {
        'message': 'Successfully'
    }
