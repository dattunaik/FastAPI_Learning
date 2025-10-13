from pydantic import BaseModel, EmailStr
from typing import Optional

class EmployeeBase(BaseModel):
    name : str
    email : EmailStr

class EmployeeCreate(EmployeeBase):
    # email : Optional[EmailStr]
    pass

class EmployeeUpdate(EmployeeBase):
    pass


#output for returning employee data 
class EmployeeOut(EmployeeBase):
    id : int 

    #allows pydantic to read data directly from ORM Objects (SQLAlchemy models)
    class Config:
        orm_mode = True 