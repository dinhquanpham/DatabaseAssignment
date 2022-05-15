from fastapi import APIRouter, Depends
from services.DepartmentServices import create_department, delete_department, read_departments, update_department, delete_department
from schemas.DepartmentSchema import DepartmentSchema, DepartmentCreateSchema, DepartmentUpdateSchema
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get('', response_model=List[DepartmentSchema])
def get_departmentss(db: Session = Depends(get_db)): 
    return read_departments(db)

@router.post('', response_model=DepartmentSchema)
def post_department(department_create: DepartmentCreateSchema, db: Session = Depends(get_db)): 
    print(1)
    print(department_create)
    return create_department(db, department_create)

@router.put('/{id}', response_model=DepartmentSchema)
def put(id: int, department_update_info: DepartmentUpdateSchema, db: Session = Depends(get_db)):
    return update_department(db, id, department_update_info)

@router.delete('/{id}')
def get_one(id: int, db: Session = Depends(get_db)): 
    return delete_department(db, id)
    