from fastapi import FastAPI, Depends, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from auth import create_access_token, verify_token
from models import UserInDB
from utils import get_user, verify_pass


app = FastAPI(title="JWT Auth Practice")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.post('/token')
def login(form_data : OAuth2PasswordRequestForm = Depends()):
    user_dict = get_user(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail='invalid user')
    if not verify_pass(form_data.password, user_dict['hashed_password']):
        raise HTTPException(status_code=400, detail= 'incorrect password') 

    access_token = create_access_token(data={'sub': form_data.username})   
    return {'access_token': access_token, 'token_type':'bearer'}

@app.get('/users')
def read_users(token : str = Depends(oauth2_scheme)):
    username = verify_token(token)
    return {'username':username}