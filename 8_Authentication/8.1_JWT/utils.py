from passlib.context import CryptContext


pwt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

fake_user_db = {
    'john' : {
        'username' : 'john',
        'hashed_password' : pwt_context.hash('secret123') 
    }
}


def get_user(username : str):
    user = fake_user_db.get(username)
    return user 


def verify_pass(plain_password, hashed_password):
    return pwt_context.verify(plain_password, hashed_password )