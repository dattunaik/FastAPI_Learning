#FAST API WITH SQLALCHEMY / SQLITE FOR DB / PYDANTIC for data validation and serialization
#REST API TO HANDLE AND MANAGE THE EMPLOYEE DATABASE


#this is where the API is defined, exposing endpoints for the users 
#denotes the entrypoint of the API Server 
import crud, models, schemas
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List 


Base.metadata.create_all(bind=engine)

app = FastAPI()

#dependency wit the DB 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#end_points
#1.create an employee
@app.post('/employees', response_model=schemas.EmployeeOut)
def create_employee(employee : schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.create_employee(db, employee)
    return db_employee

#2.Read all employees
@app.get('/employees', response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

#3.Get a specfic employee 
@app.get('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id:int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return employee

#4.Update an employee
@app.put('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def update_employee(emp_id :int, employee: schemas.EmployeeUpdate, db: Session =Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return db_employee

#5. delete an employee
@app.delete('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def del_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return employee 

    #return {'detail': 'Employee is deleted} -> for this "response_model=schemas.EmployeeOut" not required
