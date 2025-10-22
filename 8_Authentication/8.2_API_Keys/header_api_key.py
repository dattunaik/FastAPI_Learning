from fastapi import FastAPI, Depends, HTTPException, Header


app = FastAPI(title="API KEYS")

API_KEY = 'my-secret-key'

def get_api_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=400, detail='incorrect api key')
    return api_key

@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {'output': 'Access Granted'}