from fastapi import FastAPI

app = FastAPI()

# @app.get('/')
# def dattu():
#     return {'message':'Its a basic version to test!'}


#Pydantic Demo 
from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str 

@app.get('/user', response_model=User)
def get_user():
    return User(id=1, name='dattu')


 