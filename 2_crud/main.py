from fastapi import FastAPI, HTTPException
from models_val import Employee
from typing import List

app = FastAPI()

# In-memory database
employees_db: List[Employee] = []

# 1. Get all employees
@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees_db


# 2. Get specific employee by ID
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for employee in employees_db:
        if employee.id == emp_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


# 3. Add a new employee
@app.post("/employees_add", response_model=Employee)
def create_employee(new_employee: Employee):
    for employee in employees_db:
        if employee.id == new_employee.id:
            raise HTTPException(status_code=400, detail="Employee already exists")
    employees_db.append(new_employee)
    return new_employee


# 4. Update an employee
@app.put("/employees/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")


# 5. Delete an employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[index]
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")
