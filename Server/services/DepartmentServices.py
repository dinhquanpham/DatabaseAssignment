from sqlalchemy.orm import Session
from models import Department
from schemas.DepartmentSchema import DepartmentCreateSchema, DepartmentUpdateSchema
from fastapi import HTTPException

def read_departments(db: Session):
    return db.query(Department).all()

def create_department(db: Session, department_create: DepartmentCreateSchema):
    new_department = Department(departmentID = department_create.departmentID, 
                                departmentName = department_create.departmentName)
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department
    
def update_department(db: Session, id: int, update_department_info: DepartmentUpdateSchema):
    department_update = db.query(Department).filter(Department.departmentID == id).first()
    if (not department_update):
         raise HTTPException(status_code=404, detail="department not found")
    department_data = update_department_info.dict(exclude_unset=True)
    for key, value in department_data.items():
        setattr(department_update, key, value)
    db.add(department_update)
    db.commit()
    db.refresh(department_update)
    return(department_update)

def delete_department(db: Session, id: int):
    department_delete = db.query(Department).filter(Department.departmentID == id).first()
    if (not department_delete):
        raise HTTPException(status_code=404, detail="department not found")
    db.delete(department_delete)
    db.commit()
    return {
        'message': 'Successfully'
    }
