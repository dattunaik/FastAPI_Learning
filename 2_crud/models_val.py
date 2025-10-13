from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int = Field(..., #pydantic knows that id is required/mandatory
                    gt=0, # we use gt as greater than & lt as less than
                    title="Employee ID") #knows the title of the field
    name: str = Field(...,
                      min_length=3, #min_length and max_length used for string length 
                      max_length=30,
                      #regex=r'^[A-Za-z ]{3,30}$', #regex function used for the input validation
                      description="Only letters and spaces allowed (3–30 characters)" 
                      #description will describe the field
                      )
    age: Optional[int] = Field(gt=0, default=None)
    department: str = Field(...,min_length=3,max_length=30)


