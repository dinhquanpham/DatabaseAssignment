from fastapi import APIRouter, Depends
from services.PaymentServices import create_payment, delete_payment, read_payments, update_payment, delete_payment
from schemas.PaymentSchema import PaymentSchema, PaymentCreateSchema, PaymentUpdateSchema
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get('', response_model=List[PaymentSchema])
def get_paymentss(db: Session = Depends(get_db)): 
    return read_payments(db)

@router.post('', response_model=PaymentSchema)
def post_payment(payment_create: PaymentCreateSchema, db: Session = Depends(get_db)): 
    print(1)
    print(payment_create)
    return create_payment(db, payment_create)

@router.put('/{id}', response_model=PaymentSchema)
def put(id: int, payment_update_info: PaymentUpdateSchema, db: Session = Depends(get_db)):
    return update_payment(db, id, payment_update_info)

@router.delete('/{id}')
def get_one(id: int, db: Session = Depends(get_db)): 
    return delete_payment(db, id)
    