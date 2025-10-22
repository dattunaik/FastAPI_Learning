from fastapi import FastAPI, Depends


app = FastAPI()

class settings:
    def __init__(self):
        self.api_key = 'mysecret'
        self.password = "*&&***"
        self.debug = True

def get_settings():
    return settings()

@app.get('/config')
def get_config(Settings : settings = Depends(get_settings)):
    return {'api_key': Settings.api_key, 'PASSWORD':Settings.password}