# crud.py
# This module encapsulates all database operations for Employee
# Abstracts away raw DB queries from the API routes, keeping the code modular 
# Keeps DB logic separate and reusable, making the app cleaner and easier to maintain

from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, emp_id: int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    # ✅ Prevent duplicate email creation
    existing_emp = db.query(models.Employee).filter(models.Employee.email == employee.email).first()
    if existing_emp:
        raise HTTPException(status_code=400, detail="Email already exists")

    db_employee = models.Employee(name=employee.name, email=employee.email)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not db_employee:
        return None

    # Optional: prevent updating to an already-used email
    if employee.email:
        existing_email = db.query(models.Employee).filter(
            models.Employee.email == employee.email,
            models.Employee.id != emp_id
        ).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already used by another employee")

    db_employee.name = employee.name
    db_employee.email = employee.email
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not db_employee:
        return None

    db.delete(db_employee)
    db.commit()
    return db_employee
