from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get('/wait')
async def wait():
    await asyncio.sleep(5) # non-blocking sleep 
    return {'message': 'Finished waiting'}